import socket 

server = socket.socket()
server.bind(("localhost", 5000))
server.listen(2)
over = 0
msg = "PREPARE"

while True:
    replies = []
    print(f"Coordinator {msg}")
    if over == 1:
        break
    for i in range(3):
        client, add = server.accept()
        client.send(msg.encode())
        reply = client.recv(1024).decode()
        print(f"Subordinate {add} : {reply}")
        replies.append(reply)
    if "ABORT" in replies:
        msg = "ABORT"
        over = 1
    elif "SUCCESS" in replies:
        msg = "COMPLETE"
        over = 1
    else:
        msg = "COMMIT"   