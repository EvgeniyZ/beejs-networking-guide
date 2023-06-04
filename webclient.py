import socket


def http_request_to_bytes(http):
    return (http + '\r\n\r\n').encode("ISO-8859-1")


def receive_response(s):
    buffer_size = 4096
    resp = ''
    b = s.recv(buffer_size)
    while len(b) != 0:
        resp += b.decode("ISO-8859-1")
        b = s.recv(buffer_size)
    return resp


print('input the desired host')
host = input()
s = socket.socket()
s.connect((host, 80))
r = "GET / HTTP/1.1\r\nHost: example.com\r\nConnection: close"
s.sendall(http_request_to_bytes(r))

response = receive_response(s)

s.close()
print(response)
