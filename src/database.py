import mysql.connector

class GestorBaseDatos:
    def __init__(self):
        self.conexion = None
        self.cursor = None

    def conectar(self):
        """Conectar a la base de datos y devolver la conexión y el cursor."""
        self.conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="escritorio"
        )
        self.cursor = self.conexion.cursor()

    def desconectar(self):
        """Cerrar la conexión y el cursor."""
        if self.cursor:
            self.cursor.close()
        if self.conexion:
            self.conexion.close()

    def obtener_contactos(self):
        """Obtener todos los contactos de la base de datos."""
        self.conectar()
        self.cursor.execute("SELECT * FROM alumnos")
        contactos = self.cursor.fetchall()
        self.desconectar()
        return contactos

    def guardar_contacto(self, nombre, edad):
        """Guardar un nuevo contacto en la base de datos."""
        self.conectar()
        self.cursor.execute("INSERT INTO alumnos (nombre, edad) VALUES (%s, %s)", (nombre, edad))
        self.conexion.commit()
        self.desconectar()

    def actualizar_contacto(self, id_contacto, nuevo_nombre, nueva_edad):
        """Actualizar un contacto en la base de datos."""
        self.conectar()
        self.cursor.execute("UPDATE alumnos SET nombre = %s, edad = %s WHERE id = %s", (nuevo_nombre, nueva_edad, id_contacto))
        self.conexion.commit()
        self.desconectar()

    def eliminar_contacto(self, id_contacto):
        """Eliminar un contacto de la base de datos."""
        self.conectar()
        self.cursor.execute("DELETE FROM alumnos WHERE id = %s", (id_contacto,))
        self.conexion.commit()
        self.desconectar()

# Ejemplo de uso:
gestor_bd = GestorBaseDatos()
# contactos = gestor_bd.obtener_contactos()
# print(contactos)
