from controllers.jarras_controller import JarrasController

class interfaces:
    def __init__(self, isJson=False):
        self.isJson = isJson
        pass

class Jarras_Interface(interfaces):
    def __init__(self, isJson=False):
        super().__init__(isJson)
        self.jarras_controller = JarrasController()

    def ejecutar(self):
        while(self.jarras_controller.jarra4G != 2):
            result = self.jarras_controller.aplicar_regla()
            print("----------------------------------------------------")
            print(f"iteracion {self.jarras_controller.count}")
            print(f"Regla aplicada: {result[2]}")
            print(f"Jarra 4G: {self.jarras_controller.jarra4G}, Jarra 3G: {self.jarras_controller.jarra3G}")

        print("\n¡Objetivo alcanzado! La jarra de 4 litros tiene exactamente 2 litros.")


class puzle_Interface(interfaces):
    def __init__(self, isJson=False):
        super().__init__(isJson)
        pass

    def ejecutar(self):
        print("Interfaz del puzle no implementada aún.")