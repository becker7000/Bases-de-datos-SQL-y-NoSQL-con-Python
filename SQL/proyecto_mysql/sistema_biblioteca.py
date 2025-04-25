import tkinter as tk
from tkinter import messagebox
import mysql.connector

# TODO: Mejorar este sistema y hacerlo orientado a objetos con interfaz gráfica

# ---------- Conexión ----------
def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="toor",
        database="bd_python_abril"
    )

# ---------- Funciones de BD ----------
def obtener_autores():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre FROM autores")
    datos = cursor.fetchall()
    conn.close()
    return datos

def obtener_editoriales():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre FROM editoriales")
    datos = cursor.fetchall()
    conn.close()
    return datos

def insertar_autor(nombre):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO autores (nombre) VALUES (%s)", (nombre,))
    conn.commit()
    conn.close()

def insertar_editorial(nombre):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO editoriales (nombre) VALUES (%s)", (nombre,))
    conn.commit()
    conn.close()

def insertar_libro(titulo, id_autor, id_editorial):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO libros (titulo, id_autor, id_editorial) VALUES (%s, %s, %s)",
                   (titulo, id_autor, id_editorial))
    conn.commit()
    conn.close()

def obtener_libros():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT libros.titulo, autores.nombre, editoriales.nombre
        FROM libros
        JOIN autores ON libros.id_autor = autores.id
        JOIN editoriales ON libros.id_editorial = editoriales.id
    """)
    datos = cursor.fetchall()
    conn.close()
    return datos

# ---------- GUI Helpers ----------
def seleccionar_o_agregar_elemento(lista, insertar_func, titulo):
    ventana = tk.Toplevel()
    ventana.title(titulo)
    seleccionado = {'id': None, 'nombre': None}

    def seleccionar():
        idx = lista_lb.curselection()
        if idx:
            seleccionado['id'] = lista[idx[0]][0]
            ventana.destroy()

    def agregar():
        nombre = entry.get()
        if nombre:
            insertar_func(nombre)
            ventana.destroy()

    lista_lb = tk.Listbox(ventana, width=40)
    for item in lista:
        lista_lb.insert(tk.END, f"{item[1]}")
    lista_lb.pack(padx=10, pady=5)

    entry = tk.Entry(ventana)
    entry.pack(pady=5)

    tk.Button(ventana, text="Agregar nuevo", command=agregar).pack(pady=3)
    tk.Button(ventana, text="Seleccionar", command=seleccionar).pack(pady=3)

    ventana.grab_set()
    ventana.wait_window()
    return seleccionado['id']

def seleccionar_autor():
    global autor_id
    lista = obtener_autores()
    autor_id = seleccionar_o_agregar_elemento(lista, insertar_autor, "Seleccionar o Agregar Autor")
    if autor_id:
        lbl_autor.config(text=f"Autor seleccionado: {dict(lista)[autor_id]}")

def seleccionar_editorial():
    global editorial_id
    lista = obtener_editoriales()
    editorial_id = seleccionar_o_agregar_elemento(lista, insertar_editorial, "Seleccionar o Agregar Editorial")
    if editorial_id:
        lbl_editorial.config(text=f"Editorial seleccionada: {dict(lista)[editorial_id]}")

def agregar_libro():
    titulo = entry_titulo.get()
    if not titulo:
        messagebox.showwarning("Error", "Ingrese un título.")
        return
    if not autor_id or not editorial_id:
        messagebox.showwarning("Error", "Seleccione autor y editorial.")
        return
    insertar_libro(titulo, autor_id, editorial_id)
    entry_titulo.delete(0, tk.END)
    actualizar_lista_libros()
    messagebox.showinfo("Éxito", "Libro agregado correctamente.")

def actualizar_lista_libros():
    lista_libros.delete(0, tk.END)
    for titulo, autor, editorial in obtener_libros():
        lista_libros.insert(tk.END, f"{titulo} | {autor} | {editorial}")

# ---------- GUI PRINCIPAL ----------
root = tk.Tk()
root.title("Gestor de Libros")
root.geometry("600x400")

autor_id = None
editorial_id = None

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

tk.Label(frame, text="Título del libro:").grid(row=0, column=0, sticky="w")
entry_titulo = tk.Entry(frame, width=40)
entry_titulo.grid(row=0, column=1, columnspan=2)

btn_autor = tk.Button(frame, text="Seleccionar Autor", command=seleccionar_autor)
btn_autor.grid(row=1, column=0, pady=5)
lbl_autor = tk.Label(frame, text="Autor seleccionado: Ninguno")
lbl_autor.grid(row=1, column=1, columnspan=2, sticky="w")

btn_editorial = tk.Button(frame, text="Seleccionar Editorial", command=seleccionar_editorial)
btn_editorial.grid(row=2, column=0, pady=5)
lbl_editorial = tk.Label(frame, text="Editorial seleccionada: Ninguna")
lbl_editorial.grid(row=2, column=1, columnspan=2, sticky="w")

btn_agregar = tk.Button(frame, text="Agregar Libro", command=agregar_libro)
btn_agregar.grid(row=3, column=0, columnspan=3, pady=10)

tk.Label(root, text="Libros existentes:").pack()
lista_libros = tk.Listbox(root, width=80, height=10)
lista_libros.pack(padx=10, pady=10)

actualizar_lista_libros()
root.mainloop()
