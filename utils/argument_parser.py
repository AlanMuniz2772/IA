"""Command-line argument parsing utilities."""

import argparse


class ArgumentParser:
    """Wrapper around argparse to keep the interface dependency isolated."""

    @staticmethod
    def parse_args() -> argparse.Namespace:
        """Parse CLI arguments and return the resulting namespace."""
        parser = argparse.ArgumentParser(
            description="Selecciona la operacion a ejecutar: 1=jarras, 2=8-puzzle."
        )
        parser.add_argument(
            "operation",
            type=int,
            help="Identificador de la operacion a ejecutar.",
        )
        return parser.parse_args()
