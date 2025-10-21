"""User interfaces for the supported problem solvers."""

from controllers.jarras_controller import JarrasController
from controllers.puzle_controller import PuzzleController, PuzzleResult


class Interfaces:
    """Base class for the different console interfaces."""

    def __init__(self, isJson: bool = False) -> None:
        self.isJson = isJson


class Jarras_Interface(Interfaces):
    """Console interface for the water jugs problem."""

    def __init__(self, isJson: bool = False) -> None:
        super().__init__(isJson)
        self.jarras_controller = JarrasController()

    def ejecutar(self) -> None:
        """Run the automatic rule application until the goal is reached."""
        while self.jarras_controller.jarra4G != 2:
            result = self.jarras_controller.aplicar_regla()
            print("----------------------------------------------------")
            print(f"iteracion {self.jarras_controller.count}")
            print(f"Regla aplicada: {result[2]}")
            print(
                f"Jarra 4G: {self.jarras_controller.jarra4G}, "
                f"Jarra 3G: {self.jarras_controller.jarra3G}"
            )

        print(
            "\n!Objetivo alcanzado! La jarra de 4 litros tiene exactamente 2 litros."
        )


class Puzle_Interface(Interfaces):
    """Console interface for the 8-puzzle solver."""

    def __init__(self, isJson: bool = False) -> None:
        super().__init__(isJson)
        self.controller = PuzzleController()

    def ejecutar(self) -> None:
        """Prompt the user for puzzle configurations and launch the solver."""
        print("Resolviendo el 8-puzzle utilizando A*.")
        initial = self._solicitar_estado(
            (
                "Ingresa el estado inicial (9 numeros, usa 0 para el espacio en blanco). "
            ),
        )
        goal = self._solicitar_estado(
            "Ingresa el estado meta.",
        )

        resultado = self.controller.resolver(initial, goal)
        self._imprimir_resultados(resultado)

    def _solicitar_estado(self, mensaje: str) -> tuple[int, ...]:
        """Read a puzzle state from the user or fall back to the provided default."""
        while True:
            respuesta = input(mensaje).strip()
            if not respuesta:
                raise ValueError("Se requiere una entrada valida.")
            try:
                valores = tuple(
                    int(valor) for valor in respuesta.replace(",", " ").split()
                )
                if len(valores) != 9:
                    raise ValueError
                return valores
            except ValueError:
                print(
                    "Entrada invalida. Debes proporcionar exactamente 9 numeros separados por espacios."
                )

    def _imprimir_resultados(self, resultado: PuzzleResult) -> None:
        """Display the resulting path and basic statistics."""
        print("\nSolucion encontrada!\n")
        for indice, estado in enumerate(resultado.path):
            print(f"Paso {indice}:")
            print(estado.pretty())
            print("-" * 20)

        print(f"Nodos explorados: {resultado.explored_nodes}")
        print(f"Nodos generados: {resultado.generated_nodes}")
        print(f"Profundidad de la solucion: {resultado.depth}")
