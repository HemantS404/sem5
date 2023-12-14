import socket 
import time

over = 0
while True:
    if over == 1:
        break
    try:
        client = socket.socket()
        client.connect(("localhost", 5000))
        msg = client.recv(1024).decode()
        print(f"Coordinator : {msg}")
        if msg =="ABORT":
            over = 1
        elif msg =="COMMIT":
            inp = input("Enter (SUCCESS/ABORT) : ").upper()
            client.send(inp.encode())
        else:
            inp = input("Enter (OK/ABORT) : ").upper()
            client.send(inp.encode())
    except Exception as e:
        print("END", e)
        break