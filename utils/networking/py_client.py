import socket               # Import socket module

s = socket.socket()         # Create a socket object
#host = socket.gethostname() # Get local machine name
host = 'localhost'
port = 9999                # Reserve a port for your service.

print host
s.connect((host, port))
str_1 = 16*'\x61'
s.send(str_1)
print s.recv(1024)
s.send(str_1)
print s.recv(1024)
s.close()                     # Close the socket when done