import socket
import sys
from _thread import *
import threading
import random


def read(conn):
    temp=''
    while True:
        try:
            data = conn.recv(1024)
            if(temp!=data):
                print ( 'client:',data)
                temp=data
                start_new_thread(write,(conn,"license_status:Received",))
                   
                
                
        except:
            continue
    
def write(conn,msg):
    try:
        conn.sendall((msg+'\n').encode('utf-8'))
    except:
        print("Error-sending-msg")

def init(sock):
    try:
        while True:
            print("waiting for a connection")
            connection, client_Address = sock.accept()
            print ('connection from', client_Address) 
            start_new_thread(read,(connection,))
            start_new_thread(write,(connection,"vacant:4",))
    
    
    finally:
        connection.close()
        sock.close()

    connection.close()
    sock.close()
        
            
    
            
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(socket.gethostname())
server_address = ('192.168.31.13',10000)
print ("starting up on %s port %s" % server_address)
sock.bind(server_address)
sock.listen(10)
start_new_thread(init,(sock,))


    
