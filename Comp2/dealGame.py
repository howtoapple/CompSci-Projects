import turtle, random, os

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
    for i in range(26):
        cases2[i] = random.choice(numbers)
        numbers.remove(cases2[i])
    for i in range(26):
        cases2[i] = cases[cases2[i]]


# boxes display
wn = turtle.Screen()

t = []

for i in range(26):
    t.append(turtle.Turtle())

# positioning
wn.tracer(0)
for i in range(5):
    t[i].penup()
    t[i].sety(70 * i)
    t[i].pendown()
for i in range(5):
    t[i + 5].penup()
    t[i + 5].setx(70)
    t[i + 5].sety(70 * i)
    t[i + 5].pendown()
for i in range(5):
    t[i + 10].penup()
    t[i + 10].setx(140)
    t[i + 10].sety(70 * i)
    t[i + 10].pendown()
for i in range(5):
    t[i + 15].penup()
    t[i + 15].setx(210)
    t[i + 15].sety(70 * i)
    t[i + 15].pendown()
for i in range(6):
    t[i + 20].penup()
    t[i + 20].setx(280)
    t[i + 20].sety(70 * i)
    t[i + 20].pendown()

for i in range(26):

    for u in range(4):
        t[i].forward(50)
        t[i].left(90)
# number
t[25].penup()
t[25].goto(310, 375)
t[25].pendown()
t[25].write(1)
wn.tracer(1)

t[0].setx(100)

shuffle()
keptCase = int(input("Which case would you like to keep?\n>"))
while keptCase < 1 or keptCase > 26:
    os.system('clear')
    print("Which case would you like to keep?")
    keptCase = int(input("Must be between 1 and 26\n>"))
pickedCases.append(keptCase)
while True:
    roundNum += 1
    if caseAmount > 1:
        caseAmount -= 1
    os.system('clear')
    print("You will pick " + str(caseAmount) + " cases this round")
    for i in range(caseAmount):
        pickCase = int(input("Please pick a case\n>"))
        while pickCase in pickedCases:
            print("You have already picked that case.")
            pickCase = int(input("Please pick a case\n>"))
        while pickCase < 1 or pickCase > 26:
            print("That is not a case number")
            pickCase = int(input("Please pick a case\n>"))
        pickedCases.append(pickCase)
        print("There was " + str(cases2[pickCase - 1]) + " in that case")
        cases[pickCase - 1] = 0

