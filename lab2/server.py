import socket
from calculator import *

s = socket.socket()
host = socket.gethostbyname('localhost')
port = 12345
s.bind((host, port))
s.listen(5)

stack = npmCalculator()
c, addr = s.accept()

while True:
    command = c.recv(1024)
    if 'push' in command:
        args = command.split()
        value = int(args[1])
        stack.pushValue(value)
        print("Pushed %s to the stack." % value)
        c.send(str(stack.stack))
    elif command == 'pop':
        value = stack.popValue()
        print("Popped %s from the stack" % value)
        c.send(str(stack.stack))
    elif command == 'add':
        stack.add()
        print("Added values")
        c.send(str(stack.stack))
    elif command == 'sub':
        stack.sub()
        print("Subtracted values")
        c.send(str(stack.stack))
    else:
        print("Command incorrect!")
        c.send("Not a valid command!")
