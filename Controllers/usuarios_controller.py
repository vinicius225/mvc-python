from fastapi import APIRouter
from Aplication.Services.usuarios_service import UsuariosServices
rotas = APIRouter()
import json

usuario_services = UsuariosServices()
@rotas.get('/usuario')
def listar_usuarios():
    retorno =  usuario_services.listar_usuarios()
    return retorno
