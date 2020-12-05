import sqlite3
tablilla = sqlite3.connect('basededatos.db')
cursero = tablilla.cursor()

cursero.execute('CREATE TABLE universidades(id INTEGER PRIMARY KEY AUTOINCREMENT, nombre VARCHAR(100), lugar VARCHAR(50), dorms VARCHAR(2), pinternacional VARCHAR(2), instalaciones VARCHAR(20), linkUni VARCHAR(255))')
tablilla.commit()