import random

num1 = random.randint(0, 11)
player_is_correct = False
attempts = 0

while player_is_correct == False:
    player_input = input("Guess a number between 0 and 10: ")
    player_input = int(player_input)

    if player_input == num1:
        attempts += 1
        print(f"You are right! It took you {attempts} attempts!")
        player_is_correct = True
    else:
        attempts += 1
        if player_input > num1:
            print("Your number is too big!")
        else:
            print("Your number is too small!")

