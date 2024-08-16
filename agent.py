import numpy as np
import pygame
import torch
from game import *
from constants import *

moves = np.array(
    [
        ACTION_LEFT_TURN,
        ACTION_STRAIGHT,
        ACTION_STRAIGHT,
        ACTION_STRAIGHT,
        ACTION_STRAIGHT,
        ACTION_STRAIGHT,
        ACTION_STRAIGHT,
        ACTION_STRAIGHT,
        ACTION_STRAIGHT,
        ACTION_STRAIGHT,
        ACTION_STRAIGHT,
        ACTION_STRAIGHT,
        ACTION_STRAIGHT,
        ACTION_STRAIGHT,
        ACTION_STRAIGHT,
        ACTION_RIGHT_TURN,
        ACTION_STRAIGHT,
        ACTION_STRAIGHT,
        ACTION_STRAIGHT,
        ACTION_STRAIGHT,
        ACTION_STRAIGHT,
        ACTION_STRAIGHT,
        ACTION_STRAIGHT,
        ACTION_STRAIGHT,
        ACTION_STRAIGHT,
        ACTION_STRAIGHT,
        ACTION_STRAIGHT,
        ACTION_STRAIGHT,
        ACTION_RIGHT_TURN,
        ACTION_STRAIGHT,
        ACTION_STRAIGHT,
        ACTION_STRAIGHT,
        ACTION_STRAIGHT,
        ACTION_LEFT_TURN,
        ACTION_STRAIGHT,
        ACTION_STRAIGHT,
        ACTION_STRAIGHT,
        ACTION_STRAIGHT,
        ACTION_STRAIGHT,
        ACTION_STRAIGHT,
        ACTION_STRAIGHT,
        ACTION_RIGHT_TURN,
        ACTION_STRAIGHT,
        ACTION_STRAIGHT,
        ACTION_STRAIGHT,
        ACTION_STRAIGHT,
        ACTION_STRAIGHT,
        ACTION_STRAIGHT,
        ACTION_STRAIGHT,
        ACTION_RIGHT_TURN,
        ACTION_STRAIGHT,
        ACTION_STRAIGHT,
        ACTION_STRAIGHT,
        ACTION_STRAIGHT,
        ACTION_STRAIGHT,
        ACTION_STRAIGHT,
        ACTION_STRAIGHT,
        ACTION_RIGHT_TURN,
        ACTION_STRAIGHT,
        ACTION_STRAIGHT,
        ACTION_STRAIGHT,
        ACTION_STRAIGHT,
        ACTION_STRAIGHT,
        ACTION_STRAIGHT,
        ACTION_STRAIGHT,
        ACTION_RIGHT_TURN,
        ACTION_STRAIGHT,
        ACTION_STRAIGHT,
        ACTION_STRAIGHT,
        ACTION_STRAIGHT,
        ACTION_STRAIGHT,
        ACTION_STRAIGHT,
        ACTION_STRAIGHT,
        ACTION_STRAIGHT,
        ACTION_STRAIGHT,
        ACTION_STRAIGHT,
        ACTION_STRAIGHT,
        ACTION_STRAIGHT,
        ACTION_STRAIGHT,
        ACTION_STRAIGHT,
        ACTION_STRAIGHT,
        ACTION_STRAIGHT,
        ACTION_STRAIGHT,
        ACTION_STRAIGHT,
        ACTION_STRAIGHT,
        ACTION_STRAIGHT,
        ACTION_STRAIGHT,
        ACTION_STRAIGHT,
        ACTION_STRAIGHT,
        ACTION_STRAIGHT,
        ACTION_STRAIGHT,
        ACTION_STRAIGHT,
        ACTION_STRAIGHT,
        ACTION_STRAIGHT,
        ACTION_STRAIGHT,
        ACTION_STRAIGHT,
        ACTION_STRAIGHT,
        ACTION_STRAIGHT,
        ACTION_STRAIGHT,
        ACTION_STRAIGHT,
        ACTION_STRAIGHT,
    ]
)


def get_action_from_keys():
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        return [1, 0, 0]
    elif keys[pygame.K_LEFT]:
        return [0, 0, 1]
    elif keys[pygame.K_RIGHT]:
        return [0, 1, 0]
    else:
        pass

if __name__ == '__main__':
    game = SnakeGame()
    idx = 0

    while True:
        action = get_action_from_keys()
        # reward, game_over, score = game.play(moves[idx])
        reward, game_over, score = game.play(action) 
        print(f"Reward: {reward}") 

        idx += 1
        print(game.get_state())
        if game_over: break

    print(f"Your score: {score}") 
