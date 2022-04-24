#Among us text-based ripoff
import os, time, random
clear = lambda:os.system('clear'); wait = time.sleep(1)
usr=0

print("Hello World!")

#Stores easy to call strings for the repetitve bits
rdict = {
    "admin": "You walk over to the Admin room",
    "cmd": "You walk over to the Command Station",
    "med": "You walk over to Medbay",
    "hall": "You walk into a hallway",
    "armour": "You walk over to the Armoury",
    "cafe": "You walk into the Cafeteria, the place you woke up in.",
    "security": "You Walk over to the Security room",
    "elect": "You walk over to Electrical"
}

#Fix the verify leaks

def cafeteria():
    global usr_input
    if usr==0:
        str="You awake into a large dark room with oddly shaped machinery."
        usr+1
    else:
        str=""
    clear();print(f"{str}you see a window that looks out into what appears to just be space\n There is a hallway that leads into more rooms and two rooms: a command station, and a Medbay ");usr+1
    crt_input=["hallway","hall","medbay","command","command station"]
    usr_input=input("What would you like to do?\n");usr_input=usr_input.lower()
    while usr_input not in crt_input:
        print("invalid input")
        usr_input=input("What would you like to do?\n");user_input=usr_input.lower()
    if usr_input=="command" or usr_input=="command station":
        clear();print(rdict["cmd"]);wait
        command()
    elif usr_input=="medbay":
        clear();print(rdict["med"])
        medbay()
    elif usr_input=="hallway" or usr_input=="hall":
        clear();print(rdict["hall"])
        hallway()


def command():
    global usr_input
    clear();print("This is the command station, where all the controls to the ship are\nYou can go to the Cafeteria or down to Comms")
    crt_input=["cafeteria","comms"]
    usr_input=input("What would you like to do?\n");usr_input=usr_input.lower()
    while usr_input not in crt_input:

    if usr_input=="cafeteria":
        clear();print(rdict["cafe"]);wait
        cafeteria()
    elif usr_input=="comms":
        clear();print(rdict[comms])
        comms()


def medbay():
    global usr_input
    clear();print("This is the MedBay, where you can heal from battle.\nYou can go to Cafeteria, and Hallway")
    crt_input=["cafeteria","hallway","hall"]
    usr_input=input("What would you like to do?\n");usr_input=usr_input.lower()
    while usr_input not in crt_input:
        print("invalid input")
    if usr_input=="cafeteria":
        clear();print(rdict["cafe"]);wait
        cafeteria()
    elif usr_input=="hallway" or usr_input==("hall"):
        clear();print(rdict[hallway])
        hallway()



def hallway():
    global usr_input
    clear();print("This is the hallway, where you are able to easily go from place to place\nYou can go to the Cafeteria, Admin, Security, and the Armoury")
    crt_input=["cafeteria","admin","security","armoury"]
    usr_input=input("What would you like to do?\n");usr_input=usr_input.lower()
    while usr_input not in crt_input:
        print("invalid input")
    if usr_input=="cafeteria":
        clear();print(rdict["cafe"]);wait
        cafeteria()
    elif usr_input=="admin":
        clear();print(rdict["admin"]);wait
        admin()
    elif usr_input=="security":
        clear();print(rdict["security"]);wait
        security()
    elif usr_input=="armoury":
        clear();print(rdict["armour"]);wait
        armoury()


def admin():
    global usr_input
    clear();print("This is admin, where you can get more information on entities\nYou can go back to the Hallway")
    crt_input=["hall","hallway"]
    usr_input=input("What would you like to do?\n");usr_input=usr_input.lower()
    while usr_input not in crt_input:
        print("invalid input")
    if usr_input=="hall" or usr_input =="hallway":
        clear();print(rdict["hall"]);wait
        hallway()


def armoury():
    global usr_input
    clear();print("This is the armoury, where you can prepare for battle with the Imposter\nYou can go to the Hallway, Electrical or Comms")
    crt_input=["hall","hallway","electrical","electric"]
    usr_input=input("What would you like to do?\n");usr_input=usr_input.lower()
    while usr_input not in crt_input:
        print("invalid input")
    if usr_input=="hall" or usr_input=="hallway":
        clear();print(rdict["hall"]);wait
        hallway()
    elif usr_input=="electrical" or usr_input=="electric":
        clear();print(rdict["elect"])


def comms():
    global usr_input
    clear();print("This is comms, where you can make communications\nYou can go to the Armoury and Command Station ")
    crt_input=["armoury","command","command station"]
    usr_input=input("What would you like to do?\n");usr_input=usr_input.lower()
    while usr_input not in crt_input:
        print("invalid input")
    if usr_input=="armoury":
        clear();print(rdict["armour"]);wait
        armoury()
    elif usr_input=="command" or usr_input=="command station":
        clear();print(rdict["cmd"])
        command()


def security():
    global usr_input
    clear();print("This is security, where you can look at cameras to find where the Imposter is\nYou can go back to the Hallway ")
    crt_input=["hall","hallway"]
    usr_input=input("What would you like to do?\n");usr_input=usr_input.lower()
    while usr_input not in crt_input:
        print("invalid input")
    if usr_input=="hall" or usr_input=="hallway":
        clear();print(rdict["hall"]);wait
        hallway()
        


def electrical():
    global usr_input
    clear();print("This is electrical, where all of the electrical components of the ship are. This is the main hiding place for the Imposter. \nYou can go to the armoury")
    crt_input=["armoury"]
    usr_input=input("What would you like to do?\n");usr_input=usr_input.lower()
    while usr_input not in crt_input:
        print("invalid input")
    if usr_input=="":
        clear();print(rdict["armour"]);wait
        armoury()

cafeteria()