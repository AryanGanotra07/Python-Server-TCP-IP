import socket
import sys
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('192.168.31.13',10000)
print('connecting to port 10000 ,',server_address)
sock.connect(server_address)
try:
    
    while True:
        message = input('Enter message:')
        
        sock.sendall(message.encode('utf-8'))
        data = sock.recv(1028)
        if data:
            print('server:',data)
            
        n=int(input("Enter 0 to end server"))
        if(n==0):
            break
finally:
    print("Closing socket")
    sock.close()
