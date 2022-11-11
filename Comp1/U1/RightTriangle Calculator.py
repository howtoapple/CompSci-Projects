#input
print("This program will calculate the area and perimeter of a right triangle")
print("What is the base length of the Triangle?")
base = int(input())
print("What is the height of the triangle")
height = int(input())

#Calculations
area = 1/2 * base * height
import math
c = math.sqrt(base**2+height**2)
perimeter = height + base + c

#Output
print(f"Base: {base}")
print(f"Height: {height}")
print(f"Area: {area}")
print(f"Perimeter: {perimeter}")