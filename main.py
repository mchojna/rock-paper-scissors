"""
Title: Rock Paper Scissors
Author: Michał Chojna
Date: 04.06.2022
Description: Rock paper scissors game
"""
# Imports modules
import random

# Graphic representation of the rock
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

# Graphic representation of the paper
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

# Graphic representation of the scissors
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Creates list of the figures
image = [rock, paper, scissors]

# Takes the player's decision which figure to choose
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors. "))

# Checks if player typed available number
if player_choice in [0, 1, 2]:

    # If player typed available number
    # Prints graphic representation of player's figure
    print(image[player_choice])

    # Computer randomly chooses figure to play
    computer_choice = random.randint(0, 2)

    # Prints computer's decision
    print("Computer chose:")

    # Prints computer's figure
    print(image[computer_choice])

    # Check the result of the game
    # Check if the player's figure and computer's figure are the same
    if player_choice == computer_choice:

        # If player's figure and computer's figure are the same
        # Prints that there is a draw
        print("It is a draw.")

    # Check if the player wins
    elif (player_choice == 0 and computer_choice == 2) or (player_choice == 1 and computer_choice == 3) or (
            player_choice == 2 and computer_choice == 1):

        # If player wins
        # Prints that plyer wins
        print("You win.")

    # Otherwise computer wins
    else:

        # Prints that computer wins
        print("You lose.")

# If player types unavailable number loses
else:
    # Prints that player loses
    print("You typed an invalid number, you lose.")
