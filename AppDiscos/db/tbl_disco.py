from sqlalchemy import Table, Column, MetaData, Integer, String, Numeric
from db import engine

engine=engine()
metadata=MetaData()

def tbl_disco():
    tbl_disco=Table('tbl_banda',metadata,
    Column('id_banda', Integer, foreign_key=True),
    Column('id_disco',Integer, primary_key=True),
    Column('titulo',String, nullable=False),
    Column('ano',Integer, nullable=False),
    Column('preco',Numeric(5,2),nullable=False)
    )

    metadata.create_all()
    return tbl_disco

