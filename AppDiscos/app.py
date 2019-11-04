from bottle import Bottle, run, post, get, request, response
from controller.insert_banda import insert_banda
from controller.insert_disco import insert_disco
from models.banda import Banda
from models.disco import Disco

PORT=8080
app=Bottle()

@post("/cadastro_banda")
def inserir_banda():
    banda=Banda(
        {
            id: request.id,
            nome: request.nome,
            genero=request.genero
        }
    )

run(server='localhost',port=8080)