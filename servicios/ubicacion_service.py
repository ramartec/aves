# servicios/ubicacion_service.py

from dao.ubicacion_dao import UbicacionDAO
from modelos.ubicacion import Ubicacion
from servicios.base_service import BaseService


class UbicacionService(BaseService):

    @staticmethod
    def listar():
        dao = UbicacionDAO()
        return dao.listar()

    @staticmethod
    def buscar(id_ubicacion):
        dao = UbicacionDAO()
        return dao.obtener(id_ubicacion)

    @staticmethod
    def guardar(ubicacion: Ubicacion):
        dao = UbicacionDAO()

        if BaseService.es_nuevo(ubicacion):
            dao.insertar(ubicacion)
            return ubicacion.id_ubicacion

        dao.actualizar(ubicacion)
        return ubicacion.id_ubicacion

    @staticmethod
    def eliminar(id_ubicacion):
        dao = UbicacionDAO()
        dao.eliminar(id_ubicacion)
