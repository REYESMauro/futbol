import mysql.connector

conn = mysql.connector.connect(user='root', password='1234', host='127.0.0.1', database='futbol')
bd = conn.cursor() # se utiliza para ejecutar consultas de mysql