from typing import Dict, Any

class Producto:
    def __init__(self, id_producto: int, nombre: str, precio: float, categoria: str, stock: int = 10) -> None:
        id_producto = int(id_producto)
        stock = int(stock)
        precio = float(precio)

        if id_producto <= 0:
            raise ValueError("El ID del producto debe ser un entero positivo.")
        if not nombre or not nombre.strip():
            raise ValueError("El nombre del producto no puede estar vacío.")
        if precio <= 0:
            raise ValueError("El precio debe ser un número mayor a cero.")
        if stock < 0:
            raise ValueError("El stock no puede ser negativo.")

        self.id_producto: int = id_producto
        self.nombre: str = nombre.strip()
        self.precio: float = precio
        self.categoria: str = categoria.strip()
        self.stock: int = stock

    def vender(self, cantidad: int) -> None:
        """Disminuye el stock disponible tras validar suficiencia."""
        if cantidad <= 0:
            raise ValueError("La cantidad a vender debe ser mayor a cero.")
        if self.stock < cantidad:
            raise ValueError("Stock insuficiente para realizar la venta.")
        self.stock -= cantidad

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id_producto": self.id_producto,
            "nombre": self.nombre,
            "precio": self.precio,
            "categoria": self.categoria,
            "stock": self.stock
        }

    @classmethod
    def from_dict(cls, datos: Dict[str, Any]) -> 'Producto':
        for llave in ["id_producto", "nombre", "precio", "categoria", "stock"]:
            if llave not in datos:
                raise KeyError(llave)
        return cls(
            id_producto=int(datos["id_producto"]),
            nombre=str(datos["nombre"]),
            precio=float(datos["precio"]),
            categoria=str(datos["categoria"]),
            stock=int(datos["stock"])
        )

    def __str__(self) -> str:
        return f"ID: {self.id_producto} | {self.nombre} ({self.categoria}) | ${self.precio:.2f} | Stock: {self.stock}"