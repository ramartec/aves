# servicios/especie_service.py

from dao.especie_dao import EspecieDAO
from modelos.especie import Especie
from servicios.base_service import BaseService


class EspecieService(BaseService):

    @staticmethod
    def listar():
        dao = EspecieDAO()
        return dao.listar()

    @staticmethod
    def buscar(id_especie):
        dao = EspecieDAO()
        return dao.obtener(id_especie)

    @staticmethod
    def guardar(especie: Especie):
        dao = EspecieDAO()

        if BaseService.es_nuevo(especie):
            dao.insertar(especie)
            return especie.id_especie

        dao.actualizar(especie)
        return especie.id_especie

    @staticmethod
    def eliminar(id_especie):
        dao = EspecieDAO()
        dao.eliminar(id_especie)
