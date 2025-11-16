"""
EventFlow - Sistema de Gestión de Eventos
Versión inicial con deuda técnica intencional para demostración
"""
import sqlite3
import json
from datetime import datetime

class EventManager:
    def __init__(self):
        self.conn = sqlite3.connect('events.db')
        self.create_tables()
    
    def create_tables(self):
        """Crear tablas de la base de datos"""
        cursor = self.conn.cursor()
        
        # DEUDA TÉCNICA: Falta manejo de errores y transacciones
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS events (
                id INTEGER PRIMARY KEY,
                name TEXT,
                date TEXT,
                capacity INTEGER
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tickets (
                id INTEGER PRIMARY KEY,
                event_id INTEGER,
                user_email TEXT,
                quantity INTEGER
            )
        ''')
        self.conn.commit()
    
    def create_event(self, name, date, capacity):
        """Crear un nuevo evento"""
        # DEUDA TÉCNICA: No hay validación de datos
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO events (name, date, capacity) VALUES (?, ?, ?)",
            (name, date, capacity)
        )
        self.conn.commit()
        return cursor.lastrowid
    
    def get_events(self):
        """Obtener todos los eventos"""
        # DEUDA TÉCNICA: No hay paginación para muchos registros
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM events")
        return cursor.fetchall()
    
    def buy_ticket(self, event_id, user_email, quantity):
        """Comprar entradas para un evento"""
        # DEUDA TÉCNICA: Lógica compleja sin separación de responsabilidades
        cursor = self.conn.cursor()
        
        # Verificar disponibilidad
        cursor.execute("SELECT capacity FROM events WHERE id = ?", (event_id,))
        event = cursor.fetchone()
        
        if not event:
            return {"error": "Evento no encontrado"}
        
        capacity = event[0]
        
        # Contar entradas vendidas
        cursor.execute("SELECT SUM(quantity) FROM tickets WHERE event_id = ?", (event_id,))
        sold = cursor.fetchone()[0] or 0
        
        if sold + quantity > capacity:
            return {"error": "No hay suficiente capacidad"}
        
        # DEUDA TÉCNICA: No hay transacción atómica
        cursor.execute(
            "INSERT INTO tickets (event_id, user_email, quantity) VALUES (?, ?, ?)",
            (event_id, user_email, quantity)
        )
        self.conn.commit()
        
        return {"success": True, "tickets": quantity}

# DEUDA TÉCNICA: Código duplicado
def print_events(events):
    for event in events:
        print(f"Evento: {event[1]}, Fecha: {event[2]}")
