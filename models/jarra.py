"""Modelo de dominio para el problema de las jarras de agua."""

from services.utils import random_choice


class Jarras:
    """Representa el conjunto de reglas del acertijo de las jarras."""

    def __init__(self) -> None:
        self.reglas = [
            {
                "nombre": "Llenar jarra de 4 litros",
                "condicion": lambda x, y: x < 4,
                "accion": lambda x, y: (4, y),
            },
            {
                "nombre": "Llenar jarra de 3 litros",
                "condicion": lambda x, y: y < 3,
                "accion": lambda x, y: (x, 3),
            },
            {
                "nombre": "Vaciar jarra de 4 litros",
                "condicion": lambda x, y: x > 0,
                "accion": lambda x, y: (0, y),
            },
            {
                "nombre": "Vaciar jarra de 3 litros",
                "condicion": lambda x, y: y > 0,
                "accion": lambda x, y: (x, 0),
            },
            {
                "nombre": "Verter de 4L a 3L hasta llenar",
                "condicion": lambda x, y: x > 0 and y < 3 and x + y >= 3,
                "accion": lambda x, y: (x - (3 - y), 3),
            },
            {
                "nombre": "Verter de 3L a 4L hasta llenar",
                "condicion": lambda x, y: x < 4 and y > 0 and x + y >= 4,
                "accion": lambda x, y: (4, y - (4 - x)),
            },
            {
                "nombre": "Verter todo de 4L a 3L",
                "condicion": lambda x, y: x > 0 and y < 3 and x + y <= 3,
                "accion": lambda x, y: (0, x + y),
            },
            {
                "nombre": "Verter todo de 3L a 4L",
                "condicion": lambda x, y: x < 4 and y > 0 and x + y <= 4,
                "accion": lambda x, y: (x + y, 0),
            },
        ]

    def get_regla(self, x, y):
        """Devuelve una regla aplicable al azar para el estado actual."""
        reglas_validas = [r for r in self.reglas if r["condicion"](x, y)]
        if not reglas_validas:
            return None
        return random_choice(reglas_validas)
