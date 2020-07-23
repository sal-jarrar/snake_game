from random import randint
from config import Config


class Apple():
    def __init__(self):
        self.set_new_location()

    def set_new_location(self):
        self.x = randint(0, Config.CELLWIDTH-1)
        self.y = randint(0, Config.CELLHEGHT-1)
