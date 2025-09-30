import random

def aplicar_regla(x, y):
    reglas = [
        {
            "nombre": "Llenar jarra de 4 litros",
            "condicion": x < 4,
            "accion": lambda: (4, y)
        },
        {
            "nombre": "Llenar jarra de 3 litros",
            "condicion": y < 3,
            "accion": lambda: (x, 3)
        },
        {
            "nombre": "Vaciar jarra de 4 litros",
            "condicion": x > 0,
            "accion": lambda: (0, y)
        },
        {
            "nombre": "Vaciar jarra de 3 litros",
            "condicion": y > 0,
            "accion": lambda: (x, 0)
        },
        {
            "nombre": "Verter de 4L a 3L hasta llenar",
            "condicion": x > 0 and y < 3 and x + y >= 3,
            "accion": lambda: (x - (3 - y), 3)
        },
        {
            "nombre": "Verter de 3L a 4L hasta llenar",
            "condicion": x < 4 and y > 0 and x + y >= 4,
            "accion": lambda: (4, y - (4 - x))
        },
        {
            "nombre": "Verter todo de 4L a 3L",
            "condicion": x > 0 and y < 3 and x + y <= 3,
            "accion": lambda: (0, x + y)
        },
        {
            "nombre": "Verter todo de 3L a 4L",
            "condicion": x < 4 and y > 0 and x + y <= 4,
            "accion": lambda: (x + y, 0)
        },
    ]

    reglas_validas = [regla for regla in reglas if regla["condicion"]]
    if reglas_validas:
        regla_elegida = random.choice(reglas_validas)
        print(f"Aplicando regla: {regla_elegida['nombre']}")
        x, y = regla_elegida["accion"]()

    return x, y

def  main():
    jarra3G = 0
    jarra4G = 0
        
    count = 0
    while(jarra4G != 2):
        jarra4G, jarra3G = aplicar_regla(jarra4G, jarra3G)
        count += 1
        print("----------------------------------------------------")
        print(f"iteracion {count}")
        print(f"Jarra 4G: {jarra4G}, Jarra 3G: {jarra3G}")

    return f"Objetivo alcanzado: Jarra 4G tiene 2 litros en {count} movimientos."


