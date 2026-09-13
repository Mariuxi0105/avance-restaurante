import tkinter as tk
from tkinter import messagebox, ttk
from typing import Callable

from modelos.usuario import Usuario
from servicios.restaurante_servicio import RestauranteServicio


class LoginView(ttk.Frame):
    """Pantalla de acceso simulado."""

    def __init__(
        self,
        master: tk.Misc,
        servicio: RestauranteServicio,
        al_ingresar: Callable[[Usuario], None],
    ) -> None:
        super().__init__(master, padding=32)
        self.servicio = servicio
        self.al_ingresar = al_ingresar
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        tarjeta = ttk.Frame(self, padding=28, relief="solid", borderwidth=1)
        tarjeta.grid(row=0, column=0)
        tarjeta.columnconfigure(1, weight=1)

        ttk.Label(tarjeta, text="Restaurante App", font=("Segoe UI", 22, "bold")).grid(
            row=0, column=0, columnspan=2, pady=(0, 6)
        )
        ttk.Label(tarjeta, text="Acceso al sistema", font=("Segoe UI", 11)).grid(
            row=1, column=0, columnspan=2, pady=(0, 22)
        )

        ttk.Label(tarjeta, text="Usuario").grid(row=2, column=0, sticky="w", padx=(0, 12), pady=6)
        self.usuario_var = tk.StringVar()
        usuario_entry = ttk.Entry(tarjeta, textvariable=self.usuario_var, width=28)
        usuario_entry.grid(row=2, column=1, sticky="ew", pady=6)

        ttk.Label(tarjeta, text="Contraseña").grid(row=3, column=0, sticky="w", padx=(0, 12), pady=6)
        self.contrasena_var = tk.StringVar()
        contrasena_entry = ttk.Entry(tarjeta, textvariable=self.contrasena_var, show="*", width=28)
        contrasena_entry.grid(row=3, column=1, sticky="ew", pady=6)

        ttk.Button(tarjeta, text="Ingresar", command=self._intentar_ingreso).grid(
            row=4, column=0, columnspan=2, sticky="ew", pady=(18, 8)
        )
        ttk.Label(tarjeta, text="Demo: admin / 1").grid(row=5, column=0, columnspan=2)
        usuario_entry.focus_set()
        contrasena_entry.bind("<Return>", lambda _evento: self._intentar_ingreso())

    def _intentar_ingreso(self) -> None:
        if not self.usuario_var.get().strip() or not self.contrasena_var.get().strip():
            messagebox.showwarning("Datos incompletos", "Ingrese usuario y contraseña.")
            return

        usuario = self.servicio.validar_acceso(
            self.usuario_var.get(), self.contrasena_var.get()
        )
        if usuario is None:
            messagebox.showerror("Acceso denegado", "Las credenciales no son válidas.")
            return
        self.al_ingresar(usuario)
