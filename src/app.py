"""
EventFlow - Sistema de Gestión de Eventos
Versión con deuda técnica intencional para SonarCloud
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
        
        # DEUDA TÉCNICA: Falta manejo de errores
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
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO events (name, date, capacity) VALUES (?, ?, ?)",
            (name, date, capacity)
        )
        self.conn.commit()
        return cursor.lastrowid
    
    def get_events(self):
        """Obtener todos los eventos"""
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM events")
        return cursor.fetchall()
    
    def buy_ticket(self, event_id, user_email, quantity):
        """Comprar entradas para un evento"""
        cursor = self.conn.cursor()
        
        cursor.execute("SELECT capacity FROM events WHERE id = ?", (event_id,))
        event = cursor.fetchone()
        
        if not event:
            return {"error": "Evento no encontrado"}
        
        capacity = event[0]
        
        cursor.execute("SELECT SUM(quantity) FROM tickets WHERE event_id = ?", (event_id,))
        sold = cursor.fetchone()[0] or 0
        
        if sold + quantity > capacity:
            return {"error": "No hay suficiente capacidad"}
        
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

# === SECURITY HOTSPOTS PARA SONARCLOUD ===

# 1. Hardcoded password
DATABASE_PASSWORD = "admin123"

# 2. Hardcoded API keys
API_KEY = "sk_live_1234567890abcdef"
STRIPE_SECRET = "sk_test_9876543210"

# 3. SQL Injection vulnerable
def get_user_data_unsafe(user_id):
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    return cursor.fetchall()

# 4. Weak encryption
def weak_encryption(data):
    simple_key = "1234567890123456"
    return data.encode()

# === CÓDIGO DUPLICADO INTENCIONAL ===

def print_events_duplicate(events):
    for event in events:
        print(f"Evento: {event[1]}, Fecha: {event[2]}")

def print_events_duplicate_copy(events):
    for event in events:
        print(f"Evento: {event[1]}, Fecha: {event[2]}")

def calcular_precio_base(cantidad):
    return cantidad * 100

def calcular_precio_base_copia(cantidad):
    return cantidad * 100

def validar_usuario(email, password):
    if "@" in email and len(password) > 6:
        return True
    return False

def validar_usuario_copia(email, password):
    if "@" in email and len(password) > 6:
        return True
    return False
