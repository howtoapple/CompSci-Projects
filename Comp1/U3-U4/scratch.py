
import random
"""
lower = int(input("Type the lower number\n"))
upper = int(input("Type the upper number\n"))
x = random.randint(lower, upper)
print(x)

#practice with While loops
x = random.randint(1, 2)
guesses = 2
while guesses > 0:
  user_Input = int(input("What do you think my number is?\n"))
  if user_Input == x:
    print("You got it right")
    break;
  else:
    print("Nope wrong guess")
    guesses = guesses -1

"""

#range check
user_Input = int(input("Please type in a number between 1 and 20:\n"))
#data validation
while user_Input < 1 or user_Input > 20:
    print("Invalid Number")
    user_Input = int(input("Please type in a number between 1 and 20:\n"))



    #input check
    user_Input = str(input("Would you like to play again?\n (Y)\n (N)\n"))

    while user_Input.upper() != "Y" and user_Input.upper() != "N":
        print("Invalid Input")
        user_Input = str(input("Would you like to play again?\n (Y)\n (N)\n"))

        #RPS Ex
        user_Input = input("What do you choose? (R) (P) (S)")
        while user_Input.upper() != "R" and user_Input.upper() != "P" and user_Input.upper() != "S":
            print("Invalid Choice")
