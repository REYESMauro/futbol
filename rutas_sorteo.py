from flask import render_template, request, redirect, Blueprint
from bd import conn, bd
import random

rutas = Blueprint('sorteo', __name__)

class Equipo:
    def __init__(self, id, nombre, lugar, delegado):
        self.id = id
        self.nombre = nombre
        self.lugar = lugar
        self.delegado = delegado

@rutas.route('/', methods=['GET', 'POST'])
def sorteo():
    bd.execute("SELECT * FROM equipo")
    filas = bd.fetchall()
    

    equipos = []
    for fila in filas:
        objetoequipo = Equipo(id=fila[0], nombre=fila[1], lugar=fila[2], delegado=fila[3])
        equipos.append(objetoequipo)     #agrega el objeto

    
    random.shuffle(equipos)             # Mezcla aleatoriamente los elementos en la lista y los reorganiza de manera aleatoria

    
    total_teams = len(equipos)          # Calcula la cantidad total de equipos en la lista y almacena ese valor en la variable 
    middle_index = total_teams // 2     # Calcula el índice que representa el punto medio de la lista de equipos.
    grupo1 = equipos[:middle_index]     # crea la lista de la mitad de los equipos segun el indice
    grupo2 = equipos[middle_index:]     # 

    return render_template("sorteo/resultado.html", grupo1=grupo1, grupo2=grupo2)