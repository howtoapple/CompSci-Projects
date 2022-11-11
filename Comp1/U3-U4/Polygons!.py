import turtle as tur
game = 1
while game == 1:
    n = int(input("How many sides would you like?\n"))
    while n <= 2:
        print("Invalid!")
        n = int(input("How many sides would you like?\n"))
    a = ((n-2)*180)/n
    print(a)
    count = 0
    while count != n:
        count = count+1
        tur.left(180 - a)
        tur.forward(50)
    yes = 0
    while yes == 0:
        again = str(input("Would you like to play again? \n(Y) Yes\n(N) No\n"))
        if again.upper() == "Y":
            tur.clear()
            yes = 1
            game = 1
        if again.upper() == "N":
            exit()
        if again.upper() != "Y" and again.upper() != "N":
            print("Invalid!")