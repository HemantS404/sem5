import socket

cliser = socket.socket()
cliser.connect(('localhost', 5000))
cliser.send(b'Meow client')
data = cliser.recv(1028)
print(data)
cliser.close()