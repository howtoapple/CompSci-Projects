import random

play = 1
playerMoves = []
one = "_"; two ="_"; three ="_"; four ="_"; five = "_"; six ="_"; seven = ""; eight =""; nine =""


def playerMove():
    userin = int(input("Enter your position [1 - 9]"))
    if userin == 1 and one != "O":
        one = "X"
        playerMoves.append()
    elif userin == 2 and two != "O":
        two = "X"
        playerMoves.append()
    elif userin == 3 and three != "O":
        three = "X"
        playerMoves.append()
    elif userin == 4 and four != "O":
        four = "X"
        playerMoves.append()
    elif userin == 5 and five != "O":
        five = "X"
        playerMoves.append()
    elif userin == 6 and six != "O":
        six = "X"
    elif userin == 7 and seven != "O":
        seven = "X"
    elif userin == 8 and eight != "O":
        eight = "X"
    elif userin == 9 and nine != "0":
        nine = "X"
    else:
        print('Invalid Input')
def board():
   print(f"_{one}_|_{two}_|_{three}_\n_{four}_|_{five}_|_{six}_\n {seven} | {eight} | {nine}\n")





board()


user = input("What is your name?")
