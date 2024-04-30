#### Ejemplo 1: Crear y Utilizar Memoria Compartida
from multiprocessing import Process, Value, Array

def f(n, a):
    n.value = 3.1415927
    for i in range(len(a)):
        a[i] = -a[i]

if __name__ == '__main__':
    num = Value('d', 0.0)  # 'd' indica un valor double
    arr = Array('i', range(10))  # 'i' indica un array de enteros

    p = Process(target=f, args=(num, arr))
    p.start()
    p.join()

    print(num.value)
    print(arr[:])
