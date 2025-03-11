print("Welcome to the Treasure Island!\nYour mission is to find the hidden treasure.\n")
print("You're at a crossroad. Where do you want to go? Type 'left' or 'right'")
direction = input().lower()

if direction == "left":
    print("You come to a serene lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat or 'swim' to swim across.")
    action = input().lower()
    if action == "wait":
        print("You patiently wait and a boat arrives. You sail to the island unharmed. There is a house with 3 doors: one red, one yellow, and one blue. Which color do you choose?")
        door = input().lower()
        if door == "yellow":
            print("Congratulations! You found the treasure! You Win!")
        elif door == "red":
            print("Oh no! It's a room full of fire. Game Over.")
        elif door == "blue":
            print("You enter a room of wild beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    elif action == "swim":
        print("You bravely attempt to swim across but get attacked by an angry trout. Game Over.")
    else:
        print("Invalid choice. Game Over.")
elif direction == "right":
    print("You walk into a dense forest and get lost. Game Over.")
else:
    print("Invalid choice. Game Over.")