from ejercicios.jarras import main as jarras

def main():
    resultado = jarras()
    print(resultado)
    input("Presiona Enter para salir...")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\nError: {e}")
        input("\nPresiona Enter para salir...")