from config import Config
from random import randint


class Snake():
    UP = "up"
    DOWN = "down"
    RIGHT = "right"
    LEFT = "left"
    HEAD = 0

    def __init__(self):
        self.x = randint(0, Config.CELLWIDTH-6)
        self.y = randint(0, Config.CELLHEGHT-6)
        self.dirction = self.RIGHT
        self.worm_coords = [
            {"x": self.x, "y": self.y},
            {"x": self.x-1, "y": self.y},
            {"x": self.x-2, "y": self.y}
        ]

    def update(self, apple):
        if self.worm_coords[self.HEAD]["x"] == apple.x and self.worm_coords[self.HEAD]["y"] == apple.y:
            apple.set_new_location()
        else:
            del self.worm_coords[-1]

        if self.dirction == self.UP:
            new_head = {"x": self.worm_coords[self.HEAD]
                        ["x"], "y": self.worm_coords[self.HEAD]["y"]-1}

        elif self.dirction == self.DOWN:
            new_head = {"x": self.worm_coords[self.HEAD]
                        ["x"], "y": self.worm_coords[self.HEAD]["y"]+1}

        elif self.dirction == self.RIGHT:
            new_head = {"x": self.worm_coords[self.HEAD]
                        ["x"]+1, "y": self.worm_coords[self.HEAD]["y"]}

        if self.dirction == self.LEFT:
            new_head = {"x": self.worm_coords[self.HEAD]
                        ["x"]-1, "y": self.worm_coords[self.HEAD]["y"]}

        self.worm_coords.insert(0, new_head)
