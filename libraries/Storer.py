
class ClientsStorer:
    def __init__(self):
        self.clients = []

    def add(self, n, conn, addr):
        self.clients.append([n, conn, addr])

    def remove(self, n):
        for c in self.clients:
            if c[0] == n:
                self.clients.remove(c)

    def checkExisting(self, n):
        for client in self.clients:
            if client[0] == n:
                return True
        return False


class ThreadsStorer:
    def __init__(self):
        self.threads = {}

    def add(self, index, thread):
        self.threads[index] = thread

    def get(self, index):
        if index in self.threads:
            return self.threads[index]

    def stopall(self):
        for key in self.threads:
            self.threads[key].stop()

    def getDataFromAll(self):
        alls = []
        for key in self.threads:
            alls.append(self.threads[key].getSended())
        return alls

    def addDataForAll(self, data):
        for key in self.threads:
            self.threads[key].setDataFromOthers(data)
