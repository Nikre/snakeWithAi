import pygame
from food import *
from snake_body import *
from constants import *


def score():
    # TODO: screare una funzione per il calcolo dello score
    pass

def draw_food(food):
    pygame.draw.circle(screen, "red", food.get_food_position(), CIRCLE_DIAMITER)


# pygame setup
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
running = True
dt = 0
snake = SnakeBody()
food = Food()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    pygame.display.set_caption(f"Snake Game - Score: {dt}")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill(color=(53, 53, 53))

    # TODO: wrappare in draw snake
    pygame.draw.circle(screen, "green", snake.position, CIRCLE_DIAMITER)
    draw_food(food)

    keys = pygame.key.get_pressed()
    snake.move(increment=10)
    snake.change_direction(keys)
    running = not snake.check_collision(WINDOW_WIDTH, WINDOW_HEIGHT)
    pygame.display.flip()

    dt = clock.tick(FPS) / 1000

pygame.quit()
