import pygame
from food import *
from snake import *
from constants import *


def score():
    # TODO: screare una funzione per il calcolo dello score
    pass

def draw_food(food):
    pygame.draw.circle(screen, "red", food.get_food_position(), CIRCLE_RADIUS)

def draw_snake(snake):
    for section in snake.body:
        pygame.draw.circle(screen, "green", section, CIRCLE_RADIUS)

def check_eaten_food(snake, food):
    if snake.get_head_position() == food.get_food_position():
        snake.eat(CIRCLE_RADIUS * 2)
        food.food_eaten()

def check_collision(snake, width, height):
    return (
        True
        if snake.get_head_position()[0] >= width
        or snake.get_head_position()[0] <= 0
        or snake.get_head_position()[1] >= height
        or snake.get_head_position()[1] <= 0
        else False
    )


# pygame setup
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
running = True
dt = 0
snake = Snake()
food = Food()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    pygame.display.set_caption(f"Snake Game - Score: {len(snake.body)}")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            snake.change_direction(pygame.key.get_pressed())
    # fill the screen with a color to wipe away anything from last frame
    screen.fill(color=(53, 53, 53))

    keys = pygame.key.get_pressed()
    snake.move(CIRCLE_RADIUS*2)
    check_eaten_food(snake, food)
    draw_snake(snake)
    draw_food(food)

    if check_collision(snake, WINDOW_WIDTH, WINDOW_HEIGHT) or snake.is_self_eaten():
        running = False

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
