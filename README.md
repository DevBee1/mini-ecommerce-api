# Mini E-commerce API

API REST de e-commerce feita com Python, FastAPI e SQLite. Projeto pessoal para praticar API REST, SQL e Git.

## O que já faz
- Cadastra produtos, com validação (nome obrigatório, preço maior que zero, estoque não negativo)
- Lista todos os produtos
- Busca um produto pelo id (retorna 404 se não existir)

## Rotas
| Método | Rota | Descrição |
|---|---|---|
| POST | /produtos | Cadastra um produto |
| GET | /produtos | Lista os produtos |
| GET | /produtos/{id} | Busca um produto |

## Tecnologias
Python, FastAPI, SQLite, Uvicorn

## Como rodar
1. Crie e ative o ambiente virtual:
   `python -m venv .venv` e `.venv\Scripts\activate` (Windows)
2. Instale as dependências: `pip install -r requirements.txt`
3. Rode a API: `uvicorn main:app --reload`
4. Abra `http://127.0.0.1:8000/docs` para testar as rotas

## Próximos passos
- Carrinho e pedidos
- Função de IA para gerar a descrição do produto
- Interface web
