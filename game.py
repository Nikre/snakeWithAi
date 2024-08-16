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
        self.frame_iteration += 1 # TODO
        self.reward = 0
        pygame.display.set_caption(f"Snake Game - Score: {self.score()}")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = True

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

    def _check_borders(self, window_width, window_height):
        x, y = self.snake.get_head_position()
        border_front = False
        border_right = False
        border_left = False
        if np.array_equal(self.snake.get_direction(), DIRECTION_RIGHT):
            border_front = x >= window_width
            border_right = y + CELL_SIZE >= window_height
            border_left = y - CELL_SIZE <= 0
        elif np.array_equal(self.snake.get_direction(), DIRECTION_LEFT):
            border_front = x <= 0
            border_right = y - CELL_SIZE <= 0
            border_left = y + CELL_SIZE >= window_height
        elif np.array_equal(self.snake.get_direction(), DIRECTION_UP): 
            border_front = y <= 0
            border_right = x + CELL_SIZE >= window_width
            border_left = x - CELL_SIZE <= 0
        elif np.array_equal(self.snake.get_direction(), DIRECTION_DOWN):
            border_front = y >= window_height
            border_right = x - CELL_SIZE <= 0
            border_left = x + CELL_SIZE >= window_width
        return border_front, border_right, border_left

    def _get_food_location(self):
        head = self.snake.get_head_position()
        food = self.food.get_food_position()

        r = food[0] > head[0]
        l = food[0] < head[0]
        u = food[1] < head[1]
        d = food[1] > head[1]

        return (r, l, u, d)

    def get_state(self):
        border_front, border_right, border_left = self._check_borders(
            WINDOW_WIDTH, WINDOW_HEIGHT
        )

        # Directions
        dir_l, dir_r, dir_u, dir_d = self.snake.get_direction()

        # Food
        food_r, food_l, food_u, food_d = self._get_food_location()

        state = (
            border_front,
            border_right,
            border_left,
            dir_l,
            dir_r,
            dir_u,
            dir_d,
            food_r,
            food_l,
            food_u,
            food_d,
        )
        return np.array(state, dtype=int)
