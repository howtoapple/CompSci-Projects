from turtle import *
import random

"""
for i in range(360):
    forward(1)
    left(1)

"""


def move():
    num = random.randint(1, 100)
    print(num)
    if (num % 2) == 0:
        print("Is Even")
    else:
        print("Is odd")


move()
