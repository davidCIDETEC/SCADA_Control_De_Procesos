import mysql.connector
import time
x = 3

cnx = mysql.connector.connect(user ='paul' , password = 'Tec2062923', host = '172.17.0.1',database ='Prueba_BASE_DE_DATOSb') #original  host = '127.0.0.1'
cursor = cnx.cursor()
cursor.execute(f"SELECT * FROM sistemas_control WHERE id = {x};")
valor = cursor.fetchone()
cnx.commit()
cursor.close()

print(valor[1])