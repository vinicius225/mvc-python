from Domain.Repositories.usuario_repository import usuario_repository
class UsuariosServices:
    def __init__(self):
        self.repositorio = usuario_repository()
    
    def listar_usuarios(self):
        return self.repositorio.listar_usuarios()