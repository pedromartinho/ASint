import socket

s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host, port))
s.listen(5)

while True:
    c, addr = s.accept()
    print ('Connection from', addr)
    c.send('hello'.encode(encoding='utf-8'))
    c.close()