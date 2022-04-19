# Code for the Game within the game
# Labyrinth Game from Hawaii Part II
from getkey import getkey, keys
Select = [">New           █\n█           Exit", "New\n >Exit"]

from playsound import playsound
playsound('CAPSTONE/HawaiiPartii.mp3')

def select():
    key = getkey()
    if key == keys.UP:
        print(Select[-1])
    elif key == keys.DOWN:
        print(Select[1])
    print(f"""
████████████████████████████
█                          █
█                          █
█                          █
█                          █
█         Labyrinth        █
█   ミラクルミュージカル   █
█                          █ 
█                          █
█           {Select[0]}           █
█                          █
█                          █
█                          █
████████████████████████████
use W, A, S, D,; press enter to select
    """)

def WASD():
    global new
    key = getkey()
    if key == 'w' or 'W':
        new = ">"
        

    elif key == keys.DOWN:
        ...  # Handle the DOWN key
    elif key == 'a':
        ...  # Handle the `a` key
    elif key == 'Y':
        ...  # Handle `shift-y`
    else:
        pass
    # Handle other text characters

select()
WASD()
