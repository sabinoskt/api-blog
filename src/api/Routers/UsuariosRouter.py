from fastapi import APIRouter
from api.Services.UsuariosService import UsuariosService
from api.Schemas.UsuariosSchema import UsuarioSchema

router = APIRouter(tags=["Usuários"])
usaurios = UsuariosService()

@router.post("/registrar")
def registrar(data: UsuarioSchema):
    return usaurios.registar(data)

@router.post("/login")
def login(data: UsuarioSchema):
    usaurios.login(data)

@router.post("/logout")
def logout():
    usaurios.logout()
