import random
from constants import *

class Food():
    def __init__(self) -> None:

        grid_width = WINDOW_WIDTH // CELL_SIZE
        grid_height = WINDOW_HEIGHT // CELL_SIZE

        # Genera posizioni casuali all'interno della griglia
        grid_x = random.randint(0, grid_width - 1)
        grid_y = random.randint(0, grid_height - 1)

        # Converte le coordinate della griglia in coordinate pixel
        pixel_x = grid_x * CELL_SIZE + CELL_SIZE // 2
        pixel_y = grid_y * CELL_SIZE + CELL_SIZE // 2

        self._food_position = (pixel_x, pixel_y)

    def get_food_position(self):
        return self._food_position

    def food_eaten(self):
        self.__init__()
