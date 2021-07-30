"""
4 August, 2020
-It is a gussing game with a scoreboard.
-Players can Sign up and track their success in the board.
-They can sign in using their id and passwords whenever.
-Players can play as long as they want to. Each game results
will be submitted to their history on the scoreboard

Story: Player has three chances to guess the summation
of two dices. First two wrong answers will return some guide.

The program was developed for below learning purposes:
- Using functions in the correct and Pythonic way.
- Designing a SQL database
- Connecting the game with the database

In order to use this program, one has to define the
needed tables in their MySql environment.

This file should be run in order to play.
"""

import random
from khoshgoman_sql import *


def dices():
    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    sum_of_dices = dice_1 + dice_2
    return dice_1, dice_2, sum_of_dices


def guess_check(guess, sum_of_dices):
    if guess == sum_of_dices:
        print("\n\n" + ("*" * 51) + "\n"
              + ("*" * 21) + "You won!"
              + ("*" * 21) + "\n" + ("*" * 51))
        check = True
    elif guess < sum_of_dices:
        print("The summation of dices is a greater number.")
        check = False
    else:
        print("The summation of dices is smaller than your guess.")
        check = False

    return check


def game(player):
    sum_of_dices = dices()
    # print(sum_of_dices[2])  # Gives the answer (just for testing)

    for i in range(3):
        print(f"You have {3 - i} chance(s).")
        guesses = int(input("Guess The summation of two dices: "))
        if guess_check(guesses, sum_of_dices[2]):
            enter_scoreboard(player, i + 1)
            break

    else:
        enter_scoreboard(player, 4)
        print(f"You lost 😑"
              f"\nFirst dice: {sum_of_dices[0]}"
              f"\nSecond dice: {sum_of_dices[1]}"
              f"\nThe summation: {sum_of_dices[2]}")


def menu():
    enter = input("Enter 'i' to sign in or any key to sign up: ")
    if enter == 'i':
        player = sign_in()
    else:
        player = sign_up()

    while True:
        if not player:
            command = 'n'
        else:
            command = input(f"Do you want to play {player}? (y/n) ")
        if command != "y" and command != "n":
            print("You have clicked the wrong key, try again.")
        elif command == "y":
            game(player)
        elif command == "n":
            print("\n\n" + ("*" * 51) + "\n"
                  + ("*" * 15) + f"HOPE TO SEE YOU SOON"
                  + ("*" * 16) + "\n" + ("*" * 51))
            break


if __name__ == "__main__":
    menu()
