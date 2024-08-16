from agent import *
from game import *
from helper import plot

if __name__ == "__main__":
    plot_scores = []
    plot_mean_scores = []
    total_score = 0
    record = 0
    agent = Agent()
    game = SnakeGame()

    while True:
        # get old state
        current_state = game.get_state()

        # get move
        move = agent.get_action(current_state)

        # perform move and get new state
        reward, game_over, score = game.play(move)
        new_state = game.get_state()

        # train short memory
        agent.train_short_memory(current_state, move, reward, new_state, game_over)

        # remember
        agent.remember(current_state, move, reward, new_state, game_over)

        if game_over:
            # train long memory, plot result
            print("GAME OVER!\n")
            game.set_new_game()
            agent.n_games += 1
            agent.train_long_memory()

            if score > record:
                record = score
                agent.model.save()

            print("Game", agent.n_games, "Score", score, "Record:", record)

            plot_scores.append(score)
            total_score += score
            mean_score = total_score / agent.n_games
            plot_mean_scores.append(mean_score)
            plot(plot_scores, plot_mean_scores)
