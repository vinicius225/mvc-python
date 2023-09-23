
import psycopg2

class conection_factory:
    
    def __init__(self, database_json):
        self.host = database_json['host']
        self.database = database_json['data_base']
        self.user = database_json['user']
        self.password = database_json['password']
    
    def conexao(self):
        return psycopg2.connect(
        host=self.host,
        database=self.database,
        user=self.user,
        password=self.password
    )
        
        
        