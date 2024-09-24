import socket
import sys
import os

def main():
    host = None  # Simboliza todas las interfaces disponibles
    port = 5000  # Puerto arbitrario no privilegiado

    # Obtiene información de dirección para IPv4 e IPv6
    for res in socket.getaddrinfo(host, port, socket.AF_UNSPEC, socket.SOCK_STREAM, 0, socket.AI_PASSIVE):
        af, socktype, proto, canonname, sa = res
        try:
            pid = os.fork()
            if pid == 0:
                print(f'Proceso hijo {os.getpid()}')
                s = socket.socket(af, socktype, proto)
                s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
                s.bind(sa)
                s.listen(1)
                print(f'Servidor escuchando en {sa}')
                while True:
                    conn, addr = s.accept()
                    with conn:
                        if res[0] == socket.AF_INET6:
                            print(f'Conectado usando IPv6 desde {addr}')
                        elif res[0] == socket.AF_INET:
                            print(f'Conectado usando IPv4 desde {addr}')
                        conn.sendall(b'Hello, client!')
                        print(f'Enviando saludo a {addr}')
                        conn.close()
                sys.exit(0)
        except OSError as e:
            print(f'Error al crear proceso hijo: {e}')
        except Exception as e:
            print(f'Error general: {e}')

if __name__ == '__main__':
    main()
    # Espera a que los procesos hijos terminen
    while True:
        try:
            pid, status = os.wait()
            print(f'Proceso {pid} terminado con estado {status}')
        except ChildProcessError:
            break
    print('Proceso padre finalizando')
