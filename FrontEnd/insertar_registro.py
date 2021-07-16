from tkinter import *
from tkinter import ttk
import demo_database

window = Tk()
frame_app = Frame(window, width=400, height=600, bg="red")
frame_app.pack()

# Inicializando las variables para almacenar lo que escriba el usuario en las cajas de Texto (Entry)
sala = StringVar()
butakas = StringVar()
boletos = StringVar()
precio = StringVar()

# Creando función "agregar_sala()", función que se ejecuta la dar clic en el botón "Agregar"
def crear_sala():
    # Obteniendo los valores de los widgets Entry mediante la función "GET()" 
    # y almacenandolos en las variables previamente inicializadas
    nombre = entry_sala.get()
    edad = entry_butakas.get()
    genero = entry_boletos.get()
  
    # creando un objeto de la Base de datos "MyDatabase", para acceder a la función "insert_db"
    demo_db = demo_database.MyDatabase()
    # ejecutando la función "insert_db" y enviando las variables como parámetros
    demo_db.insert_db(nombre, edad, genero)

# Widgets dentro del contender APP
frame_navbar = Frame(frame_app, width=400, height=100)
frame_navbar.grid(row=0, column=0)
frame_title = Frame(frame_app, width=400, height=120)
frame_title.grid(row=1, column=0)
frame_options = Frame(frame_app, width=400, height=500)
frame_options.grid(row=2, column=0)

# Widgets dentro del contender NAVBAR
title = Label(frame_navbar, 
              text="CINE LOVE",
              font=("Century Gothic", "14"))
title.place(x=250, y=40)

# Widgets dentro del contender TITLE
title1 = Label(frame_title, 
              text="SALAS DE CINE", 
              font=("Century Gothic", "22", "bold"),
              justify=LEFT)
title1.place(x=25, y=10)
title2 = Label(frame_title, 
              text="Todos los campos son obligartorios.", 
              font=("Century Gothic", "14"),
              justify=LEFT)
title2.place(x=25, y=50)

# Widgets dentro del contender OPTIONS
frame_form = Frame(frame_options, width=350, height=450, bg="#d48df0")
frame_form.place(x=25, y=5)
label_sala = Label(frame_form, 
              text="Nombre:",
              font=("Century Gothic", "20", "bold"),
              fg="white",
              bg="#d48df0")
label_sala.place(x=30, y=30)
entry_sala = Entry(frame_form, justify=LEFT, width=25, 
             font=("Century Gothic", "14"))
entry_sala.place(x=30, y=70)

label_butakas = Label(frame_form, 
              text="Edad:",
              font=("Century Gothic", "20", "bold"),
              fg="white",
              bg="#d48df0")
label_butakas.place(x=30, y=100)
entry_butakas = Entry(frame_form, justify=LEFT, width=25, 
                font=("Century Gothic", "14"))
entry_butakas.place(x=30, y=140)

label_boletos = Label(frame_form, 
              text="Género:",
              font=("Century Gothic", "20", "bold"),
              fg="white",
              bg="#d48df0")
label_boletos.place(x=30, y=170)
entry_boletos = Entry(frame_form, justify=LEFT, width=25, 
                font=("Century Gothic", "14"))
entry_boletos.place(x=30, y=210)


button_agregar = Button(frame_form, text="Insertar usuario", 
                        font=("Century Gothic", "14", "bold"),
                        command=crear_sala)
button_agregar.place(x=110, y=350)

window.mainloop()