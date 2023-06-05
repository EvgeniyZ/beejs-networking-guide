import socket


def receive(s):
    buffer_size = 4096
    resp = ''
    while True:
        content = s.recv(buffer_size).decode("ISO-8859-1")
        resp += content
        if content.endswith('\r\n\r\n'):
            return resp


s = socket.socket()
try:
    s.bind(('', 28333))
    s.listen()
    while True:
        new_connection = s.accept()
        print(new_connection[1][0] + ':' + str(new_connection[1][1]) + '\r\n')
        client_socket = new_connection[0]
        request = receive(client_socket)
        print(request)
        method = request.split('\r\n')[0].split(' ')[0]
        print('request method: ' + method)
        client_socket.sendall(('HTTP/1.1 200 OK\r\nContent-Type: text/text;\r\nConnection: close\r\n\r\n' +
                              'simple server response\r\n\r\n').encode('ISO-8859-1'))
        client_socket.close()
finally:
    s.close()
