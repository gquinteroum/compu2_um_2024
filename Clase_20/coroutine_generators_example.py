
import time

# Definir una coroutine rústica usando un generador
def coroutine():
    print("Starting coroutine")
    received = yield "First pause"
    print(f"Received in coroutine: {received}")
    received = yield "Second pause"
    print(f"Received in coroutine: {received}")
    yield "Ending coroutine"

# Scheduler que controla la ejecución del generador
def scheduler(coroutine):
    gen = coroutine()
    try:
        # Ejecutar y pausar la primera parte de la coroutine
        result = next(gen)
        print(f"Coroutine yielded: {result}")
        
        # Simular espera
        time.sleep(1)
        
        # Reanudar la coroutine enviando un valor
        result = gen.send("Data sent after first pause")
        print(f"Coroutine yielded: {result}")
        
        # Simular otra espera
        time.sleep(1)
        
        # Completar la coroutine enviando otro valor
        result = gen.send("Data sent after second pause")
        print(f"Coroutine yielded: {result}")
        
    except StopIteration:
        print("Coroutine finished")

# Ejecutar el scheduler con la coroutine
scheduler(coroutine)
