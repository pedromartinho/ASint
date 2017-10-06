import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
from random import randint

class interface:

    def __init__(self):
        curses.initscr()
        self.win = curses.newwin(20, 60, 0, 0)
        self.win.keypad(1)
        curses.noecho()
        curses.curs_set(0)
        self.win.border(0)
        self.win.nodelay(1)
        self.win.addstr(0, 2, 'Score : ' + str(0) + ' ')
        self.win.addstr(0, 27, ' SNAKE ')

    def displayApple(self,pos):
        self.win.addch(pos[0],pos[1],'*')

    def displaySnakeHead(self,pos):
        self.win.addch(pos[0],pos[1],'#')

    def displayBlank(self,pos):
        self.win.addch(pos[0],pos[1],' ')

    def displayInfo(self,score,size):
        self.win.border(0)
        self.win.addstr(0, 2, 'Score : ' + str(score) + ' ')                # Printing 'Score' and
        self.win.addstr(0, 27, ' SNAKE ')
        self.win.timeout(int(150 - (size/5 + size/10)%120))

    def gameOver(self):
        curses.endwin()

    def getKey(self):
        return self.win.getch()

class snake:

    def __init__(self):
        self.body = [[4,10], [4,9], [4,8]]

    def verifyEdge(self):
        if self.body[0][0] == 0:
            self.body[0][0] = 18
        elif self.body[0][1] == 0:
            self.body[0][1] = 58
        elif self.body[0][0] == 19:
            self.body[0][0] = 1
        elif self.body[0][1] == 59:
            self.body[0][1] = 1
        else:
            pass

    def verifyAlive(self):
        if self.body[0] in self.body[1:]:
            return False
        else:
            return True

    def head(self):
        return self.body[0]

    def size(self):
        return len(self.body)

    def getBody(self):
        return self.body

    def moveHead(self,key):
        self.body.insert(0,[self.body[0][0] + (key == KEY_DOWN and 1) + (key == KEY_UP and -1), self.body[0][1] + (key == KEY_LEFT and -1) + (key == KEY_RIGHT and 1)])
        self.verifyEdge()
        if self.verifyAlive():
            return self.body[0]
        else:
            return None
        # If snake crosses the boundaries, make it enter from the other side

    def lostEnd(self):
        last = self.body.pop()
        return last

class apple:

    def __init__(self):
        self.body = [10,20]

    def newPosition(self,snake):
        self.body = []
        while self.body == []:
            self.body = [randint(1, 18), randint(1, 58)]                 # Calculating next food's coordinates
            if self.body in snake: self.body = []
        return self.body

    def position(self):
        return self.body

class game:
    def __init__(self):
        self.interface = interface()
        self.snake = snake()
        self.apple = apple()
        self.score = 0

    def main(self):
        key = KEY_RIGHT
        self.interface.displayApple(self.apple.position())
        while key != 27:
            self.interface.displayInfo(self.score,self.snake.size())
            prevKey = key
            event = self.interface.getKey()

            key = key if event == -1 else event                                               # Previous key pressed
            if key not in [KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN, 27]:     # If an invalid key is pressed
                key = prevKey
            head = self.snake.moveHead(key)
            if head == None:
                break
            if head == self.apple.position():
                self.interface.displayApple(self.apple.newPosition(self.snake.getBody()))
                self.score = self.score + 1
            else:
                self.interface.displayBlank(self.snake.lostEnd())
            self.interface.displaySnakeHead(self.snake.head())
        self.interface.gameOver()
        print("\nScore - " + str(self.score))
        print("http://bitemelater.in\n")

game = game()
game.main()
