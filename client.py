import socket
import json
import subprocess
import time

def main():
    while True:
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect(('127.0.0.1', 8080))

            while True:
                command_str = client.recv(1024).decode()
                if not command_str:
                    break

                command = json.loads(command_str)

                if command["type"] == "command":
                    if command["content"] == "ping":
                        target = command["target"]
                        print(f"Received command: ping {target}")
                        result = subprocess.run(["ping", "-c", "1", target], capture_output=True, text=True)
                        output_str = result.stdout
                        print("Ping output:\n", output_str)
                        client.sendall(output_str.encode())

        except (ConnectionRefusedError, ConnectionResetError, ConnectionAbortedError):
            print("Server unreachable, retrying in 5 seconds...")
            time.sleep(5)

if __name__ == '__main__':
    main()
