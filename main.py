from utils.argument_parser import ArgumentParser
from interfaces.interfaces import Jarras_Interface

def main():
    args = ArgumentParser.parse_args()
    operation = args.operation
    isJson = False

    if operation == 1:
        interfaz = Jarras_Interface(isJson)
    elif operation == 2:
        print("Operación 2 seleccionada (no implementada).")
        return
    else:
        print("Operación no válida. Usa 1 o 2.")
        return
    interfaz.ejecutar()


if __name__ == "__main__":
    main()
        