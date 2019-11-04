from pprint import pprint
from sqlalchemy import select
from core import users_table

s = select([users_table])

for row in s.execute():
    pprint(row)