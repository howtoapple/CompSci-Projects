import os
import random
import turtle

cases = [.01, 1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750, 1000, 5000, 10000, 25000, 50000, 75000, 100000,
         200000, 300000, 400000, 500000, 750000, 1000000]
cases2 = []
pickedCases = []
keptCase = 0
roundNum = 0
caseAmount = 7

t = [" "]

for i in range(26):
    t.append(turtle.Turtle())
    t[i + 1].speed(0)

print("Welcome to Deal or No Deal!")
print("1. The primary objective of the game is to get the most money possible")
print("2. At the start of the game, you pick a case that you keep until the end")
print("3. During the rest of the game, you will be asked to pick a certain amount")
print("	of cases. When you pick a case, an amount will be revealed, and that")
print("	amount will be unavailable.")
print("4. After you've picked the cases, you will be offered an amount and you")
print("	have to decide whether you think the amount in your case is larger by")
print("	saying either 'Deal', or 'No deal'")
print("5. The game ends when you accept a deal or run out of cases to pick\n")

input("Press 'Enter' to continue")
os.system('clear')


# Shuffles the case amount to be assigned to case numbers
# cases2 is the shuffled version
def shuffle():
    global cases, cases2
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
    cases2 = [' '] * 26
    for x in range(26):
        cases2[x] = random.choice(numbers)
        numbers.remove(cases2[x])
    for x in range(26):
        cases2[x] = cases[cases2[x]]


# boxes display
wn = turtle.Screen()
t = [" 0 "]

for i in range(26):
    t.append(turtle.Turtle())
    t[i + 1].hideturtle()

# positioning
wn.tracer(0)
for i in range(5):
    t[i + 1].penup()
    t[i + 1].sety(70 * i)
    t[i + 1].pendown()
for i in range(5):
    t[i + 6].penup()
    t[i + 6].setx(70)
    t[i + 6].sety(70 * i)
    t[i + 6].pendown()
for i in range(5):
    t[i + 11].penup()
    t[i + 11].setx(140)
    t[i + 11].sety(70 * i)
    t[i + 11].pendown()
for i in range(5):
    t[i + 16].penup()
    t[i + 16].setx(210)
    t[i + 16].sety(70 * i)
    t[i + 16].pendown()
for i in range(6):
    t[i + 21].penup()
    t[i + 21].setx(280)
    t[i + 21].sety(70 * i)
    t[i + 21].pendown()

for i in range(26):

    t[i + 1].begin_fill()
    for u in range(4):
        t[i + 1].forward(50)
        t[i + 1].left(90)
    t[i + 1].end_fill()
    t[i + 1].color('white')
# number
for i in range(26):
    t[i + 1].penup()
    t[i + 1].forward(25)
    t[i + 1].left(90)
    t[i + 1].forward(25)
    t[i + 1].pendown()
    t[i + 1].write(i + 1, font=("Calibri", 10, "bold"))

kepC = turtle.Turtle()
kepC.hideturtle()

kepC.penup()
kepC.goto(150, -100)
kepC.pendown()
kepC.write("Case Kept")
for i in range(4):
    kepC.forward(70)
    kepC.left(90)
kepC.penup()
kepC.forward(10)
kepC.left(90)
kepC.forward(10)

wn.tracer(1)

shuffle()
keptCase = int(input("Which case would you like to keep?\n>"))
while keptCase < 1 or keptCase > 26:
    os.system('clear')
    print("Which case would you like to keep?")
    keptCase = int(input("Must be between 1 and 26\n>"))

t[keptCase].clear()
kepC.pendown()
kepC.begin_fill()
for u in range(4):
    kepC.forward(50)
    kepC.right(90)

kepC.end_fill()

kepC.color('white')
kepC.penup()
kepC.forward(25)
kepC.right(90)
kepC.forward(25)
kepC.pendown()
kepC.write(keptCase, font=("Calibri", 10, "bold"))

pickedCases.append(keptCase)

while True:
    roundNum += 1
    if caseAmount > 1:
        caseAmount -= 1
    os.system('clear')
    if len(pickedCases) < 25:
        print("You will pick " + str(caseAmount) + " case(s) this round")
        print()
        for i in range(caseAmount):
            av = []
            avam = []
            for i in range(26):
                numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
                           26]
                if numbers[i] not in pickedCases:
                    av.append(i + 1)
                if cases[i] != 0:
                    avam.append(cases[i])
            print("Available cases: " + str(av))
            print("Amounts left: " + str(avam))
            print()
            pickCase = int(input("Please pick a case\n>"))

            while pickCase in pickedCases:
                print("You have already picked that case.")
                pickCase = int(input("Please pick a case\n>"))

            while pickCase < 1 or pickCase > 26:
                print("That is not a case number")
                pickCase = int(input("Please pick a case\n>"))

            pickedCases.append(pickCase)
            t[pickCase].clear()
            print("There was " + str(cases2[pickCase - 1]) + " in that case")

            for i in range(26):
                if cases[i] == cases2[pickCase - 1]:
                    cases[i] = 0
            input("Press 'Enter' to continue")
            os.system('clear')
        sum = 0
        caseNum = 28 - len(pickedCases)
        for i in range(26):
            sum += cases[i] ** 2
        sum = sum / caseNum
        sum = sum ** .5
        sum = sum / 10 * 7
        sum = round(sum, 2)
        print("The banker offers " + str(sum) + " dollars")
        dOND = input("Deal or No Deal? \n>")
        while dOND.upper() != "DEAL" and dOND.upper() != "NO DEAL":
            print("The banker offers " + str(sum) + " dollars")
            dOND = input("Deal or No Deal? \n>")
        if dOND.upper() == "DEAL":
            print("You win " + str(sum))
            break
    else:
        for i in range(26):
            numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
            if numbers[i] not in pickedCases:
                lastCase = i
        print("There is one case left, case " + str(lastCase))
        print("You kept case " + str(keptCase))
        keepOrSwitch = input("Would you like to keep your case or switch (Keep, Switch)\n>")
        while keepOrSwitch.upper() != "KEEP" and keepOrSwitch.upper() != "SWITCH":
            os.system('clear')
            print("There is one case left, case " + str(lastCase))
            print("You kept case " + str(keptCase))
            keepOrSwitch = input("Would you like to keep your case or switch (Keep, Switch)\n>")
        if keepOrSwitch.upper() == "KEEP":
            print("You win " + str(cases2[keptCase - 1]))
            break
        else:
            print("You win " + str(cases2[lastCase]))
            break
