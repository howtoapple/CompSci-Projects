import random
import time
import os

player_name = ""
player2_name = ""
playAgain = True
player_dice = [""] * 6
player2_dice = [""] * 6
dice_keep = list()
dice_keep2 = list()
num_list = list()
diceTotal, diceTotal2 = 0, 0
play_again = True
u_score, u2_score = 30, 30

print("Welcome to 30!"
      "\nIn this game you roll 6 dice, and decide which ones to keep"
      "\nYou must keep one dice per roll, but you may choose more"
      "\nYou must have a score of at least 30 by the time all dice are kept or you lose points"
      "\nYou lose the amount you missed 30 by"
      "\nIf you score more than 30, you have the chance to subtract from your opponents score"
      "\nYou'll roll to get the number you got above thirty, if you get none on a roll the attack roll ends"
      "\nThe amount of dice you manage to match are multiplied by the number you're rolling for,"
      "\nand then subtracted from the opponents score\n")

print("Have fun!")
input("Press enter to start")
os.system('clear')

player_name = str(input("Player 1's Name:\n>"))
player2_name = str(input("Player 2's name:\n>"))
os.system('clear')


def roll_dice():
    global num_list
    for i in range(len(player_dice)):
        player_dice[i] = random.randint(1, 6)
        num_list.append(i)

    print(f"Roll \033[1;32;48m{player_dice}")
    print(f"\033[1;0;48mList \033[1;34;48m{num_list} \033[1;0;48m")


def roll_dice2():
    for i in range(len(player2_dice)):
        player2_dice[i] = random.randint(1, 6)
        num_list.append(i)

    print(f"Roll \033[1;32;48m{player_dice}")
    print(f"\033[1;0;48mList \033[1;32;48m{num_list} \033[1;0;48m")


def player_roll():
    global dice_keep, player_dice, num_list

    print(f"{player_name}'s turn! ")
    input("Press 'enter' to roll.")

    roll_dice()

    usr_input = int(input("How many dice do you want to keep?\n>"))
    while usr_input > 6:
        print("Invalid Input\n")
        usr_input = int(input("How many dice do you want to keep?\n>"))

    if usr_input == 6:
        dice_keep.append(player_dice)

    for i in range(usr_input):
        usr_input2 = int(input("Dice #?\n>"))
        dice_keep.append(player_dice[usr_input2])

    for i in range(usr_input):
        player_dice.pop()

    print(f"\nDice you've kept. \n{dice_keep}")
    time.sleep(2)

    if len(dice_keep) != 6:
        num_list.pop(all)
        player_roll()
        os.system('clear')
    else:
        print("Your points this round: " + sum(dice_keep))
        num_list.pop()
        player2_roll()


def player2_roll():
    print("Hello World!")


def attack_roll():
    global dice_keep, player_dice
    object_number = diceTotal - 30
    count = 1
    print("Attack roll!")
    while dice_keep < 6 and count > 0:
        count = 0
        roll_dice()
        for i in range(player_dice):
            if i == object_number:
                dice_keep.append(player_dice[i])
                count += 1
        for i in range(count):
            player_dice.pop()


# count = object_number * len(dice_keep)

player_roll()
