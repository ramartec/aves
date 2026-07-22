from dao.conexion import Conexion


class DAOBase:

    @staticmethod
    def obtener_conexion():

        return Conexion.obtener_conexion()

    @staticmethod
    def obtener_cursor(dictionary=True):

        conexion = DAOBase.obtener_conexion()

        cursor = conexion.cursor(dictionary=dictionary)

        return conexion, cursor

    @staticmethod
    def cerrar(cursor=None, conexion=None):

        if cursor is not None:
            cursor.close()

        if conexion is not None and conexion.is_connected():
            conexion.close()