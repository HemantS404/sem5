import socket

sersoc = socket.socket()

sersoc.bind(('localhost', 5000))
sersoc.listen()
while True:
    cliser, addr = sersoc.accept()
    print("Conneted to :", addr)
    data = cliser.recv(1028)
    print(data)
    cliser.send(b'Meow Server')
    break
sersoc.close()