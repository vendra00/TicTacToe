# utils/NetworkUtils.py

import socket
import requests


def start_host():
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 0))  # Bind to localhost and a free port
    server_socket.listen(1)

    # Get the host IP and port
    host_ip, host_port = server_socket.getsockname()
    print(f"Game hosted at {host_ip}:{host_port}")

    # Wait for a connection
    print("Waiting for a player to join...")
    connection, client_address = server_socket.accept()
    print(f"Connection from {client_address}")

    return connection


def join_game(host_ip, host_port):
    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the host's port
    client_socket.connect((host_ip, host_port))
    print(f"Connected to game at {host_ip}:{host_port}")

    return client_socket


def get_public_ip_address():
    """
    Retrieves the public IP address of the host machine using an external web service.

    Returns:
        str: The public IP address of the host.
    """
    try:
        response = requests.get('https://api.ipify.org')
        return response.text
    except requests.RequestException:
        return 'Unable to get public IP address'


def get_host_details():
    """
    Retrieves the public IP address and port number for hosting a game.

    Returns:
        tuple: A tuple containing the public IP address and a port number.
    """
    public_ip = get_public_ip_address()

    # Create a server socket to get a free port
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', 0))  # Bind to all interfaces with a random free port
        host_port = s.getsockname()[1]

    return public_ip, host_port
