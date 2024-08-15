import pygame
from snake_body import *
from constants import *

# pygame setup
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
running = True
dt = 0
snake = SnakeBody()


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill(color=(53, 53, 53))

    # wrappare in drow snake
    pygame.draw.circle(screen, "red", snake.position, CIRCLE_DIAMITER)

    keys = pygame.key.get_pressed()
    snake.move(increment=10)
    snake.change_direction(keys)
    running = not snake.check_collision(WINDOW_WIDTH, WINDOW_HEIGHT)
    print(running)
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(FPS) / 1000

pygame.quit()
