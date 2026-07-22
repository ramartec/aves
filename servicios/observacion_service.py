# servicios/observacion_service.py

from dao.observacion_dao import ObservacionDAO
from modelos.observacion import Observacion
from servicios.base_service import BaseService


class ObservacionService(BaseService):

    @staticmethod
    def listar():

        return ObservacionDAO.listar()

    @staticmethod
    def buscar(id_observacion):

        return ObservacionDAO.buscar_por_id(id_observacion)

    @staticmethod
    def guardar(observacion: Observacion):

        if BaseService.es_nuevo(observacion):

            return ObservacionDAO.insertar(observacion)

        ObservacionDAO.editar(observacion)

        return observacion.id_observacion

    @staticmethod
    def eliminar(id_observacion):

        return ObservacionDAO.eliminar(id_observacion)