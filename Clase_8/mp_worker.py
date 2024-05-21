"""
Ejercicio: modificar este código (usando los comandos de bash aprendidos) para demostrar que existe paralelismo real.
"""

import multiprocessing

def worker(num):
    """Función que será ejecutada por cada proceso."""
    print(f'Worker: {num}')

if __name__ == '__main__':
    # Lista para mantener los procesos
    processes = []

    # Crear procesos
    for i in range(9):  # Crear 5 procesos
        p = multiprocessing.Process(target=worker, args=(i,))
        processes.append(p)
        p.start()

    # Esperar a que todos los procesos terminen
    for p in processes:
        p.join()

    print("Procesamiento completado.")
