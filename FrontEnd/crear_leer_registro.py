from tkinter import *
from tkinter import ttk
import demo_database

print('data: ' + str(demo_database.data))

window = Tk()
frame_app = Frame(window, width=400, height=600, bg="red")
frame_app.pack()

my_table = ttk.Treeview(window)

# Define Our Columns 
my_table['columns'] = ('NOMBRE', 'EDAD', 'GENERO')

# Formate Our Columns
my_table.column('#0', width=120, minwidth=50)
my_table.column('NOMBRE', anchor=W, width=120)
my_table.column('EDAD', anchor=W, width=120)
my_table.column('GENERO', anchor=W, width=120)

# Create Headings
my_table.heading('#0', text='ID_CAMPO', anchor=W)
my_table.heading('NOMBRE', text='NOMBRE', anchor=W)
my_table.heading('EDAD', text='EDAD', anchor=W)
my_table.heading('GENERO', text='GENERO', anchor=W)

# Add Data

# registro = 0
# for fila in cursor:
#     registro = registro + 1 
#     print(str(registro) +" - "+ str(fila))
#     nombre = fila[0]  
#     edad = fila[1]
#     genero = fila[2]  
#     my_table.insert(parent='', index='end', iid=registro, text=str(registro), 
#         values=(nombre, edad, genero))


# Pack to the screen
my_table.pack(pady=20, padx=20)

# Inicializando las variables para almacenar lo que escriba el usuario en las cajas de Texto (Entry)
sala = StringVar()
butakas = StringVar()
boletos = StringVar()
precio = StringVar()

registro = "hola mundo"

    
def show_users():
    fila = 0 
    print(fila)
    print('data resultado: ' + str(demo_database.data))
    for user in demo_database.data:
        registro = user
        print('variable registro: ' + str(registro))
        title1 = Label(frame_title, 
              text=registro, 
              font=("Century Gothic", "22", "bold"),
              justify=LEFT)
        title1.place(x=25, y=10)
        #print(str(fila) + ' - ' + str(user))
        fila = fila + 1 

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
    demo_db.read_db()
    show_users()
    

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
              text=registro, 
              font=("Century Gothic", "22", "bold"),
              justify=LEFT)
title1.place(x=25, y=10)
title2 = Label(frame_title, 
              text="Todos los campos son obligartorios.", 
              font=("Century Gothic", "14"),
              justify=LEFT)
title2.place(x=25, y=50)

# Widgets dentro del contender OPTIONS
frame_form = Frame(frame_options, width=350, height=450, bg="yellow")
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