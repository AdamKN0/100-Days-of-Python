from SnakeGame import SnakeGame
from Food import Food
from Score import Score

if __name__ == "__main__":
    food = Food()
    score = Score()
    game = SnakeGame(food, score)
    game.run_game()
