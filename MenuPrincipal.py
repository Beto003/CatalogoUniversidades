import sys
import os
from tkinter import *
from PIL import ImageTk,Image
import sqlite3

root = Tk()
root.title('UNISEARCH')
root.iconbitmap('universidad.ico')
root.geometry("400x330")

def anadir():
	os.system('Añadir.py')
def busqueda():
	os.system('Buscar.py')

imagen = PhotoImage(file="colegio.png")
chiquita = imagen.subsample(7, 7)

unisearch = Label(root, text = '¡Bienvenido a UniSearch!')
unisearch.pack(pady =5)
unisearch.config(font=("Sans-Serif",25), padx=15, pady=15)
imagen_et = Label(root, image=chiquita, bd=0).pack(pady = 5)
selecciona = Label(root, text = 'Selecciona la acción que deseas realizar.')
selecciona.pack(pady = 5)
selecciona.config(font=("Sans-Serif",12), padx=15, pady=15)
a = Button(root, text = 'Añadir', command = anadir)
a.pack(pady = 5)
a.config(font=("Sans-Serif",12), padx=5, pady=5)
b = Button(root, text = 'Buscar', command = busqueda)
b.pack(pady = 5)
b.config(font=("Sans-Serif",12), padx=5, pady=5)
root.mainloop()