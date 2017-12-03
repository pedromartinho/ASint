class Node:
    def __init__(self, godNode, type, name):
        self.godNode = godNode
        self.type = type
        self.name = name
        self.childrenNodes = []


    def addChild(self, node):
        self.childrenNodes.append(node)

class roomNode(Node):
    def __init__(self, godNode, type, name, info):
        super(roomNode, self).__init__(godNode, type, name)
        self.info = info