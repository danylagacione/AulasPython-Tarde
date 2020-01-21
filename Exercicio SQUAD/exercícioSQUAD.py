# Definição de Squads

# No contexto corporativo, squad é um modelo organizacional que consiste em dividir a equipe da empresa em pequenos times multidisciplinares.
# Na HBSIS todas as equipes de produto são divididas em squads e possuem um stack padrão que envolve linguagem de programação backend, 
# framework frontend e banco de dados. 
# Recentemente foram contratados três novos programadores para compor as squads. Será preciso enviar cada novo 
# programador para uma Squad de acordo com suas habilidades. 
# Hoje são utilizados três bancos de dados no ambiente HBSIS, o MsSqlServer, PostgreSQL e o MongoDb.
# As equipes que atualmente possuem vagas em aberto utilizam como linguagem de backend,  Python, Java e PHP. 
# Como framework de frontend estão sendo utilizados o React, Angular e Vue. 
# Existem várias squads que utilizam a mesma linguagem de backend porém utilizam banco de dados e framework frontend distintos. 
# Os três programadores que foram contratados são; Mateus, Tiago e a Carol. 
# Cada um dos programadores possui conhecimento em um banco de dados, uma linguagem de backend e um framework frontend.
# Foi realizada uma avaliação com cada um dos programadores e estipulado algumas regras para inseri-los nas squads. 
# O programador que trabalha com Java também conhece PostgreSql. 
# O framework de frontend de Carol não é VUE. O programador que usa Angular trabalha com MongoDb. 
# Mateus é especialista Python e não conhece MySqlServer. Tiago não sabe PHP. 

# Crie um sistema que realize a validação da regras estipuladas e apenas permita que um programador seja 
# inserido em uma squad se estiver de acordo com seus conhecimentos de linguagem, framework e banco de dados.
# Usando as estruturas( Lista, Tuplas, Dicionários), Metodos
# Deve ser feito apenas no console - Usar esquema de cores.

# angular tbm trabalha com MongoDb

# 3 squads
# 3 banco de dados- MsSqlServer, PostgreSQL e o MongoDb.
# 3 linguagens -  Python, Java e PHP.
# 3 frameworks - React, Angular e Vue

# Mateus - Python e MongoDb e angular
# Tiago - java tbm conhece o PostgreSQL - vue
# Carol- PHP - Mysql - react e não é o  vue 

# dicionario nome a linguagem

pessoas = ['carol', 'tiago', 'mateus']
listaBD = ['sql', 'postegree', 'mongo']
lista_linguagem = ['php', 'java', 'python']
lista_framework = ['react', 'vue', 'angular']

tupla_dados = ('nome','l_backend', 'banco_dados', 'framework')
lista_dicio  = []

k = 0
for i in range(1,4):
    dicio = {tupla_dados[0]:pessoas[k], tupla_dados[1]: listaBD[k], 
            tupla_dados[2]:lista_linguagem[k], tupla_dados[3]:lista_framework[k] }
    lista_dicio.append(dicio)
    k = k + 1
print(lista_dicio)

