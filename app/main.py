# Uncomment this to pass the first stage
import socket


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    #
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    client_connection, client_address = server_socket.accept()
    request_data = client_connection.recv(1204)
    lines = request_data.decode().split("\r\n")
    method, path, version = lines[0].split()

    print(lines)
    response = ""
    if path == "/":
        response = "HTTP/1.1 200 OK\r\n\r\n"
    else:
        response = "HTTP/1.1 404 Not Found\r\n\r\n"


    client_connection.send(response.encode())

if __name__ == "__main__":
    main()
