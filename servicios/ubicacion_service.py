# servicios/ubicacion_service.py

from dao.ubicacion_dao import UbicacionDAO
from modelos.ubicacion import Ubicacion
from servicios.base_service import BaseService


class UbicacionService(BaseService):

    @staticmethod
    def listar():

        return UbicacionDAO.listar()

    @staticmethod
    def buscar(id_ubicacion):

        return UbicacionDAO.buscar_por_id(id_ubicacion)

    @staticmethod
    def guardar(ubicacion: Ubicacion):

        if BaseService.es_nuevo(ubicacion):

            return UbicacionDAO.insertar(ubicacion)

        UbicacionDAO.editar(ubicacion)

        return ubicacion.id_ubicacion

    @staticmethod
    def eliminar(id_ubicacion):

        return UbicacionDAO.eliminar(id_ubicacion)