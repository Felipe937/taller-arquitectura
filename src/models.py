"""
Modelos de datos para EventFlow
DEUDA TÉCNICA: Falta estructura adecuada de modelos
"""

# DEUDA TÉCNICA: Clases sin métodos, solo datos
class Event:
    def __init__(self, name, date, capacity):
        self.name = name
        self.date = date
        self.capacity = capacity

class Ticket:
    def __init__(self, event_id, user_email, quantity):
        self.event_id = event_id
        self.user_email = user_email
        self.quantity = quantity
