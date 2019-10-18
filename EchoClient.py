import socket
import sys
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('192.168.1.119',10000)
server_address1 = ('192.168.1.119',9999)
server_address2 = ('192.168.1.119',9998)
server_address3 = ('192.168.1.119',9997)
print('connecting to port 10000 ,',server_address)
sock.connect(server_address)
sock1.connect(server_address1)
sock2.connect(server_address2)
sock3.connect(server_address3)
try:
    while True:
        socket = int(input('enter socket'))
        message = input('Enter message:')
        if(socket==0):
            sock.sendall((message+'\n').encode('utf-8'))
        elif socket==1:
            sock1.sendall((message+'\n').encode('utf-8'))
        elif socket==2:
            sock2.sendall((message+'\n').encode('utf-8'))
        elif socket==3:
            sock3.sendall((message+'\n').encode('utf-8'))
except:
    print("Excepted")
