from fastapi import APIRouter, FastAPI, Depends, HTTPException
from Aplications.Services.autenticacao_service import AutenticacaoService
from Aplications.Models.autenticacaoModel import Autenticacao
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
rotas = APIRouter()
import json

rotas = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

autenticacao_service = AutenticacaoService()

@rotas.post("/autenticar")
def autenticacao(autenticacao: Autenticacao):
    data = autenticacao_service.gerar_token(usuario=autenticacao.login,senha= autenticacao.senha)
    return data
