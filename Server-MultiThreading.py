import socket
import sys
from _thread import *
import threading

def read(conn):
    temp=''
    while True:
        try:
            data = conn.recv(1024)
            if(temp!=data):
                print ( 'client:',data)
                temp=data
                
        except:
            continue
    
def write(conn):
    msg='vacant:4'
    while True:
        try:
            conn.sendall((msg+'\n').encode('utf-8'))
        except:
            continue
        
            
    
            
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(socket.gethostname())
server_address = ('192.168.3.113',10000)
print ("starting up on %s port %s" % server_address)
sock.bind(server_address)
sock.listen(10)
while True:
    print ("waiting for a connection")
    connection, client_Address = sock.accept()
    print ('connection from', client_Address) 
    start_new_thread(read,(connection,))
    start_new_thread(write,(connection,))
    
