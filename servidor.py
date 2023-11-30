from flask import Flask
from rutas_jugador import rutas as r_jugador
from rutas_equipo import rutas as r_equipo
from rutas_sorteo import rutas as r_sorteo



app = Flask("futbol")
app.register_blueprint(r_equipo, url_prefix='/equipo')
app.register_blueprint(r_jugador, url_prefix='/jugador')
app.register_blueprint(r_sorteo, url_prefix='/sorteo')




if __name__ == '__main__':   #comprueva si el archivo se ejecuta como el programa principal
    app.run(debug=True) #permite que la aplicación se ejecute en modo de depuración "informacion de lo que pasa internamente"