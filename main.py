from _mysql_connector import (connection)
from _mysql_connector import errocode
import os
from load_dotenv import load_dotenv
load_dotenv()
senha= os.getenv('SENHA_SQL')

bd_conexao = connection.MySQLConnection(
    host='localhost',
    user='root',
    password= senha,
    database='bd_python'
    
)