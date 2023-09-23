from infrastructures.conection_database_erp_sistema import conection_database_SQL
from  Domain.Entities.usuario import usuario
import pandas as pd

class usuario_repository:
    def __init__(self):
        self.conection_database_SQL = conection_database_SQL()
        
    def listar_usuarios(self):
        return self.conection_database_SQL.conexao().query(usuario).all()
        