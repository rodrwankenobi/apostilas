from core import engine, users_table

con=engine.connect()
ins=users_table.insert()
new_user=ins.values([
    {
        'id': 1,
        'nome': 'Danilo',
        'idade': 4,
        'senha': 'danilo27'
    },
    {
        'id': 2,
        'nome': 'Rodrigo',
        'idade': 30,
        'senha': 'danilo27'
    },
    {
        'id': 3,
        'nome': 'Mia',
        'idade': 33,
        'senha': 'danilo27'
    }
])
con.execute(new_user)