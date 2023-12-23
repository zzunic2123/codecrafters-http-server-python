# Uncomment this to pass the first stage
import socket

status_codes = {200: 'OK', 404: 'Not Found'}


def build_response(path, status, contentType):
    path = path.split("/")
    func = path[0]
    body = "/".join(path[2:])
    response = ("HTTP/1.1 " + str(status) + " " + status_codes[status] + "\r\n"
                + "Content-Type: " + contentType + "\r\n"
                + "Content-Length: " + str(len(body)) + "\r\n\r\n"
                + body)

    return response


def main():
    print("Logs from your program will appear here!")

    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    client_connection, client_address = server_socket.accept()
    request_data = client_connection.recv(1204)
    lines = request_data.decode().split("\r\n")
    method, path, version = lines[0].split()

    if path == "/" or path.startswith("/echo/"):
        response = build_response(path, 200, "text/plain")
    else:
        response = build_response(path, 404, "text/plain")

    client_connection.sendall(response.encode())


if __name__ == "__main__":
    main()
