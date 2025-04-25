import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
from datetime import datetime

from services.cliente_service import crear_cliente, obtener_clientes
from services.cita_service import agregar_cita_a_cliente, obtener_citas_de_cliente
from models.cliente import Cliente
from models.cita import Cita
from ui.charts import mostrar_grafica_mensual

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Citas - Consultor Python")
        self.root.geometry("900x700")
        self.crear_widgets()

    def crear_widgets(self):
        # Frame izquierdo - lista de clientes
        self.cliente_frame = ttk.Frame(self.root)
        self.cliente_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

        ttk.Label(self.cliente_frame, text="Clientes").pack()
        self.lista_clientes = tk.Listbox(self.cliente_frame, height=20)
        self.lista_clientes.pack()
        self.lista_clientes.bind("<<ListboxSelect>>", self.mostrar_citas)

        ttk.Button(self.cliente_frame, text="Recargar", command=self.cargar_clientes).pack(pady=5)
        ttk.Button(self.cliente_frame, text="Agregar Cliente", command=self.mostrar_formulario_cliente).pack(pady=5)

        # Frame para agregar cliente
        self.form_cliente = ttk.Frame(self.root)
        self.form_cliente.pack(side=tk.LEFT, padx=20, pady=20)

        ttk.Label(self.form_cliente, text="Nombre").pack()
        self.nombre_cliente_entry = ttk.Entry(self.form_cliente)
        self.nombre_cliente_entry.pack()

        ttk.Label(self.form_cliente, text="Correo").pack()
        self.correo_cliente_entry = ttk.Entry(self.form_cliente)
        self.correo_cliente_entry.pack()

        ttk.Label(self.form_cliente, text="Teléfono").pack()
        self.telefono_cliente_entry = ttk.Entry(self.form_cliente)
        self.telefono_cliente_entry.pack()

        ttk.Label(self.form_cliente, text="Empresa").pack()
        self.empresa_cliente_entry = ttk.Entry(self.form_cliente)
        self.empresa_cliente_entry.pack()

        ttk.Button(self.form_cliente, text="Guardar Cliente", command=self.agregar_cliente).pack(pady=5)

        # Frame derecho - citas y gráfica
        self.derecho_frame = ttk.Frame(self.root)
        self.derecho_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.tree_citas = ttk.Treeview(self.derecho_frame, columns=("fecha", "tema", "estado"), show='headings')
        for col in self.tree_citas["columns"]:
            self.tree_citas.heading(col, text=col.capitalize())
        self.tree_citas.pack(fill=tk.BOTH, expand=True)

        ttk.Button(self.derecho_frame, text="Mostrar Gráfica Mensual", command=self.graficar).pack(pady=10)
        ttk.Button(self.derecho_frame, text="Agregar Cita", command=self.mostrar_formulario_cita).pack(pady=5)

        # Frame para agregar cita
        self.form_cita = ttk.Frame(self.root)
        self.form_cita.pack(side=tk.RIGHT, padx=20, pady=20)

        ttk.Label(self.form_cita, text="Fecha y Hora (YYYY-MM-DD HH:MM)").pack()
        self.fecha_cita_entry = ttk.Entry(self.form_cita)
        self.fecha_cita_entry.pack()

        ttk.Label(self.form_cita, text="Duración (minutos)").pack()
        self.duracion_cita_entry = ttk.Entry(self.form_cita)
        self.duracion_cita_entry.pack()

        ttk.Label(self.form_cita, text="Tema de la cita").pack()
        self.tema_cita_entry = ttk.Entry(self.form_cita)
        self.tema_cita_entry.pack()

        ttk.Button(self.form_cita, text="Guardar Cita", command=self.agregar_cita).pack(pady=5)

        self.cargar_clientes()

    def cargar_clientes(self):
        self.lista_clientes.delete(0, tk.END)
        self.clientes = obtener_clientes()
        for cliente in self.clientes:
            self.lista_clientes.insert(tk.END, cliente.nombre)

    def mostrar_citas(self, event):
        seleccion = self.lista_clientes.curselection()
        if not seleccion:
            return
        nombre = self.lista_clientes.get(seleccion)
        citas = obtener_citas_de_cliente(nombre)

        # Limpiar el treeview
        for row in self.tree_citas.get_children():
            self.tree_citas.delete(row)

        for cita in citas:
            self.tree_citas.insert("", tk.END, values=(cita.fecha.strftime("%Y-%m-%d %H:%M"), cita.tema, cita.estado))

    def graficar(self):
        seleccion = self.lista_clientes.curselection()
        if not seleccion:
            messagebox.showinfo("Info", "Selecciona un cliente primero.")
            return
        nombre = self.lista_clientes.get(seleccion)
        mostrar_grafica_mensual(self.derecho_frame, nombre)

    def mostrar_formulario_cliente(self):
        self.form_cliente.pack(side=tk.LEFT, padx=20, pady=20)

    def mostrar_formulario_cita(self):
        seleccion = self.lista_clientes.curselection()
        if not seleccion:
            messagebox.showinfo("Info", "Selecciona un cliente primero.")
            return
        self.form_cita.pack(side=tk.RIGHT, padx=20, pady=20)

    def agregar_cliente(self):
        nombre = self.nombre_cliente_entry.get()
        correo = self.correo_cliente_entry.get()
        telefono = self.telefono_cliente_entry.get()
        empresa = self.empresa_cliente_entry.get()

        if not nombre or not correo or not telefono or not empresa:
            messagebox.showwarning("Campos vacíos", "Por favor, llena todos los campos.")
            return

        cliente = Cliente(nombre, correo, telefono, empresa)
        crear_cliente(cliente)

        messagebox.showinfo("Cliente agregado", f"El cliente {nombre} fue agregado con éxito.")
        self.cargar_clientes()

    def agregar_cita(self):
        seleccion = self.lista_clientes.curselection()
        if not seleccion:
            messagebox.showinfo("Info", "Selecciona un cliente primero.")
            return

        nombre_cliente = self.lista_clientes.get(seleccion)
        fecha_str = self.fecha_cita_entry.get()
        duracion = self.duracion_cita_entry.get()
        tema = self.tema_cita_entry.get()

        try:
            fecha = datetime.strptime(fecha_str, "%Y-%m-%d %H:%M")
            duracion = int(duracion)
        except ValueError:
            messagebox.showwarning("Formato incorrecto", "La fecha o la duración no son correctas.")
            return

        cita = Cita(fecha.isoformat(), duracion, tema)
        agregar_cita_a_cliente(nombre_cliente, cita)

        messagebox.showinfo("Cita agregada", f"La cita para {nombre_cliente} fue agregada con éxito.")
        self.mostrar_citas(None)
