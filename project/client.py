import socket
import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN

s = socket.socket()
host = socket.gethostbyname('localhost')
port = 12340
s.connect((host, port))

key = KEY_RIGHT
curses.initscr()
win = curses.newwin(20, 60, 0, 0)
while True:
    event = win.getch()
    key = key if event == -1 else event
    if key == KEY_RIGHT:
        s.send(str(KEY_RIGHT))
    elif key == KEY_LEFT:
        s.send(str(KEY_LEFT))
    elif key == KEY_UP:
        s.send(str(KEY_UP))
    elif key == KEY_DOWN:
        s.send(str(KEY_DOWN))
    elif key == 27:
        s.send(str(27))
