from sqlalchemy import Table, Column, MetaData, Integer, String
from db import engine

engine=engine()
metadata=MetaData()

def tbl_banda():
    tblBanda=Table('tbl_banda',metadata,
        Column('id',Integer, primary_key=True),
        Column('nome',String, nullable=False),
        Column('genero',Integer, nullable=False),
    )

    metadata.create_all()

    return tblBanda