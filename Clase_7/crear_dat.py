# Abrir el archivo para escritura (el modo 'wb' es para escritura binaria)
with open('example.dat', 'wb') as f:
    # Escribir una cadena de texto convertida a bytes
    f.write(b'Initial data in the file that is long enough for the example.')

# Asegúrate de que el archivo tiene suficiente tamaño para los ejemplos de mmap

