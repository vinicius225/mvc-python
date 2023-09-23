import datetime
from Domain.Entities.perfil import perfil
from Crosscutting.enums.status_enum import status
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy

Base = declarative_base()

class usuario(Base):
        __tablename__ = 'usuarios'
        id  = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
        nome = sqlalchemy.Column(sqlalchemy.String)
        email = sqlalchemy.Column(sqlalchemy.String)
        telefone = sqlalchemy.Column(sqlalchemy.String)
        senha = sqlalchemy.Column(sqlalchemy.String)
        #id_perfil : sqlalchemy.Column(sqlalchemy.Integer)
     #   perfil = sqlalchemy.orm.relationship(perfil, backref='usuarios')

        def status(cls):
            return sqlalchemy.Column(sqlalchemy.Enum(status))  
        data_nascimento = sqlalchemy.Column(sqlalchemy.Date)
        data_cadastro= sqlalchemy.Column(sqlalchemy.Date)
        data_atualizacao= sqlalchemy.Column(sqlalchemy.Date)
        