from servicios.observacion_service import ObservacionService


class BuscadorService:

    @staticmethod
    def buscar(
        especie="",
        ubicacion="",
        sexo="",
        fecha=None
    ):
        observaciones = ObservacionService.listar()
        resultado = []

        especie_buscada = (especie or "").strip().lower()
        ubicacion_buscada = (ubicacion or "").strip().lower()
        sexo_buscado = (sexo or "").strip().lower()

        for observacion in observaciones:

            if especie_buscada:
                nombre_comun = ""
                nombre_cientifico = ""

                if observacion.especie:
                    nombre_comun = (
                        observacion.especie.nombre_comun or ""
                    ).lower()

                    nombre_cientifico = (
                        observacion.especie.nombre_cientifico or ""
                    ).lower()

                if (
                    especie_buscada not in nombre_comun
                    and especie_buscada not in nombre_cientifico
                ):
                    continue

            if ubicacion_buscada:
                lugar = ""

                if observacion.ubicacion:
                    lugar = (
                        observacion.ubicacion.sitio or ""
                    ).lower()

                if ubicacion_buscada not in lugar:
                    continue

            if sexo_buscado:
                sexo_observacion = (
                    observacion.sexo or ""
                ).lower()

                if sexo_buscado != sexo_observacion:
                    continue

            if fecha is not None:
                if observacion.fecha != fecha:
                    continue

            resultado.append(observacion)

        return resultado
