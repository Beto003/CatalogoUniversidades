from tkinter import *
from PIL import ImageTk,Image
import sqlite3

root = Tk()
root.title('Buscar Universidades')
root.iconbitmap('universidad.ico')
root.geometry("1000x1000")

imagen = PhotoImage(file="colegio.png")
chiquita = imagen.subsample(8, 8)

lupa = PhotoImage(file = "loupe.png")
lupita = lupa.subsample(10, 10)
label = Label(image= lupa)


# Frames General, Áreas y busqueda

filtros = LabelFrame(root, text = 'Filtros', pady = 15, width = 200, height = 580)
busqueda = LabelFrame(root, pady = 15, width = 1000, height = 100, background = '#54da99')
result = LabelFrame(root, width = 780, height = 580, background = '#ededed')
logo = Label(busqueda, image=chiquita, bd=0, background = '#54da99')

filtros.grid(row = 1, column = 0, padx = 10, pady = 10, columnspan = 2, sticky = W)
filtros.grid_propagate(0)
busqueda.grid(row = 0, column = 0, padx = 10, pady = 10, columnspan = 3, sticky = W)
busqueda.grid_propagate(0)
result.grid(row = 1, column = 1, padx = 10, pady = 10, columnspan = 3, sticky = W)
result.grid_propagate(0)
logo.grid(row =0, column = 0, padx = 10, rowspan = 2)
#GENERAL
def enable_disable(filtro):
  try:
    try:
      filtro.deselect()
    except:
      pass
    estado = str(filtro.button['state'])
    if estado == 'disabled':
      filtro.configure(state='normal')
    else:
      filtro.configure(state='disable')
  except: 
    try:
      filtro.deselect()
    except:
      if isinstance(filtro, Scale):
        empleabilidad.set(0)
        print(empleabilidad.get())  
    estado = filtro.cget('state')
    if estado == 'disabled':
      filtro.configure(state='normal')
    else:
      filtro.configure(state='disable')
    
def disableChildren(parent):
  for child in parent.winfo_children():
      wtype = child.winfo_class()
      if wtype not in ('Frame','Labelframe', 'Checkbutton', 'Label'):
          child.configure(state='disable')
      else:
          disableChildren(child)

def deleteChildren(parent):
    for child in parent.winfo_children():
        child.destroy()

etBuscar_c = Label(busqueda, text = 'Carrera', background = '#54da99')
enBuscar_c = Entry(busqueda, width = 45)
etBuscar_c.grid(row = 1, column = 1, sticky ='NESW')
enBuscar_c.grid(row = 1, column = 2, padx = 15, pady = 10, sticky = 'NESW')
etBuscar_c.config(font=("Sans-Serif",10))
enBuscar_c.config(font=("Sans-Serif",10))

etBuscar = Label(busqueda, text = 'Universidad', background = '#54da99')
enBuscar = Entry(busqueda, width = 45)
etBuscar.grid(row = 0, column = 1)
enBuscar.grid(row = 0, column = 2, padx = 15, pady = 5)
etBuscar.config(font=("Sans-Serif",10))
enBuscar.config(font=("Sans-Serif",10))

lugarChk = StringVar()
areasChk = StringVar()
dormitoriosChk = StringVar()
PIChk = StringVar()
instalacionesChk = StringVar()
costoChk = StringVar()
becaChk = StringVar()
ingresoChk = StringVar()
clickedChk = StringVar()
empleabilidadChk= StringVar()

areas = StringVar()
dormitorios = StringVar()
dormitorios.set('')
PI = StringVar()
instalaciones = StringVar()
instalaciones.set('')
costo = StringVar()
beca = StringVar()
beca.set('')
ingreso = StringVar()
ingreso.set('')
clicked = StringVar()
empleabilidad= StringVar()

list_areas = ['Medicina', 'Ciencias Aplicadas', 'Humanidades', 'Ciencias Teóricas', 'Ingeniería']

etLugar = Checkbutton(filtros, text = 'Lugar', variable = lugarChk, onvalue = 'Si', offvalue = 'No', command = lambda: enable_disable(enLugar))
etLugar.deselect()
enLugar = Entry(filtros, width = 20)
etLugar.grid(row = 18, column = 0, sticky = W, pady = 5, padx = 2)
enLugar.grid(row = 19, column = 0, sticky = W, padx = 4)

