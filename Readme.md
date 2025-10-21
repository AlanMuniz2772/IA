# Proyecto IA

Solucion modular para ejercicios clasicos de Inteligencia Artificial siguiendo una arquitectura inspirada en SOLID. El proyecto incluye:

- **Jarras de agua**: aplicacion de reglas aleatorias hasta alcanzar un objetivo.
- **8-puzzle**: resolucion mediante busqueda A* sobre un grafo de estados.

## Estructura principal

- `controllers/`: orquestacion de cada problema (Jarras y 8-puzzle).
- `interfaces/`: interaccion con el usuario en modo consola.
- `models/`: modelos de dominio (`Nodo`, `Grafo`, `Jarras`, `PuzzleState`, heuristicas).
- `services/`: utilidades compartidas.
- `utils/`: utilidades de infraestructura (parser de argumentos).

Cada clase y funcion cuenta con docstrings que documentan su responsabilidad y facilitan el mantenimiento.

## Requisitos

- Python 3.10+ recomendado.
- (Opcional) Entorno virtual: `python -m venv venv` y `venv\Scripts\activate`.

## Ejecucion

```bash
python main.py <operacion>
```

Operaciones disponibles:

1. `1`: ejecuta el problema de las jarras de agua.
2. `2`: ejecuta el solucionador del 8-puzzle con A*.

## 8-puzzle con A*

1. Se solicitan los estados inicial y meta. Usa `0` para el espacio en blanco. Pulsa Enter para aceptar los ejemplos por defecto.
2. Se valida la solvencia del problema mediante el conteo de inversiones.
3. El controlador crea un `PuzzleGraph` alimentado por la heuristica seleccionada (Manhattan por defecto) y usa `Nodo` para almacenar g(n), h(n) y el padre del estado.
4. Durante la busqueda:
   - Cada estado extraido de la frontera se imprime con su coste acumulado.
   - Cada sucesor generado se muestra antes de anadirse a la cola de prioridad.
5. Al encontrar la meta, se reconstruye el camino y se imprimen todos los pasos junto con estadisticas basicas (nodos generados, explorados y profundidad).

### Heuristicas disponibles

- `manhattan`: suma de distancias Manhattan de cada ficha a su posicion meta.
- `misplaced`: numero de fichas fuera de lugar.
- `euclidean`: distancia euclidiana de cada ficha a su destino.

Puedes cambiar la heuristica instanciando `PuzzleController(heuristic="misplaced")` desde tu propio codigo.

## Construccion de ejecutables (opcional)

Para construir un ejecutable autonomo puedes usar Nuitka o PyInstaller. Recomendacion general:

```powershell
pip install nuitka pyinstaller

# Con Nuitka
nuitka --onefile main.py

# Con PyInstaller
pyinstaller --onefile main.py
```

Limpia artefactos previos antes de compilar:

```powershell
rmdir /s /q build dist
del main.spec
```
