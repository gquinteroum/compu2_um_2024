# COMPUTACIÓN II

## TP2

**Fecha de entrega: 12/11/2024**

---

### **Problema**

---

#### **A**

Se requiere procesar imágenes con Python, utilizando bibliotecas de procesamiento de imágenes. Las imágenes deben enviarse a un servidor HTTP que maneje las conexiones de forma asíncrona utilizando **asyncio**. El servidor debe procesar las imágenes convirtiéndolas a escala de grises sin bloquear el bucle de eventos. Es necesario implementar mecanismos de comunicación asíncrona entre tareas para que el servidor HTTP solicite el procesamiento de imágenes. El servidor debe esperar de manera asíncrona la finalización de la conversión y, una vez lista, enviar la imagen procesada al cliente antes de cerrar la conexión.

#### **B**

El servidor debe comunicarse con otro servidor en el mismo host. Este segundo servidor, implementado utilizando **multiprocessing** y **socketserver**, debe reducir el tamaño de la imagen según un factor de escala proporcionado por el primer servidor. La comunicación entre ambos servidores debe realizarse mediante sockets y manejarse en procesos separados.

#### **C**

Los servicios del segundo servidor (escalado de imágenes) deben ser accesibles desde el cliente a través del primer servidor, de manera que el cliente solo interactúe con el primer servidor y todas las operaciones se realicen de forma transparente.

---

### **Requerimientos**

- La aplicación debe contener como mínimo **3 funciones**.
- El servidor debe poder atender requerimientos **IPv4 e IPv6** indistintamente, utilizando **asyncio** para gestionar las conexiones.
- El segundo servidor debe utilizar **multiprocessing** y **socketserver** para manejar las solicitudes de escalado de imágenes.
- Debe procesar opciones con **getopt** (agregar una opción de ayuda) o con **argparse**.
- Debe manejar los errores de forma adecuada.
- El uso de **asyncio** y **multiprocessing** debe ser fundamental en la arquitectura de la aplicación, aprovechando sus capacidades para manejar operaciones de E/S de manera eficiente y concurrente.

---

### **Ejemplo de modo de uso**

```bash
$ ./tp2.py -h
usage: tp2.py [-h] -i IP -p PORT

Tp2 - procesa imágenes

Opciones:
  -h, --help            Muestra este mensaje de ayuda y sale
  -i IP, --ip IP        Dirección de escucha
  -p PORT, --port PORT  Puerto de escucha
```

---

### **Objetivos**

- Manejo de archivos (apertura, escritura y cierre).
- Creación y gestión de tareas asíncronas y procesos.
- Uso de mecanismos de **Inter Process Communication** utilizando sockets.
- Uso de mecanismos de sincronización basados en **asyncio** y **multiprocessing**.
- Implementación de sockets tanto asíncronos como en procesos separados para comunicaciones en red.

---

### **Referencias**

- **AsyncIO Documentation**: [https://docs.python.org/3/library/asyncio.html](https://docs.python.org/3/library/asyncio.html)
- **Multiprocessing Documentation**: [https://docs.python.org/3/library/multiprocessing.html](https://docs.python.org/3/library/multiprocessing.html)
- **SocketServer Documentation**: [https://docs.python.org/3/library/socketserver.html](https://docs.python.org/3/library/socketserver.html)
- **File Upload in HTML**: [RFC 1867](https://www.rfc-editor.org/rfc/rfc1867)

---

### **Bonus Track**

El primer servidor puede devolver al cliente inmediatamente un identificador de tarea. El cliente podrá usar ese identificador para preguntar si la tarea ya finalizó para descargar la imagen solo cuando esté listo el trabajo. 

---

### **Instrucciones Adicionales**

- **Estructura del Proyecto**: Organizar el código en módulos y paquetes de manera que sea fácil de mantener y entender. Se recomienda crear un paquete para el servidor asíncrono y otro para el servidor que utiliza multiprocessing.
- **Pruebas**: Es recomendable escribir pruebas unitarias para las funciones críticas de la aplicación. Esto ayudará a asegurar que cada componente funciona correctamente.
- **Documentación**: Comentar el código y proporcionar documentación sobre cómo configurar y ejecutar la aplicación, así como cualquier dependencia necesaria.

---

**Entrega**: Subir el proyecto al repositorio personal dentro de una carpeta cuyo nombre debe ser TP2 antes de la fecha de entrega.

---

¡Buena suerte!

---

