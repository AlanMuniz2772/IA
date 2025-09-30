Proyecto IA casta

python -m venv venv
venv\Scripts\activate

# instalar compilador
pip install nuitka


# crear exe
nuitka --onefile main.py


# Eliminar archivos anteriores
rmdir /s /q build dist
del main.spec

# Luego compilar
pyinstaller --onefile main.py