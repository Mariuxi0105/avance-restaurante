import tkinter as tk
from tkinter import ttk
from typing import Callable

from modelos.usuario import Usuario
from servicios.restaurante_servicio import RestauranteServicio


class MainView(ttk.Frame):
    """Panel principal para consultar usuarios y productos."""

    def __init__(
        self,
        master: tk.Misc,
        servicio: RestauranteServicio,
        usuario: Usuario,
        cerrar_sesion: Callable[[], None],
    ) -> None:
        super().__init__(master, padding=20)
        self.servicio = servicio
        self.usuario = usuario
        self.cerrar_sesion = cerrar_sesion
        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)

        encabezado = ttk.Frame(self)
        encabezado.grid(row=0, column=0, columnspan=2, sticky="ew", pady=(0, 18))
        encabezado.columnconfigure(0, weight=1)
        ttk.Label(encabezado, text="Panel principal", font=("Segoe UI", 22, "bold")).grid(
            row=0, column=0, sticky="w"
        )
        ttk.Label(encabezado, text=f"Sesión: {usuario.alias}").grid(row=0, column=1, padx=12)
        ttk.Button(encabezado, text="Cerrar sesión", command=self.cerrar_sesion).grid(
            row=0, column=2
        )

        menu = ttk.Frame(self)
        menu.grid(row=1, column=0, sticky="ns", padx=(0, 18))
        ttk.Button(menu, text="Productos", command=self.mostrar_productos).pack(fill="x", pady=3)
        ttk.Button(menu, text="Usuarios", command=self.mostrar_usuarios).pack(fill="x", pady=3)
        ttk.Button(menu, text="Ventas (pendiente)", state="disabled").pack(fill="x", pady=3)

        self.contenido = ttk.Frame(self)
        self.contenido.grid(row=1, column=1, sticky="nsew")
        self.contenido.columnconfigure(0, weight=1)
        self.contenido.rowconfigure(1, weight=1)
        self.mostrar_productos()

    def _limpiar_contenido(self) -> None:
        for widget in self.contenido.winfo_children():
            widget.destroy()

    def mostrar_productos(self) -> None:
        self._mostrar_tabla(
            "Productos registrados",
            ("id", "nombre", "categoria", "precio", "stock"),
            ("ID", "Nombre", "Categoría", "Precio", "Cantidad"),
            [
                (producto.id_producto, producto.nombre, producto.categoria, f"${producto.precio:.2f}", producto.stock)
                for producto in self.servicio.listar_productos()
            ],
        )

    def mostrar_usuarios(self) -> None:
        self._mostrar_tabla(
            "Usuarios registrados",
            ("id", "alias", "rango"),
            ("ID", "Usuario", "Rol"),
            [
                (usuario.id_usuario, usuario.alias, usuario.rango)
                for usuario in self.servicio.listar_usuarios()
            ],
        )

    def _mostrar_tabla(
        self,
        titulo: str,
        columnas: tuple[str, ...],
        encabezados: tuple[str, ...],
        filas: list[tuple[object, ...]],
    ) -> None:
        self._limpiar_contenido()
        ttk.Label(self.contenido, text=titulo, font=("Segoe UI", 16, "bold")).grid(
            row=0, column=0, sticky="w", pady=(0, 12)
        )
        tabla = ttk.Treeview(self.contenido, columns=columnas, show="headings")
        for columna, encabezado in zip(columnas, encabezados):
            tabla.heading(columna, text=encabezado)
            tabla.column(columna, width=130, anchor="center")
        tabla.grid(row=1, column=0, sticky="nsew")
        barra = ttk.Scrollbar(self.contenido, orient="vertical", command=tabla.yview)
        barra.grid(row=1, column=1, sticky="ns")
        tabla.configure(yscrollcommand=barra.set)
        for fila in filas:
            tabla.insert("", "end", values=fila)
