import os

def main():
    print("Ejecutando 'ls' para listar directorios...")

    # Reemplaza el proceso actual con 'ls'
    # Nota: Este código no se ejecutará más allá de este punto en el proceso actual
    os.execlp('ls', 'ls', '-l')

    # Esta línea no se ejecutará
    print("Esta línea no se mostrará.")

if __name__ == "__main__":
    main()
