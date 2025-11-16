# DEUDA TÉCNICA: Código duplicado
def print_events(events):
    for event in events:
        print(f"Evento: {event[1]}, Fecha: {event[2]}")

# === SECURITY HOTSPOTS PARA SONARCLOUD ===

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
