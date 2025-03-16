import random

print("Welcome to the Higher Lower Game!")
score = 0

data = {
    "facebook": {
        "name": "Facebook",
        "follower_count": 1001,
        "description": "Social media platform",
        "country": "United States",
    },
    "instagram": {
        "name": "Instagram",
        "follower_count": 1002,
        "description": "Social media platform",
        "country": "United States",
    },
    "cristiano": {
        "name": "Cristiano Ronaldo",
        "follower_count": 1003,
        "description": "Footballer",
        "country": "Portugal",
    },
    "beyonce": {
        "name": "Beyonce",
        "follower_count": 1004,
        "description": "Musician",
        "country": "United States",
    },
    "kyliejenner": {
        "name": "Kylie Jenner",
        "follower_count": 1005,
        "description": "Reality TV star",
        "country": "United States",
    },
    "therock": {
        "name": "Dwayne Johnson",
        "follower_count": 1006,
        "description": "Actor",
        "country": "United States",
    },
}

a = random.choice(list(data.keys()))
while True:
	b = random.choice(list(data.keys()))
	if a == b:
		b = random.choice(list(data.keys()))
	print(f"Compare A: {data[a]['name']}, a {data[a]['description']} from {data[a]['country']}")
	print("vs")
	print(f"Against B: {data[b]['name']}, a {data[b]['description']} from {data[b]['country']}")
	answer = input("Who has more followers? Type 'A' or 'B': ").lower()
	if answer == 'a':
		if data[a]['follower_count'] > data[b]['follower_count']:
			score += 1
			print(f"Your score is {score}")
			del data[b]
		else:
			print(f"Sorry, that's wrong. Your final score is {score}")
			break
	elif answer == 'b':
		if data[b]['follower_count'] > data[a]['follower_count']:
			score += 1
			print(f"Your score is {score}")
			del data
			a = b
		else:
			print(f"Sorry, that's wrong. Your final score is {score}")
			break
	else:
		print("Invalid input. Please type 'A' or 'B'")
		break
	if len(data) == 1:
		print("Congratulations! You have won the game.")
		break
