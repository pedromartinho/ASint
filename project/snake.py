class npmCalculator:

    def __init__(self):
        self.stack = []

    def pushValue(self, value):
        self.stack.append(value)

    def popValue(self):
        return self.stack.pop()

    def add(self):
        a = self.stack.pop()
        b = self.stack.pop()
        c = a + b
        self.stack.append(c)

    def sub(self):
        a = self.stack.pop()
        b = self.stack.pop()
        c = a - b
        self.stack.append(c)
