from fastapi import APIRouter, FastAPI, Depends, HTTPException
from Aplication.Services.autenticacao_service import AutenticacaoService
from Aplication.Models.autenticacaoModel import Autenticacao
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
rotas = APIRouter()
import json

rotas = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@rotas.post("/autenticar")
def autenticacao(lautenticacao: Autenticacao):
    data = AutenticacaoService().gerar_token(lautenticacao.login, autenticacao.senha)
    return data
