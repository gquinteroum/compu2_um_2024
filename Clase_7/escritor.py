import mmap
import os

# Abre el archivo para respaldo de memoria compartida
with open("/tmp/memoria_compartida", "wb") as f:
    # Define el tamaño del archivo mapeado
    f.truncate(100)

# Abre el archivo en modo lectura y escritura
with open("/tmp/memoria_compartida", "r+b") as f:
    # Mapea el archivo en memoria
    mem = mmap.mmap(f.fileno(), 100)

    # Escribe en la memoria
    mem.write(b"Hola desde el proceso 1")

    # No cierra el mapa de memoria para permitir el acceso en otro proceso
    mem.close()

