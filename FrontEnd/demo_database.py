# PASO 1: Importar el módulo "mysql.connector" previamente ¡INSTALADO!
import mysql.connector

# PASO 2: Crear una clase llamada "MyDatabase", 
#         para poder crear la conexión en el archivo Python 
#         de la Interfaz (UI_Tkinter) correspondiente 
class MyDatabase:
    # PASO 3: Crear la función "open_connection", 
    #         para abrir la conexión y tener acceso a la base de datos correspondiente
    def open_connection(self):
        # PASO 4: Crear una variable "connection", 
        #         para almacenar la configuración de la base de datos correspondiente
        connection = mysql.connector.connect( 
            host="localhost",                    
            user="root", 
            passwd="", 
            database="db_demo")
        # PASO 5: Retornar la variable "connection", 
        #         para reutilizarla en el archivo Python de la Interfaz (UI_Tkinter) 
        #         correspondiente
        return connection

    # PASO 6: Crear la función "insert_db", 
    #         para crear registros dentro de una tabla específica
    def insert_db(self, nombre, edad, genero):
        # PASO 7: Crear la variable "my_connection", 
        #         para crear y almacenar la conexión a la base de datos mediante 
        #         la función "open_connection", creada en el PASO 4.
        my_connection = self.open_connection()
        # PASO 8: Crear la variable "cursor", 
        #         para crear un puntero que nos permita acceder a un lugar específico 
        #         de nuestra base de datos
        cursor = my_connection.cursor()
        # PASO 9: Crear la variable "query", 
        #          para crear la instrucción SQL que nos permita INSERTAR o CREAR un registro 
        #          en la base de datos
        #         
        # IMPORTANTE: La estructura de la instrucción SQL está definida 
        #             y lo único que cambia son los CAMPOS y el NOMBRE DE LA TABLA
        query = "INSERT INTO tbl_usuarios(NOMBRE, EDAD, GENERO) VALUES (%s,%s,%s)"
        # PASO 10: Crear la variable "data", 
        #          para almacenar los datos o información correspondiente al registro
        #          que deseamos insertar en el paso anterior
        # 
        # IMPORTANTE: los valores de las variables (EMAIL, PWD, AGE) debe OBTENERLOS 
        #             mediante la función GET() en la Interfaz de Tkinter y enviarlos 
        #             como PARÁMETROS a la función insert_db()
        data = (nombre, edad, genero)
        # PASO 11: Ejecutar la función "EXECUTE()", 
        #          y enviarle como PÁRAMETROS las variables "query" y "data" previamente creadas
        #          en los pasos 11 y 10, 
        #          para realizar la CONSULTA SQL a la base de datos
        #
        # IMPORTANTE: Esta función permite ejecutar lenguaje SQL dentro de un archivo Python 
        #             y así modificar la base de datos desde el BackEnd y no desde la interfaz de PhpMyAdmin
        cursor.execute(query, data)
        # PASO 12: Ejecutar la función "commit()", 
        #          para confirmar la escritura en la base de datos
        my_connection.commit()
        # PASO 13: Ejecutar la función "close()", 
        #          para cerrar la conexión a la base de datos 
        my_connection.close()


