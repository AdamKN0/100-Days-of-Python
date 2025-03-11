import random

print("Welcome to the Hangman Game.")
list_of_words = ["python", "java", "kotlin", "javascript"]
word = random.choice(list_of_words)
display = ["_"] * len(word)
print("".join(display))
tries = 0

while "_" in display:
    guess = input("Guess a letter: ").lower()
    for i in range(len(word)):
        if guess == word[i]:
            display[i] = word[i]
    print("".join(display))
    tries += 1

print(f"You win after {tries} tries!")