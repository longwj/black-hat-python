#!/usr/bin/python

import socket
import sys
import pdb

HOST = str(sys.argv[1])
PORT = int(sys.argv[2])

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((HOST,PORT))

#pdb.set_trace()
request = "GET / HTTP/1.1 \r\nHost: %s\r\n\r\n" %(HOST,)
client.send(request)
response = client.recv(4096)

print response
