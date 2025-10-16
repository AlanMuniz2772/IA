from models.jarra import Jarras

class JarrasController:
    def __init__(self):
        self.jarras = Jarras()
        self.jarra3G = 0
        self.jarra4G = 0
        self.count = 0
        self.result = {

        }
    
    def aplicar_regla(self):
        regla_elegida = self.jarras.get_regla(self.jarra4G, self.jarra3G)
        if regla_elegida:
            self.jarra4G, self.jarra3G = regla_elegida["accion"](self.jarra4G, self.jarra3G)
            self.count += 1
            return self.jarra4G, self.jarra3G, regla_elegida["nombre"], self.count
        else:
            raise Exception("No hay reglas aplicables.")
        