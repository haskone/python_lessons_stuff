import socket
from threading import Thread

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 12346

s.bind((host, port))
s.listen(5)

def client_process(sock, addr):
    i = 5
    while True:
        if i == 0:
            break

        data = sock.recv(1024).decode()
        print(f'Got from {addr}: {data}')
        response = f'OK: "{data}"'
        print(f'Sending "{response}" to {addr} ...')
        sock.send(response.encode())
        i -= 1
    sock.close()
    
while True:
    inp = input()
    if inp == 'break':
        break

    print('Server is waiting for incoming connect...')
    sock, addr = s.accept()
    print('Got connection from', addr)
    
    t = Thread(target=client_process, args=(sock, addr))
    t.start()
