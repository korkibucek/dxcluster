#!/usr/bin/python3

import socket
import sys

HOST = ''
PORT = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.listen(10)
conn, addr = s.accept()
print('Connected with ' + addr[0] + ':' + str(addr[1]))
