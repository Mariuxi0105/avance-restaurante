from typing import Dict, Any


class Usuario:
    def __init__(self, id_usuario: int, alias: str, rango: str) -> None:
        id_usuario = int(id_usuario)

        if id_usuario <= 0:
            raise ValueError("El ID de usuario debe ser un entero positivo.")
        if not alias or not alias.strip():
            raise ValueError("El alias de usuario no puede estar vacío.")
        if not rango or not rango.strip():
            raise ValueError("El rango de usuario no puede estar vacío.")

        self.id_usuario: int = id_usuario
        self.alias: str = alias.strip()
        self.rango: str = rango.strip()

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id_usuario": self.id_usuario,
            "alias": self.alias,
            "rango": self.rango,
        }

    @classmethod
    def from_dict(cls, datos: Dict[str, Any]) -> "Usuario":
        for llave in ["id_usuario", "alias", "rango"]:
            if llave not in datos:
                raise KeyError(llave)
        return cls(
            id_usuario=int(datos["id_usuario"]),
            alias=str(datos["alias"]),
            rango=str(datos["rango"]),
        )

    def __str__(self) -> str:
        return f"ID: {self.id_usuario} | Alias: {self.alias} | Rango: {self.rango}"