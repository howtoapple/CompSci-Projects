"""
#Practice with if statements
x = int(input())
y = int(input())

if x < y:
  print("x is less than y")
elif y < x:
  print("x is greater than y")
else:
  print("the numbers are equal")

#Practice with User input
user_Input = int(input("What's the temp outside?\n"))
if user_Input <= 59:
  print("That is too cold")
elif user_Input == 60:
  print("That is a perfect temp")
else:
  print("That is too hot")
  """

#input manipulation practice
user_Input = input("Type in a name\n");
print(user_Input);
print(user_Input.lower());

print()
user_Input = input("Do you want to continue? (Yes) (No)")
if user_Input.lower() == "yes":
    print("Program will continue...")

#And Or Practice
x = int(input("Number:\n"))
y = int(input("Another Number:\n"))

if x > 0 and y > 0:
    print("Valid")
else:
    print("Hello World")

user_Input = int(input("Type in a number between 1 and 8:\n"))
if user_Input >=1 and user_Input <=8:
    print("Good Job")
else:
    print("Not a correct Input")