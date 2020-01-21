import MySQLdb
import MySQLdb.cursors
from contextlib import closing 

dados = {'host': "mysql.topskills.study", 'database':"topskills01", 'user': "topskills01", 'passwd':"ts2019"}

with closing(MySQLdb.connect(**dados)) as conn:
    cursor = conn.cursor
    cursor.execute ('SELECT * FROM abioluz')
    dicionario = cursor.fetchall()
    lista = []
    cabecalho = ['id', 'nome', 'idade']
    for i in dicionario:
        dic = dict(zip(cabecalho,i))
        lista.append(dic)
print(lista)        

with closing(MySQLdb.connect(**dados)) as conn:
    cursor = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM abioluz')
    dicionario = cursor.fetchall()
    for i in dicionario:
        print(i)



