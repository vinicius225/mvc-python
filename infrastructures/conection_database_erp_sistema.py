from infrastructures.connection_factory import conection_factory
import json
class conection_database_SQL:
    def __init__(self):
        with open("appsentings.json", 'r') as config:
            self.config = json.load(config) 
    def conexao(self):
        return conection_factory(self.config['database_postgres']).conexao()
    def consulta_personalizada(self, sql:str, campos):
        return conection_factory(self.config['database_postgres']).consulta_personalizada(sql,campos)
        
        