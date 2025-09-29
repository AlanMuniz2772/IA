def main():
    x= 0
    

    jarra3G = Jarra(3)
    jarra4G = Jarra(4)

    print("estado inicial")
    print(jarra3G)
    print(jarra4G)
    
    count = 0
    while(jarra4G.cantidad != 2):
        aplicar_regla(jarra4G, jarra3G)
        count += 1
        print(f"iteracion {count}")

    print("estado final")
    print(jarra3G)
    print(jarra4G)

def aplicar_regla(x,y):
    reglas = [
        {  
            "condicion": x.cantidad<4,
            "accion": lambda: x.llenar()
        }, 
        {
            "condicion": y.cantidad<3,
            "accion":  lambda: y.llenar()
        },
        {
            "condicion": x.cantidad>0,
            "accion": lambda: x.vaciar()
        },
        {
            "condicion": y.cantidad>0,
            "accion": lambda: y.vaciar()
        },
    ]

    for regla in reglas:
        if regla["condicion"]:
            regla["accion"]()




class Jarra():
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.cantidad = 0

    def llenar(self):
        self.cantidad = self.capacidad

    def vaciar(self):
        self.cantidad = 0

    def verter(self, otra_jarra):
        espacio_disponible = otra_jarra.capacidad - otra_jarra.cantidad
        cantidad_a_verter = min(self.cantidad, espacio_disponible)
        self.cantidad -= cantidad_a_verter
        otra_jarra.cantidad += cantidad_a_verter

    def __str__(self):
        return f"Jarra(capacidad={self.capacidad}, cantidad={self.cantidad})"

if __name__ == "__main__":
    main()    