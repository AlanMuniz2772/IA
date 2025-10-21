"""Controller for the classic water jugs problem."""

from models.jarra import Jarras


class JarrasController:
    """Encapsulate the rule-based resolution of the water jugs setup."""

    def __init__(self) -> None:
        self.jarras = Jarras()
        self.jarra3G = 0
        self.jarra4G = 0
        self.count = 0
        self.result = {}

    def aplicar_regla(self):
        """Apply one random valid rule and return the resulting state."""
        regla_elegida = self.jarras.get_regla(self.jarra4G, self.jarra3G)
        if regla_elegida:
            self.jarra4G, self.jarra3G = regla_elegida["accion"](
                self.jarra4G, self.jarra3G
            )
            self.count += 1
            return (
                self.jarra4G,
                self.jarra3G,
                regla_elegida["nombre"],
                self.count,
            )
        raise Exception("No hay reglas aplicables.")
