import GameState

class Node:
    def __init__():
        self.Parent = self
        self.GameState = Gamestate()
        self.human = True
        self.Children = []
    def __init__(self, parent, bd, human):
        self.Parent = parent
        self.GameState = bd
        self.human = human
        self.Children = []

    def AddChild(self, bd):
        child = Node(self, bd, not self.human)
        self.Children.append(child)
        return child

    def BecomeRoot(self):
        self.Parent = None
        return self

