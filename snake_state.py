import pygame
from abc import ABC, abstractmethod


class SnakeState(ABC):
    @abstractmethod
    def move(self, snake, increment):
        pass

    @abstractmethod
    def handle_input(self, snake, event):
        pass


class InitialState(SnakeState):
    def __init__(self, snake):
        self.snake = snake

    def move(self, increment):
        pass

    def handle_input(self, event):
        if event[pygame.K_UP]:  # UP
            self.snake._state = GoUp(self.snake)
        if event[pygame.K_DOWN]:  # DOWN
            self.snake._state = GoDown(self.snake)
        if event[pygame.K_RIGHT]:  # RIGHT
            self.snake._state = GoRight(self.snake)
        if event[pygame.K_LEFT]:  # LEFT
            self.snake._state = GoLeft(self.snake)


class GoRight(SnakeState):
    def __init__ (self, snake):
        self.snake = snake
        # self.snake._direction = (1, 0) # direzione iniziale dx

    def move(self, increment):
        self.snake.position.x += increment

    def handle_input(self, event):
        if event[pygame.K_UP]: # UP
            self.snake._state = GoUp(self.snake)
        if event[pygame.K_DOWN]: # DOWN
            self.snake._state = GoDown(self.snake)


class GoLeft(SnakeState):
    def __init__ (self, snake):
        self.snake = snake

    def move(self, increment):
        self.snake.position.x -= increment

    def handle_input(self, event):
        if event[pygame.K_UP]:  # UP
            self.snake._state = GoUp(self.snake)
        if event[pygame.K_DOWN]:  # DOWN
            self.snake._state = GoDown(self.snake)

class GoUp(SnakeState):
    def __init__ (self, snake):
        self.snake = snake

    def move(self, increment):
        self.snake.position.y -= increment

    def handle_input(self, event):
        if event[pygame.K_RIGHT]:  # RIGHT
            self.snake._state = GoRight(self.snake)
        if event[pygame.K_LEFT]:  # LEFT
            self.snake._state = GoLeft(self.snake)

class GoDown(SnakeState):

    def __init__(self, snake):
        self.snake = snake

    def move(self, increment):
        self.snake.position.y += increment

    def handle_input(self, event):
        if event[pygame.K_RIGHT]:  # RIGHT
            self.snake._state = GoRight(self.snake)
        if event[pygame.K_LEFT]:  # LEFT
            self.snake._state = GoLeft(self.snake)