dropAreas = OptionMenu(filtros, clicked, *list_areas)
dropAreas.grid(row = 1, column = 0, columnspan = 2, sticky = W)
dropAreas.config(width=10)

a =Checkbutton(filtros, text="Áreas", variable=areasChk, onvalue='Si', offvalue='No', command= lambda: enable_disable(dropAreas))
a.deselect()
a.grid(row = 0, column = 0, sticky = W)

b =Checkbutton(filtros, text="Dormitorios", variable=dormitoriosChk, onvalue="Si", offvalue="No", command= lambda: [enable_disable(rPI_1), enable_disable(rPI_2)])
b.deselect()
b.grid(row =2, column = 0, sticky = W)
rPI_1 = Radiobutton(filtros, text = 'Sí', variable = PI, value = 1)
rPI_2 = Radiobutton(filtros, text = 'No', variable = PI, value = 0)
rPI_1.grid(row = 3, column = 0, sticky = W)
rPI_2.grid(row = 3, column = 0, padx = 55, sticky = W)

c =Checkbutton(filtros, text="Programas Internacionales", variable=PIChk, onvalue="Si", offvalue="No", command= lambda: [enable_disable(rDorms_1), enable_disable(rDorms_2)])
c.deselect()
c.grid(row =4, column = 0, sticky = W)
rDorms_1 = Radiobutton(filtros, text = 'Sí', variable = dormitorios, value = 1)
rDorms_2 = Radiobutton(filtros, text = 'No', variable = dormitorios, value = 0)
rDorms_1.grid(row = 5, column = 0, sticky = W)
rDorms_2.grid(row = 5, column = 0, padx = 55, sticky = W)

d =Checkbutton(filtros, text="Nivel de nstalaciones", variable=instalacionesChk, onvalue="Si", offvalue="No", command= lambda: [enable_disable(rInstal_1), enable_disable(rInstal_2), enable_disable(rInstal_3)])
d.deselect()
d.grid(row =6, column = 0, sticky = W)
rInstal_1 = Radiobutton(filtros, text = 'Bajo', variable = instalaciones, value = 0)
rInstal_2 = Radiobutton(filtros, text = 'Medio', variable = instalaciones, value = 1)
rInstal_3 = Radiobutton(filtros, text = 'Alto', variable = instalaciones, value = 2)
rInstal_1.grid(row = 7, column = 0, sticky = W)
rInstal_2.grid(row = 7, column = 0, padx = 55, sticky = W)
rInstal_3.grid(row = 7, column = 0, padx = 115, sticky = W)

e =Checkbutton(filtros, text="Costo aproximado", variable=costoChk, onvalue="Si", offvalue="No", command = lambda: [enable_disable(costo_en), enable_disable(tolerancia_en)])
e.deselect()
e.grid(row =8, column = 0, sticky = W)
costo_en = Entry(filtros, width = 10)
tolerancia = Label(filtros, text = 'Tolerancia +/-')
tolerancia_en = Entry(filtros, width = 10)
costo_en.grid(row = 9, column = 0, sticky = W)
tolerancia.grid(row = 10, column = 0, sticky = W)
tolerancia_en.grid(row = 10, column = 0, padx = 80, sticky = W)

f =Checkbutton(filtros, text="No. de becas ofrecidas", variable=becaChk, onvalue="Si", offvalue="No", command = lambda: [enable_disable(rBeca_1), enable_disable(rBeca_2), enable_disable(rBeca_3)])
f.deselect()
f.grid(row =11, column = 0, sticky = W)
rBeca_1 = Radiobutton(filtros, text = 'Bajo', variable = beca, value = 0)
rBeca_2 = Radiobutton(filtros, text = 'Medio', variable = beca, value = 1)
rBeca_3 = Radiobutton(filtros, text = 'Alto', variable = beca, value = 2)
rBeca_1.grid(row = 12, column = 0, padx = 15, sticky = W)
rBeca_2.grid(row = 12, column = 0, padx = 70, sticky = W)
rBeca_3.grid(row = 12, column = 0, padx = 130, sticky = W)

