import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 50050

UDP_IP_CLIENT = "127.0.0.1"
UDP_PORT_CLIENT = 50060

sock = socket.socket(socket.AF_INET,
                     socket.SOCK_DGRAM)              
sock.bind((UDP_IP, UDP_PORT))

while True:   
    print("Server started")
    data, addr = sock.recvfrom(1024)

    print(f"Got {data} from {addr}")
    sock_client = socket.socket(
        socket.AF_INET, socket.SOCK_DGRAM)
    sock_client.sendto(
        "OK".encode(),
        (UDP_IP_CLIENT, UDP_PORT_CLIENT))