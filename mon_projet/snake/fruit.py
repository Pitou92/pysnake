# snake/fruit.py
import random
from snake.settings import SCREEN_WIDTH, SCREEN_HEIGHT, CELL_SIZE

class Fruit:
    def __init__(self):
        self.position = self.random_position()

    def random_position(self):
        return (random.randrange(0, SCREEN_WIDTH, CELL_SIZE),
                random.randrange(0, SCREEN_HEIGHT, CELL_SIZE))
