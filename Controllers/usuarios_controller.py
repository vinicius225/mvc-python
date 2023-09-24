from fastapi import APIRouter, Depends, HTTPException
from Aplications.Services.usuarios_service import UsuariosServices
from Aplications.Services.autenticacao_service import AutenticacaoService
rotas = APIRouter()
import json

usuario_services = UsuariosServices()
autenticacao_services = AutenticacaoService()
@rotas.get('/usuario')
def listar_usuarios(usuario : bool = Depends(autenticacao_services.decode_token)):
    if usuario:
        retorno =  usuario_services.listar_usuarios()
        return retorno
    return   HTTPException(status_code=401, detail= "Token invalido")
