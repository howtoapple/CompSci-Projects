import time, random; from os import system

fuel = 50;oxygen = 15;heat = 10;water = 5;energy = 15;distance = 0;play_again = True;lose_Cond = False;win_cond = 235; enemy = -10; eMove = True; 
approved_inputs = ["S", "Q", "H", "O", "Y", "N", "T", "F"]

def enemy_Move():
    global enemy
    eMove=random.randint(10,20);enemy=eMove + enemy
def thrust():
    global distance, heat, fuel
    pDist = random.randint(7,13);distance = pDist + distance
    heat-1;fuel-2 
def thrust_fast():
    global distance, heat, fuel
    fDist = random.randint(13, 25);distance = fDist + distance
    fuel = fuel - random.randint(3,4)

def status():
    global stats
    stats = print(f"\033[1;32;48mYour stats,\n\033[1;30;48m Fuel: {fuel}\n Oxygen: {oxygen}\n Heat: {heat}\n Food {water}\n Power: {energy}\n Current Position: {distance}\n Enemy Position: {enemy}\n")
def inputs():
    inp = input(print("Make your move,\n [O] Oxygen- Maintain your O2 supply\n [H] Heater - Warm up your shuttle\n [T] Thrust - Move across space at a moderate pace\n [F] Fast Thrust - Move at a fast pace \n[Q] Quit - Forfeit the Space Race\n"))
    inp.upper()
    print("Processing...")
    if approved_inputs:
        if inp == "O":
            energy-1;oxygen+2
        elif inp == "H":
            energy-2;heat+2
        elif inp == "T":
            thrust()
        elif inp =="F":
            thrust_fast()
        elif inp =="Q":
            print("You can't quit! Lmao")
        status()
    
def lose_cond():
    global lose_Cond
    if fuel <= 0:
        lose_Cond=True;print("You have ran out of Fuel");exit()
    elif oxygen <= 0:
        lose_Cond=True;print("You have ran out of Oxygen");exit()
    elif heat <= 0:
        lose_Cond=True;print("You have froze to death");exit()
    elif energy <= 0:
        lose_Cond;print("You have ran out of energy");exit()
    elif enemy >= distance:
        lose_Cond
print("It is 1969 and You are astronaut Biel Legstrong, your goal is to beat your rival, the Soviet Union before they get to the moon and win the space race!\n Use your resources wisely, otherwise you could get stuck or die from inadequet use of resources\n Good luck.")
while play_again == True:
    lose_cond()
    if lose_Cond == False:
        inputs()