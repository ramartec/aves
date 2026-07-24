# servicios/base_service.py

class BaseService:

    @staticmethod
    def es_nuevo(objeto):
        if hasattr(objeto, "id_observacion"):
            return objeto.id_observacion is None

        if hasattr(objeto, "id_archivo"):
            return objeto.id_archivo is None

        if hasattr(objeto, "id_especie"):
            return objeto.id_especie is None

        if hasattr(objeto, "id_ubicacion"):
            return objeto.id_ubicacion is None

        return False
