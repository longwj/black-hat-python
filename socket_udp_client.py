#!/usr/bin/python

import socket
import sys

HOST = str(sys.argv[1])
PORT = int(sys.argv[2])
CONTENT = str(sys.argv[3])
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
client.sendto(CONTENT,(HOST,PORT))

data,addr = client.recvfrom(4096)

print data
