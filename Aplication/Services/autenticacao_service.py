from Domain.Repositories.usuario_repository import usuario_repository
from Aplication.Models.autenticacaoModel import Autenticacao
import jwt
import json
from datetime import datetime, timedelta
class AutenticacaoService:
    def __init__(self) :
        self.repositorio = usuario_repository()
        with open("appsentings.json", 'r') as config:
            self.config = json.load(config)['jtw_token'] 
            
            
    def gerar_token(self, usuario: str, senha: str):
        try:
            payload = {
                "usuario": usuario,
                "exp": datetime.utcnow() + timedelta(hours=self.config["expira_token"])
            }
            encoded_jwt = jwt.encode(payload, self.config['secret_key'], algorithm=self.config['algoritimo'])
            return encoded_jwt
        except Exception as ex:
            print(ex)
            return None