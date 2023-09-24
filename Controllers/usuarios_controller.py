from fastapi import APIRouter, Depends, HTTPException, Header
from Aplications.Services.usuarios_service import UsuariosServices
from Aplications.Services.autenticacao_service import AutenticacaoService
rotas = APIRouter()
import json

usuario_services = UsuariosServices()
autenticacao_services = AutenticacaoService()
@rotas.get('/usuario')
def listar_usuarios(authorization  = Header(None)):
    if authorization is None:
        raise HTTPException(status_code=401, detail="Autenticação JWT obrigatória")
    token = authorization.split("Bearer ")[1] if authorization.startswith("Bearer ") else None
    if token is None:
        raise HTTPException(status_code=401, detail="Token JWT inválido")
    user = autenticacao_services.decode_token(token)  # Substitua pela sua função de decodificação de token JWT
    if user == False:
        raise HTTPException(status_code=401, detail="Token JWT inválido")
    return user
