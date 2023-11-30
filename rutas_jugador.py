from flask import render_template, request, redirect, Blueprint
from bd import conn, bd

rutas = Blueprint('jugador', __name__)


class Jugador:
    def __init__(self, id, nombres, apellidos, nacimiento):
        self.id = id
        self.nombres = nombres
        self.apellidos = apellidos
        self.nacimiento = nacimiento

@rutas.route('/ver/<int:id>')  
def ver(id):
    bd.execute(f"SELECT * FROM jugador WHERE id={id}")
    fila = bd.fetchone()
    objugador = Jugador(id= fila[0], nombres=fila[1], apellidos=fila[2], nacimiento= fila[3])
    return render_template("jugador/ver.html",objugador=objugador)
    

@rutas.route('/eliminar/<int:id>')  #define la ruta
def eliminar(id): #una funcion que toma como argumento id
    bd.execute(f"DELETE FROM jugador WHERE id={id}")
    conn.commit() 
    return redirect('/jugador')


@rutas.route('/agregar', methods=['GET', 'POST']) #POST se utilizan para enviar datos al servidor despues de dar clic en el boton de agregar
def agregar():
    if request.method == 'POST': # se ejecuta cuando se le da clic al boton guardar
        id = request.form['id']  
        nombres = request.form['nombres']
        apellidos = request.form['apellidos']
        nacim =request.form['nacim']

        bd.execute(f"INSERT INTO jugador VALUES({id}, '{nombres}', '{apellidos}', '{nacim}')")
        conn.commit() # manda la orden a msql para guardar el nuevo dato

        return redirect(f"/jugador")
    else: # Cuando se llama por primera vez
        return render_template('jugador/agregar.html')
    

@rutas.route('/editar/<int:id>', methods=['GET', 'POST'])    
def editar(id):
    if request.method == 'POST':
        id = request.form['id']  
        nombres = request.form['nombres']
        apellidos = request.form['apellidos']
        nacim =request.form['nacim']

        bd.execute(f"UPDATE jugador SET id={id}, nombres='{nombres}', apellidos='{apellidos}', nacim='{nacim}' WHERE id={id}")
        conn.commit() # manda la orden a msql para guardar el nuevo dato

        return redirect(f"/jugador")
    else:
        bd.execute(f"SELECT * FROM jugador WHERE id={id}")
        fila = bd.fetchone()
        objugador = Jugador(id = fila[0], nombres=fila[1], apellidos=fila[2], nacimiento= fila[3])
        return render_template("jugador/editar.html",objugador=objugador)


@rutas.route('/')  #define la ruta
def listar(): #una funcion que toma como argumento id
    bd.execute(f"SELECT * FROM jugador") #se hace una consulta a mysql de todos los datos de jugador
    filas = bd.fetchall()  #  esta obtiene todas la filas de la consulta y las guarda en filas
    jugadores =[] #donde se guarda todos los objetos Jugador
    for fila in filas: # recorre cada fila de cada jugador
        objetojugador = Jugador(id = fila[0], nombres=fila[1], apellidos=fila[2], nacimiento=fila[3]) #por cada interacc se crea un nuevo jugador como esta ubicado en la tabla jugador de la base de datos
        jugadores.append(objetojugador) #esto agrega el nuevo jugador = que push

    return render_template("jugador/listar.html",jugadores = jugadores) # muestra la lista de jugadores en la utilizando listar.html
    