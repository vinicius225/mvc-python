import datetime
from Crosscutting.enums.status_enum import status

class perfil:
    def __init__(self):
        self.id : int
        self.nome: str
        self.status = status
        self.data_cadastro: datetime.date
        self.data_atualizacao: datetime.date
        