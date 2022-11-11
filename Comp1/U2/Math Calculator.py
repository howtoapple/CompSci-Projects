#Main Menu
print("\033[1;32;48m Math Calculator")
print("\033[1;37;48m")
print("Please choose from the following Options\n (A) Area Calculations\n (B) Volume Calculations\n (C) Measurement Calculations\n")
#Ask user for choice
user_Choice = input()

#Area Menu
if user_Choice.upper() == "A":
    print("\n\033[1;32;48m Welcome to the Area Cacluations")
    print("\033[1;36;48m")
    print("Please choose from the following Options\n (S) Square\n (O) Circle\n (T) Triangle\n")
    user_input = input()
    if user_input.upper() == "S":
        x = int(input("\nArea = x * y\nPlease enter your first value\n"))
        y = int(input("Please enter your second value\n"))
        y = x * y
        print(y)
    elif user_input.upper() == "O":
        r = int(input("\nEnter the Radius\n"))
        x = 3.14 * (r ** 2)
        print(x)
    elif user_input.upper() == "T":
        base = int(input("\nArea = (Base * Height) 1/2\nPlease enter the base of the triangle\n"))
        height = int(input("Please enter the height of the triangle\n"))
        a = base * height / 1/2
        print(a)
    else:
        print("Invalid Option")

#Volume Menu
elif user_Choice.upper() == "B":
    print("\n\033[1;32;48m Welcome to the Volume Calcuations")
    print("\033[1;36;48m")
    print("Please choose from the following Options\n (A) Cylinder\n (P) Pyramid\n (C) Cube\n")
    user_input = input()
    if user_input.upper() == "A":
        x = int(input("V = 3.14 * r * h\nEnter the radius\n"))
        y = int(input("Enter the Height\n"))
        y = 3.14 * (x ** 2) * y
        print(y)
    elif user_input.upper() == "P":
        l = int(input("(V = lwh / 3)\nEnter the length\n"))
        w = int(input("Enter the width\n"))
        h = int(input("Enter the height\n"))
        y = (l * w * h) / 3
        print(y)
    elif user_input.upper() == "C":
        l = int(input("(V = l * w * h)\nEnter the length\n"))
        w = int(input("Enter the width\n"))
        h = int(input("Enter the height\n"))
        y = l * w * h
        print(y)
#Measurements Menu
elif user_Choice.upper() == "C":
    print("\n\033[1;32;48m Welcome to Unit Calulator")
    print("\033[1;36;48m")
    print("Please choose from the following Options\n (I) Inches to Centimeters\n (F) Feet to Meters\n (M) Miles to Killometers\n")
    user_input = input()
    if user_input.upper() == "I":
        y = int(input("\n(Enter 0 for Centimeters to Inches)\nPlease enter the amount of inches\n"))
        if y == 0:
            y = int(float(input("Please enter the amount of centimeters\n")))
            y = y / 2.54
            print(y)
        else:
            y = y * 2.54
            print(y)
    elif user_input.upper() == "F":
        y = int(input("\n(Enter 0 for Meters to Feet)\nEnter the amount of feet\n"))
        if y == 0:
            y = int(float(input("Enter the amount of Meters\n")))
            y = y * 3.28084
            print(y)
        else:
            y = y / 3.28084
            print(y)
    elif user_input.upper() == "M":
        y = int(input("\n(Enter 0 for Killometers to Miles)\nEnter the amount of Miles\n"))
        if y == 0:
            y = int(float(input("Enter the amount of Killometers\n")))
            y = y / 1.609
            print(y)
        else:
            y = y * 1.609
            print(y)
    else:
        print("\nInvalid Option")
else:
    print("\nInvalid Option")