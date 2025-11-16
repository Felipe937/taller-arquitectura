"""
Tests para EventFlow - DEUDA TÉCNICA: Cobertura insuficiente
"""
import pytest
import os
from app import EventManager

class TestEventManager:
    def setup_method(self):
        """Configuración antes de cada test"""
        self.manager = EventManager()
    
    def test_create_event(self):
        """Test crear evento"""
        event_id = self.manager.create_event("Concierto", "2024-01-01", 100)
        assert event_id is not None
    
    def test_get_events(self):
        """Test obtener eventos"""
        self.manager.create_event("Concierto", "2024-01-01", 100)
        events = self.manager.get_events()
        assert len(events) > 0
    
    # DEUDA TÉCNICA: Faltan tests para casos edge
