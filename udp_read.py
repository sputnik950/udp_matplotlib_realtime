import socket
import sys
from contextlib import closing

class Udp_read():

    def __init__(self, port_in):

        self.bufsize = 4096
        self.port = int(port_in)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # with closing(self.sock):
        self.sock.bind(("", self.port))

    def read_udp(self):
        return self.sock.recv(self.bufsize)

        
