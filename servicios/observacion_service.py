# servicios/observacion_service.py

from dao.observacion_dao import ObservacionDAO
from modelos.observacion import Observacion


class ObservacionService:

    @staticmethod
    def listar():
        dao = ObservacionDAO()
        return dao.listar()

    @staticmethod
    def buscar(id_observacion):
        dao = ObservacionDAO()
        return dao.obtener(id_observacion)

    @staticmethod
    def guardar(observacion: Observacion):   # CAMBIO: ya no lanza excepción
        dao = ObservacionDAO()

        if observacion.id_observacion is None:
            dao.insertar(observacion)
        else:
            dao.actualizar(observacion)

        return observacion.id_observacion

    @staticmethod
    def eliminar(id_observacion):            # CAMBIO: ya no lanza excepción
        dao = ObservacionDAO()
        dao.eliminar(id_observacion)
