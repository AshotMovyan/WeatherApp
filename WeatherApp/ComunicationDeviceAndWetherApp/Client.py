import socket
import time

HEADER = 64
PORT = 8080
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.1.20"
ADDR = (SERVER, PORT)


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(2)
client.connect(ADDR)
print('connected_Client')


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    c = client.recv(2048).decode(FORMAT)
    # print(c)
    return c


# send('')


