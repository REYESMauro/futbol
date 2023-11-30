from flask import render_template, request, redirect, Blueprint
from bd import conn, bd

rutas = Blueprint('equipo', __name__)


class Equipo:
    def __init__(self, id, nombre, lugar, delegado):
        self.id = id
        self.nombre = nombre
        self.lugar = lugar
        self.delegado = delegado


@rutas.route('/ver/<int:id>')  
def ver(id):
    bd.execute(f"SELECT * FROM equipo WHERE id_equipo={id}")
    fila = bd.fetchone()
    objequipo = Equipo(id= fila[0], nombre=fila[1], lugar=fila[2], delegado= fila[3])
    return render_template("equipo/ver.html",objequipo=objequipo)
    

@rutas.route('/eliminar/<int:id>')  #define la ruta
def eliminar(id): #una funcion que toma como argumento id
    bd.execute(f"DELETE FROM equipo WHERE id_equipo={id}")
    conn.commit() 
    return redirect('/equipo')


@rutas.route('/agregar', methods=['GET', 'POST']) #POST se utilizan para enviar datos al servidor despues de dar clic en el boton de agregar
def agregar():
    if request.method == 'POST': # se ejecuta cuando se le da clic al boton guardar
        id_equipo = request.form['id']  
        nombre = request.form['nombre']
        lugar = request.form['lugar']
        deleg=request.form['deleg']

        bd.execute(f"INSERT INTO equipo VALUES({id_equipo}, '{nombre}', '{lugar}', '{deleg}')")
        conn.commit() # manda la orden a msql para guardar el nuevo dato

        return redirect(f"/equipo")
    else: # Cuando se llama por primera vez
        return render_template('equipo/agregar.html')
    

@rutas.route('/editar/<int:id>', methods=['GET', 'POST'])    
def editar(id):
    if request.method == 'POST':
        id_equipo = request.form['id']  
        nombre = request.form['nombre']
        lugar = request.form['lugar']
        deleg =request.form['deleg']

        bd.execute(f"UPDATE equipo SET id_equipo={id}, nombre='{nombre}', lugar='{lugar}', deleg='{deleg}' WHERE id_equipo={id}")
        conn.commit() # manda la orden a msql para guardar el nuevo dato

        return redirect(f"/equipo")
    else:
        bd.execute(f"SELECT * FROM equipo WHERE id_equipo={id}")
        fila = bd.fetchone()
        objequipo = Equipo(id = fila[0], nombre=fila[1], lugar=fila[2], delegado= fila[3])
        return render_template("equipo/editar.html",objequipo=objequipo)


@rutas.route('/')  #define la ruta
def listar(): #una funcion que toma como argumento id
    bd.execute(f"SELECT * FROM equipo") #se hace una consulta a mysql de todos los datos de Equipo
    filas = bd.fetchall()  #  esta obtiene todas la filas de la consulta y las guarda en filas
    equipos =[] #donde se guarda todos los objetos Equipo
    for fila in filas: # recorre cada fila de cada Equipo
        objetoequipo = Equipo(id = fila[0], nombre=fila[1], lugar=fila[2], delegado=fila[3]) #por cada interacc se crea un nuevo Equipo como esta ubicado en la tabla jugador de la base de datos
        equipos.append(objetoequipo) #esto agrega el nuevo jugador = que push

    return render_template("equipo/listar.html",equipos = equipos) # muestra la lista de equipos en la utilizando listar.html
    