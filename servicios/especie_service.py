# servicios/especie_service.py

from dao.especie_dao import EspecieDAO
from modelos.especie import Especie
from servicios.base_service import BaseService


class EspecieService(BaseService):

    @staticmethod
    def listar():

        return EspecieDAO.listar()

    @staticmethod
    def buscar(id_especie):

        return EspecieDAO.buscar_por_id(id_especie)

    @staticmethod
    def guardar(especie: Especie):

        if BaseService.es_nuevo(especie):

            return EspecieDAO.insertar(especie)

        EspecieDAO.editar(especie)

        return especie.id_especie

    @staticmethod
    def eliminar(id_especie):

        return EspecieDAO.eliminar(id_especie)