import socket
import json

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 8080))
    server.listen(1)

    while True:
        conn, addr = server.accept()

        try:
            handle_client(conn)
        except Exception as e:
            print(f"Error handling client: {e}")

def handle_client(conn):
    command = {
        "type": "command",
        "content": "ping",
        "target": "8.8.8.8" # Replace with the desired IP address
    }
    command_str = json.dumps(command)
    conn.sendall(command_str.encode())

    response = conn.recv(1024)
    print("Ping result:\n", response.decode())

if __name__ == '__main__':
    main()
