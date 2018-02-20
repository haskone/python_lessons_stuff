import time
import random
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 12347

s.connect((host, port))
s.send(f"{random.random()}".encode())

data = s.recv(1024).decode()
print(f"Got {data}, close the connection")
s.close()