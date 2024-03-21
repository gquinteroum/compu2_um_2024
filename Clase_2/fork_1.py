import os
import time

def main():
    print(f"Proceso padre PID: {os.getpid()}")

    pid = os.fork()
    print('LINEA 7:', pid)
    if pid == 0:
        # Código ejecutado por el proceso hijo
        print(f"Este es el proceso hijo, PID: {os.getpid()}")
        time.sleep(10)
        print('Termina el hijo')
    elif pid > 0:
        # Código ejecutado por el proceso padre
        print(f"Este es el proceso padre, PID todavía: {os.getpid()}")
        os.wait()  # El padre espera a que el hijo termine
        print('Termina el padre')
    else:
        # fork falló
        print("fork falló")


if __name__ == "__main__":
    main()
