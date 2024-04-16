import os

fifo_path = '/tmp/my_fifo'

print("Opening FIFO...")
with open(fifo_path, 'r') as fifo:
    print("FIFO opened for reading.")
    while True:
        message = fifo.readline().strip()
        if message == "":
            print("No more messages. Exiting.")
            break
        print(f'Received: {message}')
