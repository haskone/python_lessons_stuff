import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 50050

sock = socket.socket(socket.AF_INET,
                     socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET,
                socket.SO_RCVBUF, 1024)
sock.setblocking(0)                
sock.bind((UDP_IP, UDP_PORT))


while True:
    try:
        data, addr = sock.recvfrom(5)
        import time
        time.sleep(1)
        print("received message:", data.decode())
    except BlockingIOError:
        pass