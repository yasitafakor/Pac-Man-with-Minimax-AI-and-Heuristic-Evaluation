class Player:
    def __init__(self, position):
        self.position = position

    def up(self):
        self.position[0] -= 1

    def down(self):
        self.position[0] += 1

    def right(self):
        self.position[1] += 1

    def left(self):
        self.position[1] -= 1



