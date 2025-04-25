from datetime import datetime

class Cita:
    def __init__(self, fecha, duracion, tema, estado='Pendiente'):
        # Asegurémonos de que la fecha esté en formato ISO 8601 antes de crear el objeto
        if isinstance(fecha, str):
            self.fecha = datetime.fromisoformat(fecha)  # Convierte de string a datetime
        elif isinstance(fecha, datetime):
            self.fecha = fecha  # Ya es un objeto datetime
        else:
            raise ValueError("La fecha debe ser una cadena en formato ISO 8601 o un objeto datetime")
        
        self.duracion = duracion
        self.tema = tema
        self.estado = estado
