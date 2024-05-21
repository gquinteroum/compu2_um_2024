import mmap
import os
import tempfile

# Crea un archivo temporal
temp = tempfile.NamedTemporaryFile()

# Define el tamaño del archivo mapeado
size = 100  # en bytes

# Trunca el archivo al tamaño deseado
temp.truncate(size)

# Mapea el archivo en memoria
mem = mmap.mmap(temp.fileno(), size, access=mmap.ACCESS_WRITE)

# Aquí podrías lanzar los procesos no relacionados. Esto es un ejemplo con fork,
# pero en un escenario real podrías lanzar procesos independientes que abran el mismo archivo.
pid = os.fork()

if pid == 0:
    # Proceso hijo
    mem.write(b'Hola desde el hijo\n')
    mem.seek(0)  # Mueve el cursor al inicio para leer
    print('Proceso hijo lee:', mem.readline().decode())
    mem.close()
    os._exit(0)  # Salir del hijo

# Espera a que el hijo termine
os.wait()

# El proceso padre continúa
mem.seek(0)  # Asegúrate de mover el cursor al inicio
print('Proceso padre lee:', mem.readline().decode())
mem.close()

# Cierra el archivo temporal
temp.close()

