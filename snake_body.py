import pygame
from constants import *
from snake_state import *


class SnakeBody():
    def __init__(self) -> None:
        self.position = pygame.Vector2((WINDOW_WIDTH/ 2) - OFFSET_START, WINDOW_HEIGHT / 2)
        self.lengh = 1
        ''' 
            la direzione è gestista con le varie tuple:
            * DX -> (1, 0)
            * SX -> (-1, 0)
            * UP -> (0, 1)
            * DOWN -> (0, -1)
        '''
        self._direction = None
        self._state = InitialState(self)

    def move(self, increment):
        self._state.move(increment);

    def change_direction(self, event):
        self._state.handle_input(event)

    def check_collision(self, width, height):
        return (
            True
            if self.position.x >= width
            or self.position.x <= 0
            or self.position.y >= height
            or self.position.y <= 0
            else False
        )

    def get_direction(self):
        return self._direction
