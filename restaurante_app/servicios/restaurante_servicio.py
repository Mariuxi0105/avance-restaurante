from typing import List, Optional

from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.archivo_servicio import ArchivoServicio


class RestauranteServicio:
    """Fachada de datos y reglas necesarias para la primera interfaz gráfica."""

    def __init__(self, archivo_servicio: type[ArchivoServicio] = ArchivoServicio) -> None:
        self._archivo_servicio = archivo_servicio
        self._productos: List[Producto] = []
        self._usuarios: List[Usuario] = []

    def cargar_datos(self) -> None:
        self._productos = self._archivo_servicio.cargar_productos()
        self._usuarios = self._archivo_servicio.cargar_usuarios()

    def validar_acceso(self, alias: str, contrasena: str) -> Optional[Usuario]:
        """Valida el acceso simulado usando alias e ID del usuario."""
        alias_normalizado = alias.strip().lower()
        for usuario in self._usuarios:
            if usuario.alias.lower() == alias_normalizado and str(usuario.id_usuario) == contrasena.strip():
                return usuario
        return None

    def listar_productos(self) -> List[Producto]:
        return list(self._productos)

    def listar_usuarios(self) -> List[Usuario]:
        return list(self._usuarios)

    def cantidad_productos(self) -> int:
        return len(self._productos)

    def cantidad_usuarios(self) -> int:
        return len(self._usuarios)
