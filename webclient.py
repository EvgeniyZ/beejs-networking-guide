import socket


def http_request_to_bytes(http):
    return (http + '\r\n\r\n').encode("ISO-8859-1")


s = socket.socket()
s.connect(("example.com", 80))
r = "GET / HTTP/1.1\r\nHost: example.com\r\nConnection: close"
s.sendall(http_request_to_bytes(r))
b = s.recv(4096)
s.close()
response = b.decode("ISO-8859-1")
print(response)
