# welcome message
# rules or number code of the game
# ask player to input a number 
# confirm player's choice
# display computer's choice
# 0 for rock, 5 for paper, 2 for scissors
# define a function that enables computer pick randomly from 0,2 and 5
# ensure player chooses only from 0,2 and 5 and not any other number
# def a function to know when it's a win or loss or tie 
# rock beats scissors, scissors beats paper and paper beats rock


import random

intro = input("Hello there! Choose: \n 0 for rock, \n 2 for scissors or \n 5 for paper \n\n Please choose a number: \n")

player_choice = int(intro)
computer_choice =int(random.choice("025"))

if player_choice != 0 and player_choice != 2 and player_choice != 5:
    print("you can only choose from 0, 2 and 5.")  
else:
    print(f"\nyou chose {player_choice}")
    print(f"computer chose {computer_choice} \n")

if player_choice == computer_choice:
    print("tie!")
elif player_choice == 0 and computer_choice == 2: 
    print("you win!")
elif player_choice == 2 and computer_choice == 5:
    print("you win!")
elif player_choice == 5 and computer_choice == 0:
    print("you win!")
else:
    print("computer wins!")

print("\nplay again.")
