import mysql.connector


class Conexion:

    HOST = "localhost"

    PUERTO = 3306

    USUARIO = "root"

    PASSWORD = ""

    BASE_DATOS = "avesRonald"

    @staticmethod
    def obtener_conexion():

        return mysql.connector.connect(

            host=Conexion.HOST,

            port=Conexion.PUERTO,

            user=Conexion.USUARIO,

            password=Conexion.PASSWORD,

            database=Conexion.BASE_DATOS

        )
