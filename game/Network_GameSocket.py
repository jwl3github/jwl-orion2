import socket
import pickle
import time

class Network_GameSocket(object):

    def __init__(self, socket):
        self.socket      = socket
        self.buffer_size = 4096
        self.head_size   = 64

    def setsockopt(self, level, optname, value):
        self.socket.setsockopt(level, optname, value)

    def setblocking(self, flag):
        self.socket.setblocking(flag)

    def settimeout(self, value):
        self.socket.settimeout(value)

    def bind(self, address):
        self.socket.bind(address)

    def listen(self, backlog):
        self.socket.listen(backlog)

    def accept(self):
        self.socket.settimeout(0.5)
        client_socket, (client_host, client_port) = self.socket.accept()
        self.socket.settimeout(0)
        client_socket.setblocking(1)
        client_socket.settimeout(None)
        return Network_GameSocket(client_socket), (client_host, client_port)

    def connect(self, address):
        self.socket.connect(address)

    def close(self):
        self.socket.close()

    def recv_raw(self, data_size):
        data = ''
        buffer_size = self.buffer_size
        while data_size > 0:
            try:
                chunk = self.socket.recv(min(buffer_size, data_size))
                if not chunk:
                    break
            except socket.timeout:
                print 'recv_raw -- timeout'
                self.socket.settimeout(None)  #JWL: temp
                chunk = ''
            data += chunk
            data_size -= len(chunk)
        return data

    def recv(self):
        print 'gamesocket.recv'
        head_raw = self.recv_raw(self.head_size).rstrip()
        # return None if header is empty
        if not head_raw:
            return None
        head = pickle.loads(head_raw)
        return pickle.loads(self.recv_raw(head['data_size']))

    def compose_head(self, data_size):
        return pickle.dumps({
            'data_size':    data_size
        }).ljust(self.head_size)

    def send(self, data):
        data       = pickle.dumps(data)
        head       = self.compose_head(len(data))
        data       = head + data
        total_size = len(data)
        sent       = 0
        while sent < total_size:
            chunk_size = self.socket.send(data[sent:])
            sent = sent + chunk_size
