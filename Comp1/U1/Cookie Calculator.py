#input
print("This program is to help you calculate how to share cookies equally")
print("How many cookies are available?")
a = int(input())
print("How many people are you sharing with?")
b = int(input())

#Calculation
c = a / b
x = a % b

#Output
print(f"Each person will have {c} cookies")
print(f"There will be {x} cookies left over")