import uvicorn
from starlette.applications import Starlette
from app.routes import routes

app = Starlette(debug=True, routes=routes)

if __name__ == "__main__":
    uvicorn.run("server:app", reload=True, port=5000)
    # aqui fala pro uvicorn abrir o arquivo "run" e detro dele buscar a variável "app"