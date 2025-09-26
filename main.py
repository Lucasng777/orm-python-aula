from mysql.connector import (connection)
from mysql.connector import errorcode
import os
from dotenv import load_dotenv

load_dotenv()
senha= os.getenv('SENHA_SQL')
try:
    bd_conexao = connection.MySQLConnection(
    host='localhost',
    user='root',
    password= senha,
    database='bd_python'
    )
    print("conexão bem sucedida!")
except mysql.connector.error as erro:
    if erro.errno == errocode.ER_BAD_DB_ERROR:
        print("o banco de dados nao existe!")
    elif erro.errno == errocode.ER_ACCESS_DENIED_ERROR:
        print("Usuario ou senha incorretos!")
    else:
        print(erro)        
comando = bd_conexao.cursor()
select = comando.execute("SELECT * FROM ALUNOS")  
resultado = comando.fetchall()      
for linha in resultado:
    print(linha)

sql_insert = "INSERT INTO ALUNOS (nome, ano) VALUES (%s , %s) "
valores1 = ('caio','3 TEC')
valores2 = ('leonardo','2 TEC')

comando.execute(sql_insert, valores1)
comando.execute(sql_insert, valores2)
print("\n==TESTE INSERT==\n")
select = comando.execute("SELECT * FROM ALUNOS")  
resultado = comando.fetchall()      
for linha in resultado:
    print(linha)

    
comando.close()
bd_conexao.commit()
bd_conexao.close()