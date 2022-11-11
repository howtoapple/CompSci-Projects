c = int(input("What is the age of your cat?\n"));
if c == 1:
    print("Your cat is 11 in human years");
elif c >= 2:
    c = c * 4
    a = c - 8
    b = a + 22
    print(f"Your cat is {b} in human years")
else:
    print('Invalid')