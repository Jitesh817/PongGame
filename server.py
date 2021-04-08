import socket
import os
from _thread import *

n = 2

# create a socket object
serversocket = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

print("server host name: ", host)

port = 9999
clientSocketArray = []

# bind to the port
serversocket.bind((host, port))

# queue up to 5 requests
serversocket.listen(5)

def sendToAll(msg):
    for i in range(0, n):
        print(clientSocketArray[i])
        clientSocketArray[i].send((msg + " recieved").encode("ascii"))


def multi_threaded_client(connection, i):
    print("thread %d" % i)
    while True:
        data = connection.recv(2048)
        response = 'Server message: ' + data.decode('ascii')
        print("%s from %d" % (response, i+1))
        if not data:
            continue
        sendToAll(data.decode('ascii'))
    connection.close()

for i in range(0, n):
    clientsocket, addr = serversocket.accept()
    start_new_thread(multi_threaded_client, (clientsocket, i, ))
    clientSocketArray.append(clientsocket)

while True:
    continue


print(clientSocketArray)
