import random
from constants import *

class Food():
    def __init__(self) -> None:
        self._food_position = (
            random.randint(0, WINDOW_WIDTH - 1),
            random.randint(0, WINDOW_HEIGHT - 1),
        )
    
    def get_food_position(self):
        return self._food_position
    
    def food_eaten(self):
        self.__init__()
