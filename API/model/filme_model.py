
import sys
sys.path.append(r'C:\Users\900134\Documents\AulasPython-Tarde\Virtual-Alchemy')

class Filmes:
    def __init__(self):
        self.id = 0
        self.nome = ''
        self.genero = ''
        self.ano_lancamento = ''
        self.editora = ''

    def __str__(self):
         return f'{self.id}; {self.nome}; {self.genero}; {self.ano_lancamento}; {self.editora}'