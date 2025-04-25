import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from collections import Counter
from datetime import datetime
from services.cita_service import obtener_citas_de_cliente

def mostrar_grafica_mensual(frame, nombre_cliente):
    citas = obtener_citas_de_cliente(nombre_cliente)
    if not citas:
        return

    # Contar citas por mes
    meses = [cita.fecha.strftime("%Y-%m") for cita in citas]
    conteo = Counter(meses)

    meses_ordenados = sorted(conteo.keys())
    cantidades = [conteo[mes] for mes in meses_ordenados]

    # Limpiar gráficos anteriores
    for widget in frame.winfo_children():
        if isinstance(widget, FigureCanvasTkAgg):
            widget.get_tk_widget().destroy()

    # Crear gráfico
    fig, ax = plt.subplots(figsize=(6, 3))
    ax.bar(meses_ordenados, cantidades, color="skyblue")
    ax.set_title(f"Citas por mes - {nombre_cliente}")
    ax.set_ylabel("Cantidad")
    ax.set_xlabel("Mes")

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(pady=10)
