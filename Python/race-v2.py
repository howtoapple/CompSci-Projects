# Space Race game redone!
import time, random
from os import system

# Global Variables
fuel = 50
oxygen = 15
heat = 10
water = 5
energy = 15
distance = 0
play_again = True
lose_condition = False
win_condition = False
Enemy = -15

accepted_usr_input = []


def starter():
    print("It's the year 1969, and at the height of the space race the Soviets are winning\n"
          "That's why The U.S. hired you Biel Armstrong to get to the moon before the soviets do.  ")

"""
while not lose_condition:
    starter()
"""

usr_input = input("What color is math?\n>")

print(1 + 3 == 3)
