import socket
import pickle
import pandas as pd

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('127.0.0.1', 5555)  # Change this to your desired IP and port
server_socket.bind(server_address)
server_socket.listen(1)

print("Waiting for a client to connect...")

client_socket, client_address = server_socket.accept()
print(f"Connection from {client_address} has been established.")

print("Receiving...")

received_data = b""  # Variable to store received data

while True:
    chunk = client_socket.recv(4096)
    if not chunk:
        break
    received_data += chunk

# Deserialize received data back into a DataFrame
received_dataframe = pickle.loads(received_data)

# Print the complete DataFrame
print("Complete DataFrame received from the client:")
print(received_dataframe)

# Save the reconstructed DataFrame as a CSV file
received_dataframe.to_csv('Serverdf.csv', index=False)

# Close the sockets
client_socket.close()
server_socket.close()
