import random
valid_Input = ["r", "p", "s", "R", "P", "S"]
user = input("What is your name?\n")
def choice():
    global tendency
    tendency = []
    tendency.append(choices)
  
choices = [];choices = input("Your Turn...\n[R] Rock\n [P] Paper\n [S] Scissors\n");choices=choices.upper()
tendency[0]=(choices.count('R')/len(choices)*100);tendency[1]=(choices.count('P')/len(choices)*100);tendency[2]=(choices.count('S')/len(choices*100))
print(tendency)
