#Random Module
import random
rand = random.randint(1, 20)

user = str(input("Welcome to Guess the Number!\nWhat is your name?\n"))
print(f"\nOkay {user} can you guess my number between 1 and 20\nYou have 4 guesses to do so")

guess = 4
while guess > 0:
    usernv = int(input("\nEnter your guess:\n"))
    if usernv == rand:
        print("\nYou got it right!")
        break;
    else:
        guess = guess -1
        if usernv > rand:
            print("Your number is too high")
        else:
            print("\nYour number is too low")
        print(f"You have {guess} guesses left.")
if guess == 0:
    print(f"\nYou lost! the number was {rand}")