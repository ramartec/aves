import mysql.connector


class Database:

    HOST = "localhost"

    USER = "root"

    PASSWORD = ""

    DATABASE = "avesronald"

    PORT = 3306

    @classmethod
    def conectar(cls):

        return mysql.connector.connect(

            host=cls.HOST,

            user=cls.USER,

            password=cls.PASSWORD,

            database=cls.DATABASE,

            port=cls.PORT,

            charset="utf8mb4"

        )

    @classmethod
    def probar_conexion(cls):

        conexion = None

        try:

            conexion = cls.conectar()

            return True

        except Exception as error:

            print(error)

            return False

        finally:

            if conexion is not None and conexion.is_connected():

                conexion.close()
