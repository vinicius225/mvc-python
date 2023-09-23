from fastapi import APIRouter

rotas = APIRouter()

@rotas.get('/usuario')
def listar_usuarios():
    return "lista de usuarios"
