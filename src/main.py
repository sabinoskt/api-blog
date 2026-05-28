from fastapi import FastAPI
from api.Routers.UsuariosRouter import router

app = FastAPI(debug=True, title="Blog")

app.include_router(router)
