import time
import random
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 12346

s.connect((host, port))
s.send(f"{random.random()}".encode())

while True:
    data = s.recv(1024).decode()
    if data == "OK":
        print("Got OK, close the connection")
        s.close()
        break
    else:
        print("Got wrong response: {data}, "
              "continue waiting")    