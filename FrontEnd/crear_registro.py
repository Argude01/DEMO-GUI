from tkinter import *
from tkinter import ttk 

window = Tk()
window.title('Crear Registro')

# Inicializando las variables para almacenar lo que escriba el usuario en las cajas de Texto (Entry)
id_campo = StringVar()
campo1 = StringVar()
campo2 = StringVar()
campo3 = StringVar()

# Creando función "agregar_sala()", función que se ejecuta la dar clic en el botón "Agregar"
def crear_sala():
    # Obteniendo los valores de los widgets Entry mediante la función "GET()" 
    # y almacenandolos en las variables previamente inicializadas
    sala = entry_sala.get()
    butakas = entry_butakas.get()
    boletos = entry_boletos.get()
    precio = entry_precio.get()
    # creando un objeto de la Base de datos "MyDatabase", para acceder a la función "insert_db"
    cine_db = cine_database.MyDatabase()
    # ejecutando la función "insert_db" y enviando las variables como parámetros
    cine_db.insert_db(sala, butakas, boletos, precio)

my_table = ttk.Treeview(window)

# Define Our Columns 
my_table['columns'] = ('CAMPO1', 'CAMPO2', 'CAMPO3')

# Formate Our Columns
my_table.column('#0', width=120, minwidth=50)
my_table.column('CAMPO1', anchor=W, width=120)
my_table.column('CAMPO2', anchor=W, width=120)
my_table.column('CAMPO3', anchor=W, width=120)

# Create Headings
my_table.heading('#0', text='ID_CAMPO', anchor=W)
my_table.heading('CAMPO1', text='CAMPO1', anchor=W)
my_table.heading('CAMPO2', text='CAMPO2', anchor=W)
my_table.heading('CAMPO3', text='CAMPO3', anchor=W)

# Add Data
my_table.insert(parent='', index='end', iid=0, text='1', 
        values=('Value 1', 'Value 2', 'Value 3'))
my_table.insert(parent='', index='end', iid=1, text='2', 
        values=('Value 1', 'Value 2', 'Value 3')) 
my_table.insert(parent='', index='end', iid=3, text='3', 
        values=('Value 1', 'Value 2', 'Value 3'))
my_table.insert(parent='', index='end', iid=4, text='4', 
        values=('Value 1', 'Value 2', 'Value 3'))           

# Pack to the screen
my_table.pack(pady=20, padx=20)

window.mainloop()