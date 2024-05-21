import mmap
import os

# Abre el archivo en modo lectura y escritura
with open("/tmp/memoria_compartida", "r+b") as f:
    # Mapea el archivo en memoria
    mem = mmap.mmap(f.fileno(), 100)

    # Lee desde la memoria
    mem.seek(0)
    print("Mensaje del proceso 1:", mem.readline().decode())

    # Cierra el mapa de memoria
    mem.close()

