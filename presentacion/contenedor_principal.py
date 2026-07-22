import customtkinter as ctk

from presentacion.panel_inicio import PanelInicio
from presentacion.pantalla_detalle_observacion import PantallaDetalleObservacion


class ContenedorPrincipal(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(
            master,
            fg_color="transparent"
        )

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.pantalla_actual = None

        self.mostrar_inicio()

    # ==================================================

    def limpiar(self):

        if self.pantalla_actual is not None:

            self.pantalla_actual.destroy()

            self.pantalla_actual = None

    # ==================================================

    def mostrar_inicio(self):

        self.limpiar()

        self.pantalla_actual = PanelInicio(self)

        self.pantalla_actual.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

    # ==================================================

    def mostrar_detalle(self):

        self.limpiar()

        self.pantalla_actual = PantallaDetalleObservacion(self)

        self.pantalla_actual.grid(
            row=0,
            column=0,
            sticky="nsew"
        )