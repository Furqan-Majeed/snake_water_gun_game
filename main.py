# Snake, Water, Gun Game 
# concept same as Stone Paper Scissor

# Below Are The Mathematical Value Assign For Choices
'''
1 is for snake 
-1 is for water
0 is for gun
'''
import random

# Assign a random choice to the computer variable: -1 for Water, 0 for Gun, 1 for Snake
computer = random.choice([-1, 0, 1])

# User input
youstr = input("Enter your choice (s for Snake, w for Water, g for Gun): ").lower()

# Dictionaries to map user input to numbers and numbers to readable choices
youDict = {
    "s": 1,
    "w": -1,
    "g": 0,
}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

# Get the user's choice in numerical form
you = youDict[youstr]

# Print both the user's choice and the computer's choice in readable form
print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

# Check if the game is a draw
if computer == you:
    print("It's a draw")

# If not a draw, determine the winner
else:
    if computer == -1 and you == 0:
        print("You lose!")  # Computer: Water, You: Gun
    elif computer == -1 and you == 1:
        print("You win!")   # Computer: Water, You: Snake
    elif computer == 1 and you == 0:
        print("You win!")   # Computer: Snake, You: Gun
    elif computer == 1 and you == -1:
        print("You lose!")  # Computer: Snake, You: Water
    elif computer == 0 and you == 1:
        print("You lose!")  # Computer: Gun, You: Snake
    elif computer == 0 and you == -1:
        print("You wign!")   # Computer: Gun, You: Water

