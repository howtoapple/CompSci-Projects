x = float(input("What is the bill total amount?\n"))
y = int(input("How many times is the bill going to be split?\n"))
tip = int(input("Tip Percentage?\n"))

p = tip/100
t = round((x*p)+x,2)
a = round(t/y,2)
c = 20
b = round(abs(c-a),2)

print(f"Total Bill Amount: {t}")
print(f"Each person has to pay: {a}")

if b <= 0:
    print(f"You do not have enough money {b} left")
else:
    print(f"You have enough money {b} left") 