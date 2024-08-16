from game import *


if __name__ == '__main__':
    game = SnakeGame()

    while not game.game_over:
        game.play() 
    
    print(f"Your score: {game.score()}")
