import signal
import sys

def signal_handler(signum, frame):
    print("Señal recibida:", signum)
    print("Frame actual:", frame)
    print("Estamos en el archivo:", frame.f_code.co_filename)
    print("En la línea:", frame.f_lineno)
    sys.exit("Terminando el programa")

# Configurar el manejador de señales para señales de interrupción (como Ctrl+C)
signal.signal(signal.SIGINT, signal_handler)

# Simular un bucle infinito para demostrar
print("Ejecutando programa. Presiona Ctrl+C para detener.")
while True:
    pass
