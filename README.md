# Python Socket Programming with DataFrame Transmission

This repository contains a simple demonstration of socket programming in Python, where a server-client network is established to transmit a DataFrame with one million rows between the client and server.

## Features

- **Server-Client Network**: Establishes a network connection between a server and a client using Python's socket module.
- **DataFrame Transmission**: Demonstrates sending a DataFrame with one million rows from the client to the server over the network.
- **Sample Data**: Includes sample data generation for creating a large DataFrame for transmission.
- **Issues Faced**: One challenge encountered is when transmitting a large DataFrame, the `.recv()` function accumulates data in its buffer. As a result, when sending a larger DataFrame, there's a risk of buffer overflow. Ideally, the data should be paged to prevent this issue, but currently, this isn't happening.

## Requirements

- Python 3.x
- pandas
- socket
- pickle
- memory_profiler

## Usage

1. Clone this repository:

    ```bash
    git clone https://github.com/mihirsar/pysocket.git
    ```

2. Navigate to the project directory

    

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the server:

    ```bash
    python server.py
    ```

5. Run the client:

    ```bash
    python client.py
    ```

## File Structure

- `server.py`: Python script for the server side of the socket connection.
- `client.py`: Python script for the client side of the socket connection.
- `circuits.csv`: is a sample csv can be used as a demo
- `requirements.txt`: required libs
- `1 million rows sample dataset`: [Drive link](https://drive.google.com/file/d/1UhKJRCwCglC3tmBQwS9pgd0wgnGMsjrd/view?usp=drive_link)




