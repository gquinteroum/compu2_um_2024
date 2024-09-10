import socketserver
import multiprocessing as mp
import sys
import signal
import os

class ForkingTCPRequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print(f"Child process PID: {os.getpid()}")
        
        data = self.request.recv(1024).strip()

        print(f"Received message: {data.decode('utf-8')}")
        self.request.sendall(bytes(f"Echo: {data.decode('utf-8')}", "utf-8"))

class ForkingTCPServer(socketserver.ForkingMixIn, socketserver.TCPServer):
    allow_reuse_address = True

def signal_handler(signum, frame):
    print("Shutting down server...")
    server.shutdown()
    server.server_close()
    sys.exit(0)

if __name__ == "__main__":
    HOST, PORT = "localhost", 7373
    
    # Configurar el manejador de señales
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    
    server = ForkingTCPServer((HOST, PORT), ForkingTCPRequestHandler)
    print(f"Main process PID: {os.getpid()}")
    
    try:
        print(f"Server started on {HOST}:{PORT}")
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        print("Server is shutting down")
        server.shutdown()
        server.server_close()
