#an Overhaul of my original program
import random
option = str(input("Choose your mode\n (A) Player V COMP\n (B) Player V Player\n\n"))
user = str(input("Player 1 What is your name?\n"))
plays = 0
score = 0
score2 = 0

if option.upper() == "A":
    usernv = str(input(f"\033[1;32;48m\n{user} Pick one!\n \033[1;36;48m(R) Rock\n (P) Paper\n (S) Scissors\n"))
    usernv = usernv.upper()
    bot = random.randint(1, 3)
    if bot == 1:
        print("Computer chose Rock")
    elif bot == 2:
        print("Computer chose Paper")
    else:
        print("Computer chose Scissors")
    print(f"{user} chose {usernv}")
    if usernv == "R":
        if bot == 2:
            print("Computer wins!")
        elif bot == 3:
            print(f"{user} wins!")
    elif usernv == "P":
        if bot == 1:
            print(f"{user} wins!")
        elif bot == 3:
            print("Computer wins!")
    elif usernv == "S":
        if bot == 1:
            print("Computer wins!")
        elif bot == 2:
            print(f"{user} wins!")

if option.upper() == "B":

    user2 = str(input("Player 2 what is your name?\n"))
    while plays >= 5:
        usernv = str(input(f"\033[1;32;48m\n{user} Pick one!\n \033[1;36;48m(R) Rock\n (P) Paper\n (S) Scissors\n"))
        usernv = usernv.upper()
        while usernv != "R" and usernv != "P" and usernv != "S":
            print("\033[1;37;48m Invalid Character")
            usernv = str(input(f"\033[1;32;48m\n{user} Pick one!\n \033[1;36;48m(R) Rock\n (P) Paper\n (S) Scissors\n"))
            usernv = usernv.upper()
        user2nv = str(input(f"\033[1;32;48m{user2} Pick one!\n \033[1;36;48m (R) Rock\n (P) Paper\n (S) Scissors\n"))
        user2nv = user2nv.upper()
        while user2nv != "R" and user2nv != "P" and user2nv != "S":
            print("Invalid Character")
            user2nv = str(input(f"\033[1;32;48m{user2} Pick one!\n \033[1;36;48m(R) Rock\n (P) Paper\n (S) Scissors\n"))
            user2nv = user2nv.upper()

        print(f"\033[1;31;48m {user} chose {usernv}\n {user2} chose {user2nv}\033[1;37;48m")
        if usernv == "R":
            if user2nv == "P":
                print(f"{user2} wins!")
                score2 = score2 + 1
                plays = plays + 1
            elif user2nv == "S":
                print(f"{user} wins!")
                score = score + 1
                plays = plays + 1
        elif usernv == "P":
            if user2nv == "R":
                print(f"{user} wins!")
                score = score + 1
                plays = plays + 1
            elif user2nv == "S":
                print(f"{user2} wins!")
                score2 = score2 + 1
                plays = plays + 1
        elif usernv == "S":
            if user2nv == "R":
                print(f"{user2} wins!")
                score2 = score2 + 1
                plays = plays + 1
            elif user2nv == "P":
                print(f"{user} wins!")
                score = score + 1
                plays = plays + 1
    plays = 0
    option = str(input("Do you want to play again? (Y) (N)\n"))
    option = option.upper()
    if option == "Y":
        score = 0
        score2 = 0
    elif option == "N":
        print("The game is now over")
    print(f"{user} got {score}")
    print(f"{user2} got {score2}")
else:
print("Invalid Option")