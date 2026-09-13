# Restaurante App

Desarrollado por: MARIUXI JESSENIA TEJADA MAYORGA

Aplicación desktop de gestión básica de un restaurante desarrollada con Python y Tkinter. La estructura sigue una separación por capas: modelos, servicios y vista.

## Estructura del proyecto

```text
restaurante_app/
├── .gitignore
├── main.py
├── README.md
├── datos/
│   ├── productos.json
│   └── usuarios.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
└── .git
```

## Capas de la aplicación

- Modelo: define las entidades `Producto` y `Usuario`.
- Servicio: lee y escribe los datos desde JSON a través de `ArchivoServicio` y valida el acceso del usuario en `RestauranteServicio`.
- Vista: `LoginView` y `MainView` renderizan la interfaz con Tkinter.
- Controlador de arranque: `main.py` crea la ventana principal y conecta la lógica con la vista.

## Datos

La aplicación consume los datos almacenados en los archivos JSON dentro de la carpeta `datos/`:

- `productos.json`
- `usuarios.json`

## Ejecución

Desde la raíz del proyecto:

```bash
python main.py
```

## Acceso de demostración

```text
Usuario: admin
Contraseña: 1
```

## Validación

Se puede verificar la sintaxis del proyecto con:

```bash
python -m compileall -q main.py modelos servicios ui
```
