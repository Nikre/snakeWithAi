import pygame
from collections import deque
from constants import *
from snake_state import *


class Snake():
    def __init__(self) -> None:

        center_x = (WINDOW_WIDTH // CELL_SIZE) // 2
        center_y = (WINDOW_HEIGHT // CELL_SIZE) // 2

        # Sposta la posizione iniziale leggermente a sinistra (ad esempio, di 1/4 della larghezza)
        offset = (OFFSET_START // CELL_SIZE) // 4
        start_x = center_x - offset

        # Assicurati che la posizione iniziale sia all'interno della finestra
        start_x = max(0, start_x)

        # Converti le coordinate della cella in coordinate pixel
        pixel_x = start_x * CELL_SIZE + CELL_SIZE // 2
        pixel_y = center_y * CELL_SIZE + CELL_SIZE // 2

        self.body = deque([pygame.Vector2(pixel_x, pixel_y)])
        self._state = InitialState(self)

    def move(self, increment):
        movement = self._state.move(increment)
        if movement:
            self.body.popleft()
            self.body.append(movement)

    def eat(self, increment):
        movement = self._state.move(increment)
        self.body.append(movement)

    def change_direction(self, action):
        self._state.handle_input(action)

    def get_direction(self):
        return self._state._direction

    def get_head_position(self):
        return self.body[-1]

    def is_self_eaten(self):
        return self.body.count(self.get_head_position()) >= 2