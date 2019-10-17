import socket
import sys

def read(conn):
    while True:
        try:
            data = connection.recv(1028)
            print ( 'client:',data)
        except:
            continue
def write(conn,msg):
    while True:
        try:
            conn.sendall((message+'\n').encode('utf-8'))
        except:
            continue
            
    
            
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(socket.gethostname())
server_address = ('192.168.3.113',10000)
print ("starting up on %s port %s" % server_address)
sock.bind(server_address)
sock.listen(1)
print ("waiting for a connection")
connection, client_Address = sock.accept()
print ('connection from', client_Address)

        
        
        
