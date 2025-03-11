import random
print("Welcome to the Number Guessing Game")

def set_difficulty():
	level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
	if level == "easy":
	    return 10
	elif level == "hard":
	    return 5
	else:
		print("Invalid input")
		exit()

def compare_numbers(guess, number):
	if guess < number:
		return "Too low."
	elif guess > number:
		return "Too high."
	else:
		return f"You got it! The number was {number}"

def game():
    print("I'm thinking of a number between 1 and 100")
    number = random.randint(1, 100)
    attempts = set_difficulty()
    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        print(compare_numbers(guess, number))
        if guess == number:
            break
        attempts -= 1
        if attempts == 0:
            print(f"You've run out of guesses, you lose. the number was {number}")
            break

game()