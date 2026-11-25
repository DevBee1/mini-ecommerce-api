import sqlite3
from contextlib import contextmanager

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

DB = "loja.db"
app = FastAPI(title="Mini E-commerce")


@contextmanager
def conectar():
    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row
    try:
        yield con
        con.commit()
    finally:
        con.close()


def criar_tabelas():
    with conectar() as con:
        con.execute(
            """CREATE TABLE IF NOT EXISTS produtos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                preco REAL NOT NULL,
                estoque INTEGER NOT NULL DEFAULT 0
            )"""
        )


criar_tabelas()


class ProdutoIn(BaseModel):
    nome: str = Field(min_length=1)
    preco: float = Field(gt=0)
    estoque: int = Field(default=0, ge=0)


@app.post("/produtos", status_code=201)
def criar_produto(p: ProdutoIn):
    with conectar() as con:
        cur = con.execute(
            "INSERT INTO produtos (nome, preco, estoque) VALUES (?, ?, ?)",
            (p.nome, p.preco, p.estoque),
        )
        return {"id": cur.lastrowid, **p.model_dump()}


@app.get("/produtos")
def listar_produtos():
    with conectar() as con:
        return [dict(r) for r in con.execute("SELECT * FROM produtos")]


@app.get("/produtos/{produto_id}")
def obter_produto(produto_id: int):
    with conectar() as con:
        r = con.execute("SELECT * FROM produtos WHERE id = ?", (produto_id,)).fetchone()
    if r is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return dict(r)