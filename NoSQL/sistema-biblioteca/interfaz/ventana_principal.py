# Archivo: interfaz/ventana_principal.py

import tkinter as tk
from tkinter import ttk, messagebox
from modelos.libro import Libro
from modelos.autor import Autor
from servicios.servicio_libros import guardar_libro, obtener_libros

class AplicacionPrincipal:
    def __init__(self, raiz):
        self.raiz = raiz
        self.raiz.title("Gestor de Libros")
        self.raiz.geometry("600x600")  # Aumentar el tamaño de la ventana
        self.raiz.resizable(False, False)
        self.construir_interfaz()

    def construir_interfaz(self):
        color_fondo_ventana = "#dad870"
        color_fondo_entrada = "#f7f7f7"
        color_verde_activo = "#3c4c34"
        color_texto = "#202820"
        color_fondo_boton = "#748c54"
        color_fondo_lista = "#748c54"

        self.raiz.configure(bg=color_fondo_ventana)

        # Crear un frame contenedor para centrar y alinear mejor
        self.frame_contenedor = ttk.Frame(self.raiz, padding="10")
        self.frame_contenedor.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        # Frame del formulario
        self.frame_formulario = ttk.Frame(self.frame_contenedor, padding="10")
        self.frame_formulario.grid(row=0, column=0, sticky="ew")

        for i in range(2):  # Asegurar expansión de columnas
            self.frame_formulario.columnconfigure(i, weight=1)

        ttk.Label(self.frame_formulario, text="Título del libro:", background=color_fondo_entrada, foreground=color_texto).grid(row=0, column=0, sticky="e", padx=10, pady=5)
        self.entrada_titulo = ttk.Entry(self.frame_formulario, width=40)
        self.entrada_titulo.grid(row=0, column=1, padx=10, pady=5)

        ttk.Label(self.frame_formulario, text="Autor:", background=color_fondo_entrada, foreground=color_texto).grid(row=1, column=0, sticky="e", padx=10, pady=5)
        self.entrada_autor = ttk.Entry(self.frame_formulario, width=40)
        self.entrada_autor.grid(row=1, column=1, padx=10, pady=5)

        ttk.Label(self.frame_formulario, text="Nacionalidad del autor:", background=color_fondo_entrada, foreground=color_texto).grid(row=2, column=0, sticky="e", padx=10, pady=5)
        self.entrada_nacionalidad = ttk.Entry(self.frame_formulario, width=40)
        self.entrada_nacionalidad.grid(row=2, column=1, padx=10, pady=5)

        self.var_leido = tk.BooleanVar()
        ttk.Checkbutton(self.frame_formulario, text="¿Leído?", variable=self.var_leido).grid(row=3, columnspan=2, pady=5)

        ttk.Label(self.frame_formulario, text="Fecha de lectura (YYYY-MM-DD):", background=color_fondo_entrada, foreground=color_texto).grid(row=4, column=0, sticky="e", padx=10, pady=5)
        self.entrada_fecha = ttk.Entry(self.frame_formulario, width=40)
        self.entrada_fecha.grid(row=4, column=1, padx=10, pady=5)

        ttk.Button(self.frame_formulario, text="Guardar libro", command=self.guardar_libro, width=40, style="TButton").grid(row=5, column=1, columnspan=2, pady=10)
        ttk.Button(self.frame_formulario, text="Mostrar todos", command=self.mostrar_libros, width=40, style="TButton").grid(row=6, column=1, columnspan=2, pady=10)

        # Área de texto igualando el ancho del frame
        self.lista_libros = tk.Text(self.frame_contenedor, height=12, width=70, bg=color_fondo_lista, fg=color_texto, font=("Arial", 10), wrap=tk.WORD)
        self.lista_libros.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        style = ttk.Style()
        style.configure("TButton", background=color_fondo_boton, foreground=color_texto)
        style.map("TButton", background=[('active', color_verde_activo)])

    def guardar_libro(self):
        titulo = self.entrada_titulo.get()
        autor_nombre = self.entrada_autor.get()
        nacionalidad = self.entrada_nacionalidad.get()
        leido = self.var_leido.get()
        fecha = self.entrada_fecha.get() if leido else None

        if not titulo or not autor_nombre or not nacionalidad:
            messagebox.showwarning("Faltan datos", "Todos los campos deben estar llenos.")
            return

        autor = Autor(autor_nombre, nacionalidad)
        libro = Libro(titulo, autor.a_diccionario(), leido, fecha)
        guardar_libro(libro)
        messagebox.showinfo("Éxito", "Libro guardado correctamente.")
        self.limpiar_entradas()

    def mostrar_libros(self):
        self.lista_libros.delete(1.0, tk.END)
        libros = obtener_libros()
        for libro in libros:
            texto = f"{libro['titulo']} - {libro['autor']['nombre']} ({libro['autor']['nacionalidad']})"
            if libro.get("leido"):
                texto += f" - Leído el {libro.get('fecha_lectura')}"
            texto += "\n"
            self.lista_libros.insert(tk.END, texto)

    def limpiar_entradas(self):
        self.entrada_titulo.delete(0, tk.END)
        self.entrada_autor.delete(0, tk.END)
        self.entrada_nacionalidad.delete(0, tk.END)
        self.entrada_fecha.delete(0, tk.END)
        self.var_leido.set(False)
