from tkinter import *
from tkinter import ttk 

import mysql.connector

connection =mysql.connector.connect(host="localhost", 
                                  user="root", 
                                  passwd="", 
                                  database="db_demo")

window = Tk()
window.title('Mostrar Registros')

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
cursor = connection.cursor()
cursor.execute("SELECT NOMBRE, EDAD, GENERO FROM TBL_USUARIOS")
registro = 0
for fila in cursor:
    registro = registro + 1 
    print(str(registro) +" - "+ str(fila))
    nombre = fila[0]  
    edad = fila[1]
    genero = fila[2]  
    my_table.insert(parent='', index='end', iid=registro, text=str(registro), 
        values=(nombre, edad, genero))

connection.close()         

# Pack to the screen
my_table.pack(pady=20, padx=20)

window.mainloop()