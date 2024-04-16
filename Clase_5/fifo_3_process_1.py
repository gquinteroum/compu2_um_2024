import os
import time

fifoA_path = '/tmp/fifoA'
fifoB_path = '/tmp/fifoB'

# Crear FIFOs si no existen
if not os.path.exists(fifoA_path):
    os.mkfifo(fifoA_path)
if not os.path.exists(fifoB_path):
    os.mkfifo(fifoB_path)

# Abrir FIFOs
with open(fifoA_path, 'w') as fifoA, open(fifoB_path, 'r') as fifoB:
    while True:
        # Enviar un mensaje a process2
        fifoA.write('Hello from process1\n')
        fifoA.flush()
        print("Sent to process2.")
        
        # Recibir respuesta de process2
        message = fifoB.readline().strip()
        if message:
            print(f"Received from process2: {message}")
        time.sleep(1)

