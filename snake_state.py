import pygame
import numpy as np
from constants import *
from abc import ABC, abstractmethod


class SnakeState(ABC):
    """
    La direzione del serpente è così definita
    [0, 1, 0, 0] -> Right
    [1, 0, 0, 0] -> Left
    [0, 0, 1, 0] -> UP 
    [0, 0, 0, 1] -> DOWN
    """

    @abstractmethod
    def move(self, increment):
        pass

    @abstractmethod
    def handle_input(self, action):
        pass

    def get_direction(self):
        return self._direction


class InitialState(SnakeState):
    def __init__(self, snake):
        self.snake = snake
        self._direction = DIRECTION_NONE

    def move(self, increment):
        return None

    def handle_input(self, action):
        if np.array_equal(action, ACTION_STRAIGHT):
            self.snake._state = GoRight(self.snake)
        elif np.array_equal(action, ACTION_RIGHT_TURN):
            self.snake._state = GoDown(self.snake)
        elif np.array_equal(action, ACTION_LEFT_TURN): # EXPLICIT
            self.snake._state = GoUp(self.snake)
        
        ''' NOTE: Old version
             if event[pygame.K_UP]:  # UP
                 self.snake._state = GoUp(self.snake)
             if event[pygame.K_DOWN]:  # DOWN
                 self.snake._state = GoDown(self.snake)
             if event[pygame.K_RIGHT]:  # RIGHT
                 self.snake._state = GoRight(self.snake)
             if event[pygame.K_LEFT]:  # LEFT
                 self.snake._state = GoLeft(self.snake)
        '''

class GoRight(SnakeState):
    def __init__(self, snake):
        self.snake = snake
        self._direction = DIRECTION_RIGHT

    def move(self, increment):
        return (
            self.snake.get_head_position()[0] + increment,
            self.snake.get_head_position()[1],
        )

    def handle_input(self, action):
        if np.array_equal(action, ACTION_STRAIGHT):
            pass
            # self.snake._state = GoRight(self.snake)
        elif np.array_equal(action, ACTION_RIGHT_TURN):
            self.snake._state = GoDown(self.snake)
        elif np.array_equal(action, ACTION_LEFT_TURN):  # EXPLICIT
            self.snake._state = GoUp(self.snake)

        # if event[pygame.K_UP]:  # UP
        #     self.snake._state = GoUp(self.snake)
        # if event[pygame.K_DOWN]:  # DOWN
        #     self.snake._state = GoDown(self.snake)


class GoLeft(SnakeState):
    def __init__(self, snake):
        self.snake = snake
        self._direction = DIRECTION_LEFT

    def move(self, increment):
        return (
            self.snake.get_head_position()[0] - increment,
            self.snake.get_head_position()[1],
        )

    def handle_input(self, action):
        if np.array_equal(action, ACTION_STRAIGHT):
            pass
            # self.snake._state = GoLeft(self.snake)
        elif np.array_equal(action, ACTION_RIGHT_TURN):
            self.snake._state = GoUp(self.snake)
        elif np.array_equal(action, ACTION_LEFT_TURN):  # EXPLICIT
            self.snake._state = GoDown(self.snake)

        # if event[pygame.K_UP]:  # UP
        #     self.snake._state = GoUp(self.snake)
        # if event[pygame.K_DOWN]:  # DOWN
        #     self.snake._state = GoDown(self.snake)


class GoUp(SnakeState):
    def __init__(self, snake):
        self.snake = snake
        self._direction = DIRECTION_UP

    def move(self, increment):
        return (
            self.snake.get_head_position()[0],
            self.snake.get_head_position()[1] - increment,
        )

    def handle_input(self, action):
        if np.array_equal(action, ACTION_STRAIGHT):
            pass
            # self.snake._state = GoUp(self.snake)
        elif np.array_equal(action, ACTION_RIGHT_TURN):
            self.snake._state = GoRight(self.snake)
        elif np.array_equal(action, ACTION_LEFT_TURN):  # EXPLICIT
            self.snake._state = GoLeft(self.snake)

        # if event[pygame.K_RIGHT]:  # RIGHT
        #     self.snake._state = GoRight(self.snake)
        # if event[pygame.K_LEFT]:  # LEFT
        #     self.snake._state = GoLeft(self.snake)


class GoDown(SnakeState):
    def __init__(self, snake):
        self.snake = snake
        self._direction = DIRECTION_DOWN

    def move(self, increment):
        return (
            self.snake.get_head_position()[0],
            self.snake.get_head_position()[1] + increment,
        )

    def handle_input(self, action):
        if np.array_equal(action, ACTION_STRAIGHT):
            pass
            # self.snake._state = GoDown(self.snake)
        elif np.array_equal(action, ACTION_RIGHT_TURN):
            self.snake._state = GoLeft(self.snake)
        elif np.array_equal(action, ACTION_LEFT_TURN):  # EXPLICIT
            self.snake._state = GoRight(self.snake)
