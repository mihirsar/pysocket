# Python Socket Programming with DataFrame Transmission

This repository contains a simple demonstration of socket programming in Python, where a server-client network is established to transmit a DataFrame with one million rows between the client and server.

## Features

- **Server-Client Network**: Establishes a network connection between a server and a client using Python's socket module.
- **DataFrame Transmission**: Demonstrates sending a DataFrame with one million rows from the client to the server over the network.
- **Sample Data**: Includes sample data generation for creating a large DataFrame for transmission.

## Requirements

- Python 3.x
- pandas
- socket
- pickle
- memory_profiler

## Usage

1. Clone this repository:

    ```bash
    git clone https://github.com/yourusername/python-socket-dataframe-transmission.git
    ```

2. Navigate to the project directory:

    ```bash
    cd python-socket-dataframe-transmission
    ```

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
- `data_generation.py`: Python script for generating sample data (one million rows DataFrame).
- `requirements.txt`: File containing the required Python dependencies.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

