from libraries import Storer
from libraries import NewClient
import socket


class Main:
    def __init__(self, IP: str, PORT: int):
        self.IP, self.PORT = IP, PORT

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((IP, PORT))
        self.s.listen(16384)
        self.s.setblocking(False)

        self.clients = Storer.ClientsStorer()
        self.threads = Storer.ThreadsStorer()
        self.id = 0

        while True:
            try:
                try:
                    conn, addr = self.s.accept()

                    self.clients.add(self.id, conn, addr)
                    self.id += 1

                    thread = NewClient.Main(conn, addr, self.id)
                    thread.start()

                    self.threads.add(self.id, thread)
                except socket.error:
                    pass

                try:
                    d = self.threads.getDataFromAll()

                    for key in self.threads.threads:
                        thread = self.threads.threads[key]

                        for data in d:
                            thread.setDataFromOthers(data)
                except socket.error:
                    pass
            except KeyboardInterrupt:
                print('Exiting...')
                self.threads.stopall()
                exit()
