# Example on how to write a string to UDP socket
import socket

# Define server IP address and port
server = "192.168.1.101"
port = 1983

# Initialize and write to the socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(bytes("25 5 \r\n", "utf-8"), (server, port))


