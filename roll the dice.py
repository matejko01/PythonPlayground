import random

play_game = True

def roll_the_dice():
    dice = random.randint(0, 7)
    print(f"Result: {dice}")

player_answer = input("Would you like to roll the dice? (1: yes, 2: no)")

while play_game == True:
    if player_answer == "1":
        roll_the_dice()
        player_answer = input("Would you like to roll the dice again? (1: yes, 2: no)")
    elif player_answer == "2":
        print("pity")
        play_game = False
    else:
        player_answer = input("Would you like to roll the dice? (1: yes, 2: no)")
    