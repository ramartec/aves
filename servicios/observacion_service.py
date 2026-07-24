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
    def guardar(observacion: Observacion):
        raise NotImplementedError(
            "ObservacionDAO todavía no tiene insertar() ni actualizar()."
        )

    @staticmethod
    def eliminar(id_observacion):
        raise NotImplementedError(
            "ObservacionDAO todavía no tiene eliminar()."
        )
