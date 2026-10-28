from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from schemas import ProdutoCriar, ProdutoResposta
from contextlib import asynccontextmanager

from database import Base, engine, get_db
from models import Produto


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield 

app = FastAPI(title="StockFlow", lifespan=lifespan,)



@app.get("/")
def inicio():
    return{"mensagem": "API do StockFlw funcionando!"}

@app.post("/produtos", response_model=ProdutoResposta, status_code=201,)
def cadastrar_produto(produto: ProdutoCriar, db: Session = Depends(get_db)):
    novo_produto = Produto(
        nome=produto.nome,
        codigo=produto.codigo,
        preco=produto.preco,
    )

    db.add(novo_produto)

    try: 
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="Não foi possível cadastrar: verifique se o código já existe.",
        )

    db.refresh(novo_produto)
    return novo_produto
    

@app.get("/produtos", response_model=list[ProdutoResposta])
def listar_produtos(db: Session = Depends(get_db)):
    consulta = select(Produto).order_by(Produto.id)
    return db.scalars(consulta).all()


@app.get("/produtos/{produto_id}", response_model=ProdutoResposta)
def consultar_produto(
    produto_id: int,
    db: Session = Depends(get_db),
):
    produto = db.get(Produto, produto_id)

    if produto is None:
        raise HTTPException(
            status_code=404,
            detail="Produto não encontrado.",
        )
    
    return produto