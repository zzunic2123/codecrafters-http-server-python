# Uncomment this to pass the first stage
import socket
import threading
import os

status_codes = {200: 'OK', 404: 'Not Found', 201: 'Created'}


def build_response(body, status, content_type):
    response = ("HTTP/1.1 " + str(status) + " " + status_codes[status] + "\r\n"
                + "Content-Type: " + content_type + "\r\n"
                + "Content-Length: " + str(len(body)) + "\r\n\r\n"
                + body)

    return response


def resolve_body(path, header, directory_path = None):

    path = path.split("/")
    if not directory_path:
        func = path[1]

        body = ""
        if func == "echo":
            body = "/".join(path[2:])
        else:
            if len(header.split()) >= 2:
                body = header.split()[1]

        return body

    file_path = path[2]

    print(file_path)
    print(directory_path)




def process_request(client_connection, client_address, directory_path):
    request_data = client_connection.recv(1204)
    lines = request_data.decode().split("\r\n")
    method, path, version = lines[0].split()
    # host_placeholder, host = lines[1].split()
    # header_placeholder, header = lines[2].split()

    if method == "GET":
        if path == "/" or path.startswith("/echo/"):
            response = build_response(resolve_body(path, lines[2]), 200, "text/plain")
        elif path.startswith("/files/"):
            file_path = path.split("/")[2]
            if not os.path.isfile(directory_path + file_path):
                response = build_response(resolve_body(path, lines[2]), 404, "text/plain")
            else:
                f = open(directory_path + file_path, "r")
                body = f.read()
                response = build_response(body, 200, "application/octet-stream")
        else:
            response = build_response(resolve_body(path, lines[2]), 404, "text/plain")
    else:
        file_path = path.split("/")[2]
        request_body = lines[6]
        f = open(directory_path + file_path, "w")
        f.write(request_body)
        response = build_response(request_body, 201, "application/octet-stream")

    client_connection.sendto(response.encode(), client_address)


import sys


def main():
    print("Logs from your program will appear here!")

    directory_path = ""
    if len(sys.argv) >= 2:
        directory_path = sys.argv[2]
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    while True:
        client_connection, client_address = server_socket.accept()
        thread = threading.Thread(target=process_request, args=(client_connection, client_address, directory_path))
        thread.start()


if __name__ == "__main__":
    main()
