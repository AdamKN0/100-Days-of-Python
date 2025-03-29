from SnakeGame import SnakeGame
from Food import Food
from Score import Score

if __name__ == "__main__":
    score = Score()
    food = Food()
    game = SnakeGame(food, score)
    game.run_game()
