from app import app
from sqlalchemy import insert
from db.db import engine
from db.tbl_disco import tbl_disco


engine=engine()
ins=insert.bind(engine)

def insert_disco(disco):
    ins.values(disco.id_banda,disco.id_disco,disco.titulo, disco.ano, disco.preco)