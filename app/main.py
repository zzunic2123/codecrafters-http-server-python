# Uncomment this to pass the first stage
import socket
import threading

status_codes = {200: 'OK', 404: 'Not Found'}

def build_response(path, status, content_type, header):
    path = path.split("/")
    func = path[1]

    body = ""
    if func == "echo":
        body = "/".join(path[2:])
    else:
        if len(header.split()) >= 2:
            body = header.split()[1]

    response = ("HTTP/1.1 " + str(status) + " " + status_codes[status] + "\r\n"
                + "Content-Type: " + content_type + "\r\n"
                + "Content-Length: " + str(len(body)) + "\r\n\r\n"
                + body)

    return response

def process_request(client_connection, client_address):
    request_data = client_connection.recv(1204)
    lines = request_data.decode().split("\r\n")
    method, path, version = lines[0].split()
    # host_placeholder, host = lines[1].split()
    # header_placeholder, header = lines[2].split()

    if path == "/" or path.startswith("/echo/"):
        response = build_response(path, 200, "text/plain", lines[2])
    else:
        response = build_response(path, 404, "text/plain", lines[2])

    client_connection.sendto(response.encode(), client_address)

def main():
    print("Logs from your program will appear here!")

    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    while True:
        client_connection, client_address = server_socket.accept()
        thread = threading.Thread(target=process_request, args=(client_connection,client_address))
        thread.daemon = True
        thread.start()


if __name__ == "__main__":
    main()
