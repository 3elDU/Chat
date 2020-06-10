from threading import Thread
import socket


class Main(Thread):
    def __init__(self, c: socket.socket, a: tuple, n: int):
        Thread.__init__(self)

        self.c, self.a = c, a
        self.id = n

        self.alive = True
        self.data = ''
        self.others = ''

    def getSended(self):
        nd = self.data
        self.data = ''
        return nd

    def setDataFromOthers(self, data):
        self.others += data

    def run(self):
        print("New Client Thread: ", self.id)

        while self.alive:
            try:
                d = self.c.recv(131072).decode('utf-8')
                print(self.id, ':', d)
                if d == 'stop':
                    print(self.id, 'Stopping thread')
                    self.alive = False
                else:
                    self.data += d
            except socket.error:
                pass

            try:
                self.c.send(self.others.encode('utf-8'))
                self.others = ''
            except socket.error:
                pass

        print(self.id, 'Thread stopped')

        exit()

    def stop(self):
        self.alive = False
