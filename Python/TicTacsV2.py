import random

play = True
playerMoves = []
one = "_"; two ="_"; three ="_"; four ="_"; five = "_"; six ="_"; seven = ""; eight =""; nine =""

#Executes and Validates player's moveset
def playerMove():
    global one, two, three, four, five, six, seven, eight, nine
    userin = int(input("Enter your position [1 - 9]"))
    if userin == 1 and one != "X":
        print(one)
        if one != "O":
            one = "X"
            print("Hello")
        else:
            print("Existing Symbol")
    elif userin == 2 and two != "X":
        if two != "O":
            two = "X"
        else:
            print("Existing Symbol")
    elif userin == 3 and three != "X":
        if three != "O":
            three = "X"
        else: 
            print("Existing Symbol")
    elif userin == 4 and four != "X":
        if four != "O":
            four = "X"
            print("Existing Symbol")
    elif userin == 5 and five != "X":
        if five != "O":
            five = "X"
            print("Exisiting Symbol")
    elif userin == 6 and six != "X":
        if six != "O":
            six = "X"
            print("Existing Symbol")
    elif userin == 7 and seven != "X":
        if seven != "O":
            seven = "X"
            print("Existing Symbol")
    elif userin == 8 and eight != "X":
        if eight != "O":
            eight = "X"
            print("Existing Symbol")
    elif userin == 9 and nine != "X":
        if nine != "O":
            nine = "X"
            print("Exisitng Symbol")
    else:
        print('Invalid Input')

#Check player Win Cond
def p_win():
    if one =="X":
        if two =="X" and three =="X":
            print(f"{user} wins!")
        elif four =="X" and seven =="X":
            print(f"{user} wins!")
        elif five =="X" and nine =="X":
            print(f"{user} wins!")
    elif 


#Check Computer Win Cond
def comp_win():
    pass


#Computer behaviour
def comp():
    pass

def board():
   print(f"_{one}_|_{two}_|_{three}_\n_{four}_|_{five}_|_{six}_\n {seven}  | {eight}  | {nine}\n")

board()

user = input("What is your name?\n")
while play == True:
    playerMove()
    board()
