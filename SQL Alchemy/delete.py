from core import engine, users_table
from sqlalchemy import delete

con=engine.connect()

del1=delete(users_table).where(users_table.c.id==3)

result=con.execute(del1)

print(result.rowcount)