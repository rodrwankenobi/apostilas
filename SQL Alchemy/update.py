from core import engine, users_table
from sqlalchemy import update

con=engine.connect()

up=update(users_table).where(users_table.c.id==1).values(idade=3)
up=update(users_table).where(users_table.c.id==2).values(idade=29)
result=con.execute(up)

print(result.rowcount)