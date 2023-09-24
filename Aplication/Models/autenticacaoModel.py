from pydantic import BaseModel, Field
class Autenticacao(BaseModel):
    login: str = Field(..., description= "login é um campo obrigatorio")
    senha:str = Field(..., description= "senha é um campo obrigatorio")