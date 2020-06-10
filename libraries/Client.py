import socket


class Main:
    def __init__(self, IP: str, PORT: int):
        self.IP, self.PORT = IP, PORT

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((IP, PORT))

        print('Connected to server.')

        self.messageLoop()

    def messageLoop(self):
        while True:
            try:
                try:
                    d = self.s.recv(131072).decode('utf-8')
                    print(d)

                    tosend = input('>>')

                    self.s.send(tosend.encode('utf-8'))
                except socket.error:
                    pass
            except KeyboardInterrupt:
                print('Exiting...')
                self.s.send(b'3elDU==exit')
                exit(0)
