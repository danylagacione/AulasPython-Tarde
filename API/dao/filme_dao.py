# Conexão com banco de dados/ CRUD

import sys
sys.path.append(r'C:\Users\900134\Documents\AulasPython-Tarde\API')

import MySQLdb
from API.model.filme_model import Filmes

class FilmeDao:
    conexao = MySQLdb.connect(host= '127.0.01', database= 'phpmyadmin', user='root')
    cursor = conexao.cursor()

    def listar_movies(self):
        comando_sql = f"SELECT * FROM Filmes"
        self.cursor.execute(comando_sql)
        lista = self.cursor.fetchall()
        return lista

    def listar_id(self, id):
        comando_sql = f"SELECT * FROM Filmes WHERE ID = {id}"
        self.cursor.execute(comando_sql)
        id_selecionado = self.cursor.fetchone()
        return id_selecionado

    def adicionar (self, filme : Filmes):
        comando_sql = f""" INSERT INTO Filmes
        ( 
            nome,
            genero,
            ano_lancamento,
            editora
        )
        VALUES
        (
            '{filme.nome}',
            '{filme.genero}',
            '{filme.ano_lancamento}',
            '{filme.editora}'
        )"""
        self.cursor.execute(comando_sql)
        self.conexao.commit()
        filme_add = self.cursor.lastrowid
        return filme_add

