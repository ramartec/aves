# servicios/archivo_service.py

from dao.archivo_dao import ArchivoDAO
from modelos.archivo import Archivo
from servicios.base_service import BaseService


class ArchivoService(BaseService):

    @staticmethod
    def listar():
        dao = ArchivoDAO()
        return dao.listar()

    @staticmethod
    def listar_por_observacion(id_observacion):
        dao = ArchivoDAO()
        return dao.listar_por_observacion(id_observacion)

    @staticmethod
    def buscar(id_archivo):
        dao = ArchivoDAO()
        return dao.obtener(id_archivo)

    @staticmethod
    def guardar(archivo: Archivo):
        dao = ArchivoDAO()

        if BaseService.es_nuevo(archivo):
            dao.insertar(archivo)
            return archivo.id_archivo

        dao.actualizar(archivo)
        return archivo.id_archivo

    @staticmethod
    def eliminar(id_archivo):
        dao = ArchivoDAO()
        dao.eliminar(id_archivo)
