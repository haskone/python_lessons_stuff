import socket
from threading import Thread

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 12346

s.bind((host, port))
s.listen(5)

UDP_IP_DEST = "127.0.0.1"
UDP_PORT_DEST = 50050

UDP_IP_SOURCE = "127.0.0.1"
UDP_PORT_SOURCE = 50060

source_udp = socket.socket(
    socket.AF_INET, socket.SOCK_DGRAM)          
source_udp.bind((UDP_IP_SOURCE, UDP_PORT_SOURCE))

def client_process(sock, addr):
    data = sock.recv(1024).decode()
    print(f'Got from {addr}: {data}')
       
    udp_sock = socket.socket(socket.AF_INET,
                     socket.SOCK_DGRAM)
    udp_sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
    data, addr = source_udp.recvfrom(1024)
    if data.decode() == "OK":        
        response = 'OK'
        print(f'Resending "{response}" to {addr} ...')
        sock.send(response.encode())
    else:
        print(f"Got wrong response: {data.decode()}")

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
