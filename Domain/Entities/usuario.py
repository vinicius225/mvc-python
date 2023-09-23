import datetime
from Domain.Entities.perfil import perfil
from Crosscutting.enums.status_enum import status


class usuario:
    def __init__(self):
        self.id : int
        self.nome : str
        self.email : str
        self.telefone : str
        self.senha : str
        self.id_perfil : int
        self.perfil : perfil
        self.status : status
        self.data_nascimento : datetime.date
        self.data_cadastro: datetime.date
        self.data_atualizacao: datetime.date
        