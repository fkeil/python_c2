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
    command = input("Enter command: ")
    command_json = {
        "type": "command",
        "content": command
    }
    command_str = json.dumps(command_json)
    conn.sendall(command_str.encode())

    response = conn.recv(1024)
    print("Command result:\n", response.decode())

if __name__ == '__main__':
    main()
