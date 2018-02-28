import time
import random
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 12346

s.connect((host, port))

for _ in range(5):
    s.send(f"{random.random()}".encode())
    print(s.recv(1024).decode())
    time.sleep(2)

s.close()
