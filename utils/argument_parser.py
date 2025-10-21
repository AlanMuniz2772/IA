"""Utilidades para analizar argumentos de linea de comandos."""

import argparse


class ArgumentParser:
    """Envoltura de argparse para aislar la dependencia en la interfaz."""

    @staticmethod
    def parse_args() -> argparse.Namespace:
        """Analiza los argumentos de la CLI y devuelve el espacio de nombre."""
        parser = argparse.ArgumentParser(
            description="Selecciona la operacion a ejecutar: 1=jarras, 2=8-puzzle."
        )
        parser.add_argument(
            "operation",
            type=int,
            help="Identificador de la operacion a ejecutar.",
        )
        return parser.parse_args()
