from random import randint
print("Welcome to Rock Paper Scissors Game!")
print("Please enter your choice: (1) Rock, (2) Paper, (3) Scissors")
player_choice = int(input("Enter your choice: "))
if player_choice < 1 or player_choice > 3:
	print("Invalid choice. Please enter a number between 1 and 3.")
	exit()
computer_choice = randint(1, 3)
if player_choice == computer_choice:
	print("It's a tie!")
elif player_choice == 1:
	if computer_choice == 2:
		print("Computer wins!")
	else:
		print("Player wins!")
elif player_choice == 2:
	if computer_choice == 3:
		print("Computer wins!")
	else:
		print("Player wins!")
else:
	if computer_choice == 1:
		print("Computer wins!")
	else:
		print("Player wins!")
print("Player choice:", player_choice)
print("Computer choice:", computer_choice)
