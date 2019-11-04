from app import app
from sqlalchemy import insert
from db.db import engine
from db.tbl_banda import tbl_banda


engine=engine()
ins=insert.bind(engine)

def insert_banda(banda):
    ins.values(banda.id_banda,banda.nome,banda.genero)
    