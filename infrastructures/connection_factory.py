
import sqlalchemy
import sys
import json
class conection_factory:
    
    def __init__(self, database_json):
        self.host = database_json['host']
        self.database = database_json['data_base']
        self.user = database_json['user']
        self.password = database_json['password']
    
    def conexao(self):
        engine = sqlalchemy.create_engine(f'postgresql://{self.user}:{self.password}@{self.host}/{self.database}')
        Session = sqlalchemy.orm.sessionmaker(bind=engine)
        return Session()
    
    def consulta_personalizada(self, sql:str, campos):
        try:
            #corrigir no futuro
            _conexao = self.conexao()
            retorno = _conexao.execute(sqlalchemy.sql.text(sql))
            _conexao.close()
            resultado_em_dicionarios = []
            linha_em_dicionario = []
            for row in retorno:
                for campo in range(len(campos)):
                    coluna = {campos[campo] : row[campo]}
                    linha_em_dicionario.append(coluna)
                resultado_em_dicionarios.append(json.dumps(linha_em_dicionario))
        except Exception as ex :
            print(ex)

        return resultado_em_dicionarios
    
        
        
        