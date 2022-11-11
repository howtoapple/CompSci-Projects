#This is a simple program to determine if a rook can make a valid move

#Program Instructions
print("This program will help you determine if a rook can be moved to a certain location")
print("You will type a location using (x) (y) coordinate system")

#User Starting POS
x1,y1 = input("Please enter your starting position:\n").split()
x1 = int(x1)
y1 = int(y1)

#User move to POS
x2,y2 = input("Please enter where you would like to move:\n").split()
x2 = int(x2)
y2 = int(y2)

#Decision and response
if x1 == x2:
    if y1 == y2:
        print("Invalid Move")
    elif 0 < y2 < 9:
        print("Valid Move")
    else:
        print("Invalid Move")
if 0 < x2 < 9:
    print("Valid Move")
else:
    print("Invalid Move")