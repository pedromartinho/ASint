import socket

s = socket.socket()
host = socket.gethostbyname('localhost')
port = 12345
s.connect((host, port))

while True:
    request = raw_input("> ")
    s.send(request)
    print s.recv(1024)
