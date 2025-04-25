# Archivo: main.py

import tkinter as tk
from interfaz.ventana_principal import AplicacionPrincipal

if __name__ == "__main__":
    raiz = tk.Tk()
    app = AplicacionPrincipal(raiz)
    raiz.mainloop()
