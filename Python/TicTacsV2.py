import random

play = True
playerMoves = []
one = "_"; two ="_"; three ="_"; four ="_"; five = "_"; six ="_"; seven = ""; eight =""; nine =""

def playerMove():
    global one, two, three, four, five, six, seven, eight, nine
    userin = int(input("Enter your position [1 - 9]"))
    if userin == 1:
        print(one)
        if one != "X" or two != "O":
            one = "X"
            print("Hello")
        else:
            print("Existing Symbol")
    elif userin == 2:
        if two != "X" or two != "O":
            two = "X"
        else:
            print("Existing Symbol")
    elif userin == 3:
        if three != "X":
            three = "X"
        else: 
            print("Existing Symbol")

    elif userin == 4:
        if four != "X":
            four = "X"

    elif userin == 5:
        if five != "X":
            five = "X"

    elif userin == 6:
        if six != "X":
            six = "X"

    elif userin == 7:
        if seven != "X":
            seven = "X"
    elif userin == 8:
        if eight != "X":
            eight = "X"
    elif userin == 9:
        if nine != "X":
            nine = "X"
    else:
        print('Invalid Input')
def board():
   print(f"_{one}_|_{two}_|_{three}_\n_{four}_|_{five}_|_{six}_\n {seven}  | {eight}  | {nine}\n")

board()

user = input("What is your name?\n")
while play == True:
    playerMove()
    board()
