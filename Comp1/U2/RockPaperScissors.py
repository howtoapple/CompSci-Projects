user = str(input("\033[1;32;48m What is your name?\n"))
user_2 = str(input("\nPlayer 2 what is your name?\n"))
print(f"\n{user} your turn!")
usernv = str(input("\033[1;36;48m (R) Rock\n (P) Paper\n (S) Scissors\n"))
print(f"\033[1;32;48m \n{user_2} now its your turn!")
user_2nv = str(input("\033[1;36;48m (R) Rock\n (P) Paper\n (S) Scissors\n"))
usernv = usernv.upper()
user_2nv = user_2nv.upper()
print(f"\033[1;37;48m \n{user} chose {usernv} and {user_2} chose {user_2nv}")

w1 = f"{user} wins!"
w2 = f"{user_2} wins!"
if usernv == "R":
    if user_2nv == "P":
        print(w2)
    elif user_2nv == "S":
        print(w1)
elif usernv == "P":
    if user_2nv == "R":
        print(w1)
    elif user_2nv == "S":
        print(w2)
elif usernv == "S":
    if user_2nv == "R":
        print(w2)
    elif user_2nv == "P":
        print(w1)
else:
    print("Invalid")