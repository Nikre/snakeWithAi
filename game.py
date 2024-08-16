import pygame
from food import *
from snake import *
from constants import *


class SnakeGame:

    def __init__(self) -> None:
        # pygame setup
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        self.set_new_game()

    def set_new_game(self):
        self.game_over = False
        self.reward = 0
        self.snake = Snake()
        self.food = Food()
        self.frame_iteration = 0

    def play(self, action):
        pygame.display.set_caption(f"Snake Game - Score: {self.score()}")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = False
        
        # fill the screen with a color to wipe away anything from last frame
        self.screen.fill(color=(53, 53, 53))
        self.snake.change_direction(action)

        self.snake.move(CIRCLE_RADIUS*2)
        self.check_eaten_food()
        self.draw_snake()
        self.draw_food()

        if self.check_collision(WINDOW_WIDTH, WINDOW_HEIGHT) or self.snake.is_self_eaten():
            self.game_over = True
            self.reward = -10

            # NOTE: not runnig vuol dire se c'è il game over
            return self.reward, self.game_over, self.score()

        pygame.display.flip()
        self.clock.tick(FPS)

        return self.reward, self.game_over, self.score()

    def score(self):
        return len(self.snake.body)

    def draw_food(self):
        pygame.draw.circle(self.screen, "red", self.food.get_food_position(), CIRCLE_RADIUS)

    def draw_snake(self):
        for section in self.snake.body:
            pygame.draw.circle(self.screen, "green", section, CIRCLE_RADIUS)

    def check_eaten_food(self):
        if self.snake.get_head_position() == self.food.get_food_position():
            self.snake.eat(CIRCLE_RADIUS * 2)
            self.food.food_eaten()
            self.reward = 10

    def check_collision(self, width, height):
        return (
            True
            if self.snake.get_head_position()[0] >= width
            or self.snake.get_head_position()[0] <= 0
            or self.snake.get_head_position()[1] >= height
            or self.snake.get_head_position()[1] <= 0
            else False
        )
