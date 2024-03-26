"""
Ejemplo de código secuencial.
Las instrucciones se van ejecutando una detrás de la otra

NOTA DE CLASE: mientras se ejecuta correr ps fax|grep python
"""


import time
import os

print('INICIO')
print('PID: %d  --  PPID: %d' % (os.getpid(), os.getppid()))

for i in range(5, 0, -1):
  print(i)
  time.sleep(1)


print('\nFIN')
print('PID: %d  --  PPID: %d' % (os.getpid(), os.getppid()))
