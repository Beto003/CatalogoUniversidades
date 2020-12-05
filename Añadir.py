from tkinter import *

import sqlite3

root = Tk()
root.title('Agregar Universidades')
root.iconbitmap('universidad.ico')
root.geometry("1000x1000")

instrucciones = Label(root, text = '1. Ingresa la información de la universidad en el recuadro "GENERAL"\
 y da click a "Enviar". \n2. Llena la información de cada carrera en el recuadro "CARRERAS" y da click en el boton "Enviar" para mandar cada una.\n \
3. Da click en "Finalizar" para terminar de agregar la universidad.')
instrucciones.pack()
instrucciones.config(font=("Sans-Serif",10), padx=15, pady=15)
#SQL

tablilla = sqlite3.connect('basededatos.db')
cursero = tablilla.cursor()

def enviar_uni():
    disableChildren(gral)
    try:
        x='CREATE TABLE {}(id INTEGER PRIMARY KEY AUTOINCREMENT, area VARCHAR(20), carrera VARCHAR(20), costo INTEGER, beca VARCHAR(20), requisitos VARCHAR(20), empleabilidad INTEGER, linkCarrera VARCHAR(255))'.format(enNombre.get())
        cursero.execute(x)
        t=(enNombre.get(), enLugar.get(), PI.get(), Dorms.get(), Instal.get(), enLink.get())
        cursero.execute('INSERT INTO universidades(nombre, lugar, dorms, pinternacional, instalaciones, linkUni) VALUES(?, ?, ?, ?, ?, ?)', t)
        tablilla.commit()
        enableChildren(areas)
    except:
        enableChildren(areas)

def enviar_carrera():
  x='INSERT INTO {}(area, carrera, costo, beca, requisitos, empleabilidad, linkCarrera) VALUES(?, ?, ?, ?, ?, ?, ?)'.format(enNombre.get())
  t=(clicked.get(), enCarrera.get(), enCosto.get(), Beca.get(), Ingreso.get(), slEmpl.get(), enLink_c.get())
  cursero.execute(x, t)
  tablilla.commit()
  deleteChildren(areas)

# Frames General, Áreas y Carreras
gral = LabelFrame(root, text = 'General', padx = 15, pady = 15, width = 200)
areas = LabelFrame(root, text = 'Carreras', padx = 15, pady = 15, width = 200)
carreras = LabelFrame(root, text = 'Carreras', padx = 15, pady = 15)

root.pack_propagate(0)

gral.pack(pady = 10)
gral.pack_propagate(0)
areas.pack(pady = 10)
areas.pack_propagate(0)
carreras.pack(pady = 10)

#GENERAL
def disableChildren(parent):
    for child in parent.winfo_children():
        wtype = child.winfo_class()
        if wtype not in ('Frame','Labelframe'):
            child.configure(state='disable')
        else:
            disableChildren(child)

def enableChildren(parent):
    for child in parent.winfo_children():
        wtype = child.winfo_class()
        print (wtype)
        if wtype not in ('Frame','Labelframe'):
            child.configure(state='normal')
        else:
            enableChildren(child) 

links_carreras = ['']
list_areas = ['Medicina', 'Ciencias Aplicadas', 'Humanidades', 'Ciencias Teóricas', 'Ingeniería']	#lista de áreas
PI = BooleanVar()
Dorms = BooleanVar()
Instal = IntVar()
Beca = IntVar()
Ingreso = IntVar()
list_extra = []	#lista de extracurriculares
carreras = StringVar()

def deleteChildren(parent):
    for child in parent.winfo_children():
        wtype = child.winfo_class()
        if wtype not in ('Frame','Labelframe', 'Label', 'Button', 'Radiobutton', 'Menubutton', 'Scale'):
            child.delete(0, END)
        elif wtype not in('Menubutton'):
            deleteChildren(child)

#Cargar lista a dropdown menu de areas
clicked = StringVar()
dropAreas = OptionMenu(areas, clicked, *list_areas)
dropAreas.grid(row = 0, column = 0, columnspan = 2, sticky = W)
dropAreas.config(width=10)

#Agregar institución (cajas de texto y entradas)
etNombre = Label(gral, text = 'Institución')
enNombre = Entry(gral, width = 45)
etNombre.grid(row = 0, column = 0, sticky = W)
enNombre.grid(row = 0, column = 1, padx = 15)

etLugar = Label(gral, text = 'Lugar')
enLugar = Entry(gral, width = 45)
etLugar.grid(row = 1, column = 0, sticky = W)
enLugar.grid(row = 1, column = 1, padx = 15)

etLink = Label(gral, text = 'Página oficial')
enLink = Entry(gral, width = 45)
etLink.grid(row = 8, column = 0, sticky = W)
enLink.grid(row = 8, column = 1, padx = 15)

