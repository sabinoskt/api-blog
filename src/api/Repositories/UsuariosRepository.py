from sqlalchemy.orm import sessionmaker
from src.api.Models.UsuariosModel import engine
from src.api.Models.UsuariosModel import Usuarios

class UsuariosRepository:
    def __init__(self):
        self.sessionlocal = sessionmaker(bind=engine)
        self.session = self.sessionlocal()

    def buscar_por_email(self, email):
        try:
            usuario = self.session.query(Usuarios).filter(Usuarios.email == email).first()
            return usuario
        except Exception as e:
            return str(e)

    def registrar(self, data):
        try:
            usuario = Usuarios(
                email=data.email,
                password=data.password
            )

            self.session.add(usuario)
            self.session.commit()

            return True
        except Exception as e:
            return str(e)

        finally:
            self.session.close()
