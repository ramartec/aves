# servicios/archivo_service.py

from dao.archivo_dao import ArchivoDAO
from modelos.archivo import Archivo
from servicios.base_service import BaseService


class ArchivoService(BaseService):

    @staticmethod
    def listar():

        return ArchivoDAO.listar()

    @staticmethod
    def listar_por_observacion(id_observacion):

        return ArchivoDAO.listar_por_observacion(id_observacion)

    @staticmethod
    def buscar(id_archivo):

        return ArchivoDAO.buscar_por_id(id_archivo)

    @staticmethod
    def guardar(archivo: Archivo):

        if BaseService.es_nuevo(archivo):

            return ArchivoDAO.insertar(archivo)

        ArchivoDAO.editar(archivo)

        return archivo.id_archivo

    @staticmethod
    def eliminar(id_archivo):

        return ArchivoDAO.eliminar(id_archivo)