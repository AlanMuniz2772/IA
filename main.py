"""Punto de entrada para las interfaces de linea de comandos."""

from utils.argument_parser import ArgumentParser
from interfaces.interfaces import Jarras_Interface, Puzle_Interface


def main() -> None:
    """Dirige la ejecucion hacia la interfaz del problema elegido."""
    args = ArgumentParser.parse_args()
    operation = args.operation
    is_json = False

    if operation == 1:
        interfaz = Jarras_Interface(is_json)
    elif operation == 2:
        interfaz = Puzle_Interface(is_json)
    else:
        print("Operacion no valida. Usa 1 o 2.")
        return

    interfaz.ejecutar()


if __name__ == "__main__":
    main()
