from sqlalchemy import create_engine, Table, MetaData, Column, Integer, String, DateTime
from datetime import datetime

engine = create_engine("sqlite:///teste.db", echo=True)
metadata=MetaData(bind=engine)

users_table=Table('usuarios',metadata,
        Column('id',Integer, primary_key=True),
        Column('nome',String(40), index=True),
        Column('idade',Integer, nullable=False),
        Column('senha',String(40)),
        Column('criado_em',DateTime, default=datetime.now)
    )

metadata.create_all()