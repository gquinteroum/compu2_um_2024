import os
import time

fifo_path = '/tmp/my_fifo'

# Crear el FIFO si no existe
if not os.path.exists(fifo_path):
    os.mkfifo(fifo_path)

print("Opening FIFO...")
with open(fifo_path, 'w') as fifo:
    print("FIFO opened for writing.")
    for i in range(10):
        message = f'Message {i}'
        print(f'Sending: {message}')
        fifo.write(message + '\n')
        fifo.flush()  # Asegura que el mensaje se escriba inmediatamente
        time.sleep(1)  # Espera un segundo entre mensajes

print("Done writing messages.")
