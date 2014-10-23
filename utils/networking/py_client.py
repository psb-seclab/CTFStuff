import socket               # Import socket module

s = socket.socket()         # Create a socket object
#host = socket.gethostname() # Get local machine name

host = '128.118.102.44'
port = 9999                

s.connect((host, port))
str_1 = 'hello world'
s.send(str_1)
print s.recv(1024)
print s.recv(1024)

s.close()                     # Close the socket when done