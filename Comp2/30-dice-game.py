import os
import random
import time

playAgain = True
player_names = []
player_dice = [""] * 6
dice_keep = list()
num_list = list()
dice_total = 0
play_again = True
count = 0

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
input("Press 'enter' to start")
os.system('clear')

player_amount = int(input("How many people are playing:\n>"))
while player_amount < 1:
    player_amount = int(input("How many people are playing:\n>"))
player_amount = 2
usr_scores = [30] * player_amount
for i in range(player_amount):
    player_names.append(input("Player " + str(len(player_names) + 1) + ":\n>"))
os.system('clear')


def roll_dice():
    global num_list
    for i in range(len(player_dice)):
        player_dice[i] = random.randint(1, 6)

    print(f"Roll \033[1;32;48m{player_dice}")
    print(f"\033[1;0;48mList \033[1;34;48m{num_list} \033[1;0;48m")


def player_roll(z):
    global dice_keep, player_dice, num_list, player_amount
    print(f"{player_names[z]}'s turn! ")
    input("Press 'enter' to roll.\n")

    roll_dice()

    usr_input = int(input("How many dice do you want to keep?\n>"))
    while usr_input > len(player_dice) or usr_input < 1:
        print("Invalid Input\n")
        usr_input = int(input("How many dice do you want to keep?\n>"))

    if usr_input == len(player_dice):
        dice_keep = player_dice + dice_keep
    else:
        for i in range(usr_input):
            usr_input2 = int(input("Dice #?\n>"))
            while usr_input2 >= len(player_dice):
                print("Invalid #\n")
                usr_input2 = int(input("Dice #?\n>"))
            dice_keep.append(player_dice[usr_input2])

    for i in range(usr_input):
        player_dice.pop()

    print(f"\nDice you've kept. \n{dice_keep}\n")
    time.sleep(2)
    if len(dice_keep) < 6:
        for i in range(usr_input):
            num_list.pop(len(num_list) - 1)
        player_roll(z)
        os.system('clear')
    else:
        print(f"Your points this round {sum(dice_keep)}")
        if sum(dice_keep) == 30:
            print("You are safe")
        elif sum(dice_keep) > 30:
            attack_roll(z)
        player_dice = '' * 6
        time.sleep(3)


def attack_roll(z):
    global dice_keep, player_dice
    player_dice = [""] * 6
    object_number = sum(dice_keep) - 30
    dice_keep = list()
    num_count = 1
    print("Attack roll!")
    while len(dice_keep) < 6 and num_count > 0:
        num_count = 0
        roll_dice()
        for i in range(len(player_dice)):
            if player_dice[i] == object_number:
                dice_keep.append(player_dice[i])
                num_count += 1
        for i in range(num_count):
            player_dice.pop()
        print("You currently have " + str(len(dice_keep)) + " " + str(object_number) + "'s")
        input("Press 'enter' to roll again")
    if z + 1 == len(usr_scores):
        usr_scores[0] -= len(dice_keep) * object_number
    else:
        usr_scores[z + 1] -= len(dice_keep) * object_number
    print("You take " + str(len(dice_keep) * object_number) + " points from you opponent!")
    dice_keep = [6, 6, 6, 6, 6, 6]


while playAgain:
    while count != len(player_names) - 1:
        for i in range(player_amount):
            os.system('clear')
            num_list = [0, 1, 2, 3, 4, 5]
            for u in range(len(usr_scores)):
                print("								" + player_names[u] + "'s Score:")
                print("									" + str(usr_scores[u]))
            player_roll(i)
            if sum(dice_keep) < 30:
                usr_scores[i] += sum(dice_keep) - 30
            player_dice = [""] * 6
            dice_keep = list()
            num_list = list()
            count = 0
            for u in range(len(usr_scores)):
                if usr_scores[u] < 1:
                    count += 1
            if count == len(player_names) - 1:
                break
    highest = 0
    high_player = -1
    for u in range(len(usr_scores)):
        if usr_scores[u] > highest:
            highest = usr_scores[u - 1]
            high_player = u
        print(player_names[u] + " wins!")
    playAgain = input("Would you like to play again (Y/N):\n>")
    if playAgain.upper() == "NO" or playAgain.upper() == "N":
        print("Thank you for playing!")
        break
    else:
        player_dice = [""] * 6
        dice_keep = list()
        num_list = list()
        usr_scores = [30] * player_amount
        lowest = 30
