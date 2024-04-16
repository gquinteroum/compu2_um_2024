import os

fifoA_path = '/tmp/fifoA'
fifoB_path = '/tmp/fifoB'

# Abrir FIFOs
with open(fifoA_path, 'r') as fifoA, open(fifoB_path, 'w') as fifoB:
    while True:
        # Recibir mensaje de process1
        message = fifoA.readline().strip()
        if message:
            print(f"Received from process1: {message}")

        # Responder a process1
        fifoB.write('Hello from process2\n')
        fifoB.flush()
        print("Sent to process1.")

