import socket
import pickle
import pandas as pd
import time
from memory_profiler import profile

def send_dataframe_chunks(dataframe, chunk_size, sock):
    total_chunks = (len(dataframe) + chunk_size - 1) // chunk_size  # Calculate total number of chunks
    chunks_sent = 0

    # Iterate through chunks of the DataFrame and send them to the server
    for i in range(0, len(dataframe), chunk_size):
        chunk = dataframe.iloc[i:i + chunk_size]
        serialized_chunk = pickle.dumps(chunk)
        sock.sendall(serialized_chunk)
        chunks_sent += 1

        # Calculate progress percentage
        progress_percent = (chunks_sent / total_chunks) * 100
        print(f"Progress: {progress_percent:.2f}%")

    # Sending an empty message to indicate the end of transmission
    sock.send(b"")  # Send an empty byte string to signal the end

@profile
def send_dataframe_with_measurement():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('127.0.0.1', 5555)  # Change this to the server's IP and port
    client_socket.connect(server_address)

    # Read the entire DataFrame
    df = pd.read_csv('LOAN_DATA_202312140939.csv')

    # Set the chunk size based on the number of rows you want to send at once
    chunk_size = len(df)  # Set your desired chunk size here

    try:
        print("Sending df........")
        start_time = time.time()  # Start time measurement
        send_dataframe_chunks(df, chunk_size, client_socket)
        end_time = time.time()  # End time measurement
        print("DataFrame sent successfully.")
        print(f"Time taken: {end_time - start_time} seconds")

    except Exception as e:
        print(f"Error occurred while sending DataFrame: {e}")

    client_socket.close()

if __name__ == "__main__":
    send_dataframe_with_measurement()
