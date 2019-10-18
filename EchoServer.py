import socket
import sys
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#sock3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(socket.gethostname())
#server_name = sys.argv[1]
server_address = ('192.168.3.113',10000)
#server_address1 = ('192.168.1.181',9999)
#server_address2 = ('192.168.1.181',9998)
#server_address3 = ('192.168.1.181',9997)
print ("starting up on %s port %s" % server_address)
sock.bind(server_address)
#sock1.bind(server_address1)
#sock2.bind(server_address2)
#sock3.bind(server_address3)
sock.listen(1)
#sock1.listen(1)
#sock2.listen(1)
#sock3.listen(1)
print ("waiting for a connection")
connection, client_Address = sock.accept()
#connection1, client_Address1 = sock1.accept()
#connection2, client_Address2 = sock2.accept()
#connection3, client_Address3 = sock3.accept()

while True:
    try:
        print ('connection from', client_Address)
       # print ('connection from', client_Address1)
        #print ('connection from', client_Address2)
        #print ('connection from', client_Address3)
        while True:
            socket = 0
            message = 'vacant:9'
            if(socket==0):
                connection.sendall((message+'\n').encode('utf-8'))
            elif socket==1:
                connection1.sendall((message+'\n').encode('utf-8'))
            elif socket==2:
                connection2.sendall((message+'\n').encode('utf-8'))
            elif socket==3:
                connection3.sendall((message+'\n').encode('utf-8'))
            data = connection.recv(1028)
            print ( 'client:',data)
        
    finally:
        connection.close()
        #connection1.close()
        #connection2.close()
        #connection3.close()
connection.close()
#connection1.close()
#connection2.close()
#connection3.close()


