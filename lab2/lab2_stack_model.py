class rpnCalculator:
    'class for all employees'

    def __init__(self):
        self.stack = []

    def pushValue(self, value):
        self.stack.append(value)

    def popValue(self):
        return self.stack.pop()

    def Add_sub(self):
        var1 = self.popValue()
        var2 = self.popValue()
        var3 = var1 + var2
        self.pushValue(var3)

stack = rpnCalculator()
stack.pushValue(3)
stack.pushValue(4)
stack.pushValue(4)
stack.Add_sub()
value = stack.popValue()
stack.pushValue(1)
print (stack.__dict__)
