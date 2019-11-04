from bottle import get, post, request, response, run, jinja2_view

@get("/login")
@jinja2_view("Views\login.html")
def pag_inicial_get():
    return

@post("/login")
@jinja2_view("Views\login.html")
def pag_inicial_post():
    username=request.forms.get("username")
    return f"Olá {username}, você está logado!"

if __name__=='__main__':
    run(host='localhost', port=8080)