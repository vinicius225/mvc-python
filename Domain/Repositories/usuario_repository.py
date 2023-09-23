from infrastructures.conection_database_erp_sistema import conection_database_SQL
import pandas as pd

class usuario_repository:
    def __init__(self):
        self.conexao = conection_database_SQL().conexao()
        
    def listar_usuarios(self):
        sql = """ select * from usuarios ;"""
        
        dataframe = pd.read_sql_query(sql, self.conexao).to_dict(orient='records')
        return dataframe
        
        