# DEUDA TÉCNICA: Código duplicado
def print_events(events):
    for event in events:
        print(f"Evento: {event[1]}, Fecha: {event[2]}")

# === SECURITY HOTSPOTS PARA SONARCLOUD - VERSIÓN CORREGIDA ===

# 1. Hardcoded password (Security Hotspot)
DATABASE_PASSWORD = "admin123"  # Cambiar por variable de entorno

# 2. SQL Injection potential (Security Hotspot)
def get_user_data_unsafe(user_id):
    import sqlite3
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    
    # ❌ VULNERABLE: SQL Injection
    cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")
    
    # ✅ SECURE: Parameterized query  
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    
    return cursor.fetchall()

# 3. Weak cryptography (Security Hotspot)
def weak_encryption(data):
    # ❌ VULNERABLE: Weak encryption
    simple_key = "1234567890123456"  # Should be generated securely
    return data.encode()  # No real encryption

# 4. Hardcoded API keys (Security Hotspot)
API_KEY = "sk_live_1234567890abcdef"
STRIPE_SECRET = "sk_test_9876543210"

# 5. More code duplication for SonarCloud detection
def print_events_duplicate(events):
    for event in events:
        print(f"Evento: {event[1]}, Fecha: {event[2]}")

def print_events_duplicate_copy(events):
    for event in events:
        print(f"Evento: {event[1]}, Fecha: {event[2]}")

# === MÁS CÓDIGO DUPLICADO PARA SONARCLOUD ===

# Duplicación intencional 1
def calcular_precio_base(cantidad):
    precio = cantidad * 100
    return precio

def calcular_precio_base_copia(cantidad):
    precio = cantidad * 100
    return precio

# Duplicación intencional 2  
def validar_usuario(email, password):
    if "@" in email and len(password) > 6:
        return True
    return False

def validar_usuario_copia(email, password):
    if "@" in email and len(password) > 6:
        return True
    return False

# Duplicación intencional 3
def formatear_fecha(fecha_str):
    partes = fecha_str.split("-")
    return f"{partes[2]}/{partes[1]}/{partes[0]}"

def formatear_fecha_copia(fecha_str):
    partes = fecha_str.split("-")
    return f"{partes[2]}/{partes[1]}/{partes[0]}"

# Método largo para complexity
def proceso_venta_muy_largo(usuario_id, evento_id, cantidad):
    # Paso 1: Validar usuario
    usuario = obtener_usuario(usuario_id)
    if not usuario:
        return "Error: Usuario no existe"
    
    # Paso 2: Validar evento
    evento = obtener_evento(evento_id)
    if not evento:
        return "Error: Evento no existe"
    
    # Paso 3: Validar disponibilidad
    if cantidad > evento.capacidad_disponible:
        return "Error: No hay suficiente capacidad"
    
    # Paso 4: Calcular precio
    precio_base = cantidad * evento.precio
    iva = precio_base * 0.16
    total = precio_base + iva
    
    # Paso 5: Crear orden
    orden_id = crear_orden(usuario_id, evento_id, cantidad, total)
    
    # Paso 6: Actualizar inventario
    actualizar_inventario(evento_id, cantidad)
    
    # Paso 7: Enviar confirmación
    enviar_email_confirmacion(usuario.email, orden_id)
    
    return f"Venta exitosa. Orden: {orden_id}"

# Métodos dummy para que no falle
def obtener_usuario(id):
    return {"id": id, "email": "test@test.com"}

def obtener_evento(id):
    return {"id": id, "precio": 100, "capacidad_disponible": 50}

def crear_orden(usuario_id, evento_id, cantidad, total):
    return "ORD-12345"

def actualizar_inventario(evento_id, cantidad):
    pass

def enviar_email_confirmacion(email, orden_id):
    pass
