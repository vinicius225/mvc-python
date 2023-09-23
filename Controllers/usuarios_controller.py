from fastapi import APIRouter
from Aplication.Services.usuarios_service import UsuariosServices
rotas = APIRouter()

usuario_services = UsuariosServices()
@rotas.get('/usuario')
def listar_usuarios():
    return usuario_services.listar_usuarios()
