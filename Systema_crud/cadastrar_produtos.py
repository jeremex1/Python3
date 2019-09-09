import mysql.connector as connector
from sytema import Systema_cadastro
#from conexao_bd import *


class Cadastro_produtos():
    def __init__(self):
        self.teste = Systema_cadastro()
        print("%s",self.teste.get_nome())

Cadastro_produtos()