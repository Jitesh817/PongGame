import socket
import time
import pygame
import os
from _thread import *

pygame.init()

display_width = 1500
display_height = 750
paddleWidth = 7
paddleHeight = 100
boundary = (display_width * 0.015)+paddleWidth

gameDisplay = pygame.display.set_mode((display_width, display_height))
# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

print("client host name: ", host)

port = 9999

# connection to hostname on the port.
s.connect((host, port))

def printRecMsg():
    while True:
        print(s.recv(1024).decode("ascii"))

# Receive no more than 1024 bytes
count = 1

start_new_thread(printRecMsg , ())
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        if event.type == pygame.KEYDOWN:
            print("key is being pressed")
            msg = "message asdra"
            s.send(msg.encode("ascii"))


s.close()
