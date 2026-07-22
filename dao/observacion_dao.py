from dao.database import Database

from modelos.observacion import Observacion
from dao.especie_dao import EspecieDAO
from dao.ubicacion_dao import UbicacionDAO
from dao.archivo_dao import ArchivoDAO


class ObservacionDAO:

    def __init__(self):

        self.db = Database()

        self.especieDAO = EspecieDAO()

        self.ubicacionDAO = UbicacionDAO()

        self.archivoDAO = ArchivoDAO()

    # =====================================================

    def listar(self):

        conexion = self.db.conectar()

        cursor = conexion.cursor(dictionary=True)

        cursor.execute("""

            SELECT *

            FROM observaciones

            ORDER BY fecha DESC, hora DESC

        """)

        datos = cursor.fetchall()

        cursor.close()

        conexion.close()

        observaciones = []

        for fila in datos:

            observaciones.append(

                self._crear_objeto(fila)

            )

        return observaciones
    
        # =====================================================

    def obtener(self, id_observacion):

        conexion = self.db.conectar()

        cursor = conexion.cursor(dictionary=True)

        cursor.execute(

            """

            SELECT *

            FROM observaciones

            WHERE id_observacion = %s

            """,

            (id_observacion,)

        )

        fila = cursor.fetchone()

        cursor.close()

        conexion.close()

        if fila is None:

            return None

        return self._crear_objeto(fila)

    # =====================================================

    def _crear_objeto(self, fila):

        especie = self.especieDAO.obtener(

            fila["id_especie"]

        )

        ubicacion = self.ubicacionDAO.obtener(

            fila["id_ubicacion"]

        )

        archivos = self.archivoDAO.listar_por_observacion(

            fila["id_observacion"]

        )
    
        # =====================================================

        observacion = Observacion(

            id_observacion=fila["id_observacion"],

            especie=especie,

            ubicacion=ubicacion,

            fecha=fila["fecha"],

            hora=fila["hora"],

            cantidad=fila["cantidad"],

            sexo=fila["sexo"],

            edad=fila["edad"],

            comportamiento=fila["comportamiento"],

            notas=fila["notas"],

            archivos=archivos

        )

        return observacion
    
        # =====================================================

    def listar_por_especie(self, id_especie):

        return [

            observacion

            for observacion in self.listar()

            if observacion.especie
            and observacion.especie.id_especie == id_especie

        ]

    # =====================================================

    def listar_por_ubicacion(self, id_ubicacion):

        return [

            observacion

            for observacion in self.listar()

            if observacion.ubicacion
            and observacion.ubicacion.id_ubicacion == id_ubicacion

        ]