"""
import time
print("My favourite class is")
time.sleep(2)
print("Computer Programming 1")

animal_List = ["dog","cat","bird","alligator","bear"]
print(animal_List[1])
animal_List[4] = "whale"

user = input("Name an animal:\n")
animal_List.append(user)
print(animal_List)


approved_Inputs = ["Y","N","NO","YES"]
user = input("Do you want to go again? (Y) (N)\n")
while user.upper() not in approved_Inputs:
  print("Invalid Option")
  user = input("Do you want to go again? (Y) (N)\n")
"""

#practice with custom functions
def player1Turn():
    print("Player 1 Turn")
    input("Press Enter to continue\n")

def player2Turn():
    print("Player 2 Turn")
    input("Press Enter to continue\n")

a = 0

def raspberryPi():
    global a
    a = 3
    print(a)

print(a)
raspberryPi()
print(a)

def add(a,b):
    return a+b
def multi(a,b):
    return a*b

print(add(6,8))

"""

while True:
  player1Turn()
  player2Turn()"""