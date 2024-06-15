#!/usr/bin/env python3
import socket

SERVER_ADDRESS = "127.0.0.1"
PORT = 4000
BUFFER_SIZE = 1024

server = socket.create_server((SERVER_ADDRESS, PORT))
print("Listening for connections on port", PORT)
server.listen()


connection, client_address = server.accept()
print("Connected to", client_address)
try:
	while True:
		data = connection.recv(BUFFER_SIZE)
		if not data:
			break
		print(f"Received: {data.decode()}")
		connection.sendall(data)
		print(f"Echoed back: {data.decode()}")
finally:
	connection.close()
	print("Disconnect from", client_address)