g =Checkbutton(filtros, text="Dificultad de ingreso", variable=ingresoChk, onvalue="Si", offvalue="No", command = lambda: [enable_disable(rIngreso_1), enable_disable(rIngreso_2), enable_disable(rIngreso_3)])
g.deselect()
g.grid(row =13, column = 0, sticky = W)
rIngreso_1 = Radiobutton(filtros, text = 'Baja', variable = ingreso, value = 0)
rIngreso_2 = Radiobutton(filtros, text = 'Media', variable = ingreso, value = 1)
rIngreso_3 = Radiobutton(filtros, text = 'Alta', variable = ingreso, value = 2)
rIngreso_1.grid(row = 14, column = 0, sticky = W)
rIngreso_2.grid(row = 14, column = 0, padx = 55, sticky = W)
rIngreso_3.grid(row = 14, column = 0, padx = 115, sticky = W)

h = Checkbutton(filtros, text='Empleabilida del \negresado (%)', variable=empleabilidadChk, onvalue="Si", offvalue="No", command = lambda: [enable_disable(empleabilidad), enable_disable(toleranciaSc_en)])
empleabilidad = Scale(filtros, from_=0, to=100, length = 150, orient=HORIZONTAL)

h.deselect()
h.grid(row = 15, column = 0, sticky = W)
empleabilidad.grid(row = 16, column = 0, columnspan = 1, sticky = W)
toleranciaSc = Label(filtros, text = 'Tolerancia +/-')
toleranciaSc_en = Entry(filtros, width = 10)
toleranciaSc.grid(row = 17, column = 0, sticky = W)
toleranciaSc_en.grid(row = 17, column = 0, padx = 80, sticky = W)

#SQL
datos=[]
generales=[]
m=[]

posbeca = StringVar()
posingreso = StringVar()

'''
canvas.place(relx=0, rely=0, relheight=1, relwidth=1)
scrollbar.place(relx=1, rely=0, relheight=1, anchor='ne')
container.grid(row = 1, column = 2, padx = 10, pady = 10, columnspan = 3, sticky = W)
'''


