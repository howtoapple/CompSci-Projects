import random

play = 1
playerMoves = []
one = "_"; two ="_"; three ="_"; four ="_"; five = "_"; six ="_"; seven = ""; eight =""; nine =""


def playerMove():
    global one, two, three, four, five, six, seven, eight, nine
    userin = int(input("Enter your position [1 - 9]"))
    if userin == 1 and one != "O" or "X":
        one = "X"
        print("Hello World")
    elif userin == 2 and two != "O" or "X":
        two = "X"

    elif userin == 3 and three != "O" or "X":
        three = "X"

    elif userin == 4 and four != "O" or "X":
        four = "X"

    elif userin == 5 and five != "O" or "X":
        five = "X"

    elif userin == 6 and six != "O" or "X":
        six = "X"
    elif userin == 7 and seven != "O" or "X":
        seven = "X"
    elif userin == 8 and eight != "O" or "X":
        eight = "X"
    elif userin == 9 and nine != "O" or "X":
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
