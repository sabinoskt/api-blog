from src.api.Repositories.UsuariosRepository import UsuariosRepository
from fastapi import status, HTTPException

class UsuariosService:
    def __init__(self):
        self.usuarios_repository = UsuariosRepository()

    def registar(self, data):
        try:
            email = self.usuarios_repository.buscar_por_email(data.email)

            if email:
                raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="E-mail já existe!")

            self.usuarios_repository.registrar(data)
            return HTTPException(
                status_code=status.HTTP_201_CREATED, detail="Cadastrado com sucesso!", headers={"Sucesso": "Ok"}
            )

        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    def login(self, data):
        ...

    def logout(self):
        ...
