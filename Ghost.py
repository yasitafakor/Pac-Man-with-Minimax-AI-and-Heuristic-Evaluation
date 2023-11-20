class Ghost:

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def getposition(self):
        return self.position

    def up(self):
        self.position[0] -= 1

    def down(self):
        self.position[0] += 1

    def right(self):
        self.position[1] += 1

    def left(self):
        self.position[1] -= 1



