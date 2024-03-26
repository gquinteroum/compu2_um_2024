import subprocess
import os
import time

# Crear un proceso hijo que termina inmediatamente
pid = os.fork()
if pid == 0:
    # Proceso hijo
    print("Este es el proceso hijo, terminando ahora.")
    os._exit(0)
else:
    # Proceso padre
    print(f"Este es el proceso padre, dejando al hijo {pid} como zombi.")
    time.sleep(20)  # Simular trabajo para dejar al hijo como zombi
    print("El proceso padre ha terminado, el hijo debería ser adoptado por init.")
    pid, es = os.wait()
    print(pid, es)
    time.sleep(10)
# Nota: Este código debe ser ejecutado en un entorno seguro, ya que crea un proceso zombi.

