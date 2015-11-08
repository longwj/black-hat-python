#!/usr/bin/python
import pdb
import socket
import threading

pdb.set_trace()
BIND_IP = "0.0.0.0"
BIND_PORT = 9999

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((BIND_IP,BIND_PORT))
server.listen(5)

print "[*] Listen on %s:%d" % (BIND_IP,BIND_PORT)

def handle_client(client_socket):
    request = client_socket.recv(1024)
    print "[*] Received: %s" % (request)
    client_socket.send("ACK")
    client_socket.close()

while True:
    client,addr = server.accept()
    print "[*] Accepted connection from: %s:%d" %(addr[0],addr[1])
    client_handler = threading.Thread(target=handle_client,args=(client,))
    client_handler.start()