def buscar():
  global generales, datos, beca, dormitorios, instalaciones, ingreso, m, canvas, scrollbar, posbeca
  tablilla = sqlite3.connect('basededatos.db')
  cursero = tablilla.cursor()

  datos = []
  generales = []
  m = []
  
  deleteChildren(result)
    
  name=enBuscar.get()
  place=enLugar.get()
  are=clicked.get()
  career=enBuscar_c.get()
  cost=str(costo_en.get())
  margen=str(tolerancia_en.get())
  scholarship=str(beca.get())
  dormas=str(PI.get())
  international=str(dormitorios.get())
  employability=str(empleabilidad.get())
  margen_emp=str(toleranciaSc_en.get())
  instalations=str(instalaciones.get())
  requisites=str(ingreso.get())

  
  if cost=='':
      cost='0'
  if margen=='':
      margen='0'
  if employability=='':
      employability='0'
  if margen_emp=='':
      margen_emp='0'
  
  x='SELECT * FROM universidades WHERE nombre LIKE {nombre} AND lugar LIKE {lugar} AND dorms LIKE {dorms} AND pinternacional LIKE {pinternacional} AND instalaciones LIKE {instalaciones}'.format(nombre='"' + name + '%"', lugar='"' + place + '%"', dorms='"'+dormas+'%"', pinternacional='"'+international+'%"', instalaciones='"'+instalations+'%"')
  cursero.execute(x)
  generales.append(cursero.fetchall())
  x='SELECT nombre FROM universidades WHERE nombre LIKE {nombre} AND lugar LIKE {lugar} AND dorms LIKE {dorms} AND pinternacional LIKE {pinternacional} AND instalaciones LIKE {instalaciones}'.format(nombre='"' + name + '%"', lugar='"' + place + '%"', dorms='"'+dormas+'%"', pinternacional='"'+international+'%"', instalaciones='"'+instalations+'%"')
  cursero.execute(x)
  nombreLugar=cursero.fetchall()

  for i in range(len(nombreLugar)):
      p='SELECT * FROM {nombre} WHERE carrera LIKE {carrera} AND (costo BETWEEN {costo_inicial} AND {costo_final} OR {costo} = "0") AND beca LIKE {beca} AND (empleabilidad BETWEEN {emp_inicial} AND {emp_final} OR {empleabilidad} = "0") AND requisitos LIKE {requisitos} AND area LIKE {area}'.format(nombre=nombreLugar[i][0], carrera='"'+career+'%"', costo='"'+cost+'"', costo_inicial=int(cost)-int(margen)/2, costo_final=int(cost)+int(margen)/2, beca='"'+scholarship+'%"', empleabilidad='"'+employability+'"', emp_inicial=int(employability)-int(margen_emp)/2, emp_final=int(employability)+int(margen_emp)/2, requisitos='"'+requisites+'%"', area='"'+are+'%"')
      cursero.execute(p)
      datos.append(cursero.fetchall())
      if len(datos[i])!=0:
          m.append(i)

  #Mostrar resultados          
  if len(m)!=0:
    r = 0
    for x in m:
        etUniversidad = str(x+1)+'.  '+ str(generales[0][x][1])
        if generales[0][x][3] == '0':
          si_no_dorms = 'Sin dormitorios'
        elif generales[0][x][3] == '1':
          si_no_dorms = 'Con dormitorios'

        if generales[0][x][5] == '0':
          nivel_instal = 'Nivel instalaciones: Bajo'
        elif generales[0][x][5] == '1':
          nivel_instal = 'Nivel instalaciones: Medio'
        elif generales[0][x][5]== '2':
          nivel_instal = 'Nivel instalaciones: Alto'

        if generales[0][x][4] == '0':
          si_no_pi = 'Progr. Intl.: No'
        elif generales[0][x][4] == '1':
          si_no_pi = 'Progr. Intl.: Sí'

        universidad1 = Label(result, text = etUniversidad)
        lugar1 = Label(result, text = generales[0][x][2])
        dormitorios1 = Label(result, text = si_no_dorms)
        pi1 = Label(result, text = si_no_pi)
        instalaciones1 = Label(result, text = nivel_instal)

        universidad1.place(relx = 0, y = 20+r)
        lugar1.place(relx = 0.175, y = 20+r)
        dormitorios1.place(relx = 0.35, y = 20+r)
        pi1.place(relx = 0.525, y = 20+r)
        instalaciones1.place(relx = 0.70, y = 20+r)

        carreras = Label(result, text = 'Carrera')
        precio = Label(result, text = 'Costo')
        no_becas = Label(result, text = 'No. de becas')
        empleabil = Label(result, text = 'Empleabilidad (%)')
        dif_ingreso = Label(result, text = 'Dificultad ingreso')

        carreras.place(relx = 0, y = r+40)
        precio.place(relx = 0.175, y = r+40)
        no_becas.place(relx = 0.35, y = r+40)
        empleabil.place(relx = 0.525, y = r+40)
        dif_ingreso.place(relx = 0.7, y = r+40)

        for i in range(len(datos[x])):
          if datos[x][i][4] == '0':
            posbeca = 'Baja'
          elif datos[x][i][4] == '1':
            posbeca = 'Media'
          elif datos[x][i][4] == '2':
            posbeca = 'Alta'

          if datos[x][i][5] == '0':
            posingreso = 'Baja'
          elif datos[x][i][5] == '1':
            posingreso = 'Media'
          elif datos[x][i][5] == '2':
            posingreso = 'Alta'

          carrera1 = Label(result, text = datos[x][i][2])
          costo1 = Label(result, text = datos[x][i][3])
          beca1 = Label(result, text = str(posbeca))
          empl1 = Label(result, text = datos[x][i][6])
          ingreso1 = Label(result, text = str(posingreso))
          carrera1.place(relx = 0, y = 20*i+60+r)
          costo1.place(relx = 0.175, y = 20*i+60+r)
          beca1.place(relx = 0.35, y = 20*i+60+r)
          empl1.place(relx = 0.525, y = 20*i+60+r)
          ingreso1.place(relx = 0.7, y = 20*i+60+r)

        r+=150
  else:
    nel= Label(result, text='Lo sentimos, pero nuestra base de datos no cuenta con una\n Universidad con las caraterísticas que buscaste.')
    nel.place(x = 250, y = 265, anchor = 'center')

#Fin SQL

fin = Button(busqueda, text = 'Buscar', image=lupita, command = buscar, background = '#54da99')
fin.grid(row = 0, column = 5, rowspan = 2)

disableChildren(filtros)

filtros.mainloop()
