class Node:
    def __init__(self, data):
        self.children = []
        self.data = data

    def PrintTree(self):
        print(self.data)
