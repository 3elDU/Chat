from libraries import Server
import socket

if __name__ == '__main__':
    ip = socket.gethostbyname(socket.gethostname())
    port = 25535
    print(ip, port)
    Server.Main(ip, port)
