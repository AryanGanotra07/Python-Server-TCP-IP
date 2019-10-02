import socket
import sys
sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(socket.gethostname())
#server_name = sys.argv[1]
server_address = ('192.168.31.13', 10000)
print ("starting up on %s port %s" % server_address)
sock.bind(server_address)
sock.listen(1)

while True:
    print ("waiting for a connection")
    connection, client_Address = sock.accept()
    try:
        print ('connection from', client_Address)
        while True:
            data = connection.recv(1028)
            print ( 'client:',data)
            
            if data:
                connection.sendall(b'Message recieved by server')
            else:
                print ('no more data from', client_Address)
                break
    finally:
        connection.close()