etPI = Label(gral, text = 'Dormitorios.')
rPI_1 = Radiobutton(gral, text = 'Sí', variable = PI, value = 1)
rPI_2 = Radiobutton(gral, text = 'No', variable = PI, value = 0)
etPI.grid(row = 2, column = 0, sticky = W)
rPI_1.grid(row = 2, column = 1, padx = 15, sticky = W)
rPI_2.grid(row = 2, column = 1, padx = 70, sticky = W)

etDorms = Label(gral, text = 'Prog. Intl.')
rDorms_1 = Radiobutton(gral, text = 'Sí', variable = Dorms, value = 1)
rDorms_2 = Radiobutton(gral, text = 'No', variable = Dorms, value = 0)
etDorms.grid(row = 3, column = 0, sticky = W)
rDorms_1.grid(row = 3, column = 1, padx = 15, sticky = W)
rDorms_2.grid(row = 3, column = 1, padx = 70, sticky = W)

etInstal = Label(gral, text = 'Instalaciones')
rInstal_1 = Radiobutton(gral, text = 'Bajo', variable = Instal, value = 0)
rInstal_2 = Radiobutton(gral, text = 'Medio', variable = Instal, value = 1)
rInstal_3 = Radiobutton(gral, text = 'Alto', variable = Instal, value = 2)
etInstal.grid(row = 4, column = 0, sticky = W)
rInstal_1.grid(row = 4, column = 1, padx = 15, sticky = W)
rInstal_2.grid(row = 4, column = 1, padx = 70, sticky = W)
rInstal_3.grid(row = 4, column = 1, padx = 130, sticky = W)


#Crear botón enviar

enviar_gral = Button(gral, text = 'Enviar', command = enviar_uni)
enviar_gral.grid(row = 9, column = 2, columnspan = 2, pady = 10, padx = 10)

#ÁREAS

# Para obtener el valor del área seleccionada en el menu dropdown: 
#area = clicked.get() 

etCarrera = Label(areas, text = 'Carreras')
enCarrera = Entry(areas, width = 45)
etCarrera.grid(row = 1, column = 0, sticky = W)
enCarrera.grid(row = 1, column = 1, padx = 15)


etCosto = Label(areas, text = 'Costo')
enCosto = Entry(areas, width = 45)
etCosto.grid(row = 2, column = 0, sticky = W)
enCosto.grid(row = 2, column = 1, padx = 15)

etBeca = Label(areas, text = 'Beca')
rBeca_1 = Radiobutton(areas, text = 'Bajo', variable = Beca, value = 0)
rBeca_2 = Radiobutton(areas, text = 'Medio', variable = Beca, value = 1)
rBeca_3 = Radiobutton(areas, text = 'Alto', variable = Beca, value = 2)
etBeca.grid(row = 3, column = 0, sticky = W)
rBeca_1.grid(row = 3, column = 1, padx = 15, sticky = W)
rBeca_2.grid(row = 3, column = 1, padx = 70, sticky = W)
rBeca_3.grid(row = 3, column = 1, padx = 130, sticky = W)

etIngreso = Label(areas, text = 'Dificultad de Ingreso')
rIngreso_1 = Radiobutton(areas, text = 'Bajo', variable = Ingreso, value = 0)
rIngreso_2 = Radiobutton(areas, text = 'Medio', variable = Ingreso, value = 1)
rIngreso_3 = Radiobutton(areas, text = 'Alto', variable = Ingreso, value = 2)
etIngreso.grid(row = 4, column = 0, sticky = W)
rIngreso_1.grid(row = 4, column = 1, padx = 15, sticky = W)
rIngreso_2.grid(row = 4, column = 1, padx = 70, sticky = W)
rIngreso_3.grid(row = 4, column = 1, padx = 130, sticky = W)

etEmpl = Label(areas, text = 'Empleabilida del \negresado (%)')
slEmpl = Scale(areas, from_=0, to=100, length = 270, orient=HORIZONTAL)
etEmpl.grid(row = 5, column = 0, sticky = W)
slEmpl.grid(row = 5, column = 1, padx = 15, columnspan = 1)

etLink_c = Label(areas, text = 'Página carrera')
enLink_c = Entry(areas, width = 45)
etLink_c.grid(row = 6, column = 0, sticky = W)
enLink_c.grid(row = 6, column = 1, padx = 15)

enviar_area = Button(areas, text = 'Enviar', command = enviar_carrera)
enviar_area.grid(row = 7, column = 2, columnspan = 2, pady = 10, padx = 10)

finalizar = Button(root, text = 'Finalizar', command = lambda:[enableChildren(gral), deleteChildren(gral), disableChildren(areas)])
finalizar.pack(pady = 10)

disableChildren(areas)

root.mainloop()
