import socket
from threading import Thread

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 12347

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
    udp_sock.sendto(data.encode(),
                    (UDP_IP_DEST, UDP_PORT_DEST))
    data_udp, addr_udp = source_udp.recvfrom(1024)

    print(f'Got UDP from {addr_udp}: {data_udp}')
    response = 'OK'
    print(f'Resending "{response}" to {addr} ...')
    sock.send(response.encode())

    sock.close()
    
while True:
    print("Server started")
    # inp = input()
    # if inp == 'break':
    #     break

    print('Server is waiting for incoming connect...')
    sock, addr = s.accept()
    print('Got connection from', addr)
    
    t = Thread(target=client_process, args=(sock, addr))
    t.start()
