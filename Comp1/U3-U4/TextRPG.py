#Among us text-based ripoff
import os, time, random
clear = lambda:os.system('clear');
keycard=False
usr=0; tasks=0
dagger=False; armor=True
pHealth=100;iHealth=250;energy=15

from replit import audio

audio.play_file('amogus.mp3')

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
    "elect": "You walk over to Electrical",
    "comms": "You walk over to the Communicaions room"
}
out = {
    "in": "What would you like to do?\n",
    "un": "Unrecognized Option"
}

#Fix the verify leaks

def cafeteria():
    global keycard
    if usr==0:
        str="You awake into a large dark room with oddly shaped machinery."
        usr+1
    else:
        str=""
    clear();print(f"{str}you see a window that looks out into what appears to just be space\n There is a 'keycard' on a table, and you can go to: hallway, a command station, and a Medbay");usr+1
    crt_input=["hallway","hall","medbay","command","command station","keycard"]
    usr_input=input(out["in"])
    usr_input=usr_input.lower()

    while usr_input not in crt_input:
        print(out["un"])
        usr_input=input(out["in"])
        usr_input=usr_input.lower()

    if usr_input=="command" or usr_input=="command station":
        clear();print(rdict["cmd"])
        time.sleep(2)
        command()
    elif usr_input=="medbay":
        clear();print(rdict["med"])
        time.sleep(2)
        medbay()
    elif usr_input=="hallway" or usr_input=="hall":
        clear();print(rdict["hall"])
        time.sleep(2)
        hallway()
    elif usr_input== "keycard":
        print("You grab the keycard!\n")
        time.sleep(2)
        keycard=True
        cafeteria()


def command():
    global usr_input
    clear();print("This is the command station, where all the controls to the ship are\nYou can go to the Cafeteria or down to Comms")
    crt_input=["cafeteria","comms"]
    usr_input=input(out["in"])
    usr_input=usr_input.lower()

    while usr_input not in crt_input:
        print(out["un"])
        usr_input=input(out["in"])
        usr_input=usr_input.lower()

    if usr_input=="cafeteria":
        clear();print(rdict["cafe"])
        time.sleep(2)
        cafeteria()
    elif usr_input=="comms":
        clear();print(rdict["comms"])
        time.sleep(2)
        comms()


def medbay():
    global usr_input
    clear();print("This is the MedBay, where you can heal from battle.\nYou can go to Cafeteria, and Hallway")
    crt_input=["cafeteria","hallway","hall"]
    usr_input=input(out["in"])
    usr_input=usr_input.lower()

    while usr_input not in crt_input:
        print(out["un"])
        usr_input=input(out["in"])
        usr_input=usr_input.lower()
    if usr_input=="cafeteria":
        clear();print(rdict["cafe"])
        time.sleep(2)
        cafeteria()
    elif usr_input=="hallway" or usr_input==("hall"):
        clear();print(rdict["hall"])
        time.sleep(2)
        hallway()



def hallway():
    global usr_input
    clear();print("This is the hallway, where you are able to easily go from place to place\nYou can go to the Cafeteria, Admin, Security, and the Armoury")
    crt_input=["cafeteria","admin","security","armoury"]
    usr_input=input(out["in"]);usr_input=usr_input.lower()

    while usr_input not in crt_input:
        print(out["un"])
        usr_input=input(out["in"]);usr_input=usr_input.lower()
    if usr_input=="cafeteria":
        clear();print(rdict["cafe"])
        time.sleep(2)
        cafeteria()
    elif usr_input=="admin":
        clear();print(rdict["admin"])
        time.sleep(2)
        admin()
    elif usr_input=="security":
        clear();print(rdict["security"])
        time.sleep(2)
        security()
    elif usr_input=="armoury":
        clear();print(rdict["armour"])
        time.sleep(2)
        armoury()


def admin():
    global keycard
    clear();print("This is admin, where you can get more information on entities\nYou can use the admin 'console' or go back to the Hallway")
    crt_input=["hall","hallway","console","admin console"]; submoves=["k","keycard","e","exit","i","info","s","stats"]
    usr_input=input(out["in"]);usr_input=usr_input.lower()

    def console():
        global usr_input
        usr_input(out["in"]+"[I] Info\n [S] Stats\n [E] Exit")

        while usr_input not in submoves:
            print(out["un"])
            usr_input=input(out["in"])
        if usr_input=="e" or usr_input=="exit":
            print("Leaving Console...")
            time.sleep(2)
            admin()
        elif usr_input=="s" or usr_input=="stats":
            print(f" Tasks: {tasks}\n Distance to Earth: {dist}\n ")

    while usr_input not in crt_input:
        print(out["un"])
        usr_input=input(out["in"])

    if usr_input=="hall" or usr_input =="hallway":
        clear();print(rdict["hall"])
        time.sleep(2)
        hallway()
    elif usr_input=="console" or usr_input=="admin console":
        print("You start using the console, it has some basic controls\nPlease Insert 'Keycard'")
        sub_input=input(out["in"] +"\n [K] Keycard\n [E] Exit Console ");sub_input=sub_input.lower()

        while sub_input not in submoves:
            print(out["un"])
            sub_input=(out["in"] +"\n [K] Keycard\n [E] Exit Console");sub_input=sub_input.lower()
        if sub_input=="e" or sub_input=="exit":
            print("Leaving console...")
            time.sleep(2)
            admin()
        elif sub_input=="k" or sub_input =="keycard":
            if keycard==True:
                print("You insert the keycard into the console.\n\"Access Granted\" The console screen shows.")
                console()
            elif keycard==False:
                print("\"Acess Denied\"")
                admin()

def armoury():
    global usr_input, dagger, armor
    clear();print("This is the armoury, where you can prepare for battle with the Imposter\nYou access the 'weapon' 'Cabinet' or go to the Hallway, Electrical or Comms")
    crt_input=["hall","hallway","electrical","electric","comms","weapon","cabinet","weapon cabinet"]
    umoves=["L","D","A"]
    usr_input=input(out["in"]);usr_input=usr_input.lower()

    while usr_input not in crt_input:
        print(out["un"])
        usr_input=input(out["in"])
    if usr_input=="hall" or usr_input=="hallway":
        clear();print(rdict["hall"])
        time.sleep(2)
        hallway()
    elif usr_input=="electrical" or usr_input=="electric":
        clear();print(rdict["elect"])
        electrical()
    elif usr_input=="comms":
        clear();print(rdict["comms"])
    elif usr_input=="weapon" or usr_input=="cabinet" or usr_input=="weapon cabinet":
        print("You open the weapon cabinet, you find various tools and weapons")
        u_input=input("What do you want to do?\n [L] Leave\n [D] Equip Dagger\n [A] Armor")
        u_input=u_input.upper()
        while u_input not in umoves:
            print(out["un"])
            u_input=input("What do you want to do?\n ")
            u_input=u_input.upper()
        if u_input =="D":
            print("You pick up the Dagger, this could be helpful when fighting the imposter")
            time.sleep(3)
            dagger=True
            armoury()
        elif u_input=="L":
            armoury()
        elif u_input=="A":
            print("You pick up the piece of armour, this can help protect you while fighting the imposter")
            armor=True
            time.sleep(3)
            armoury()

def comms():
    global usr_input
    clear();print("This is comms, where you can make communications\nYou can go to the Armoury and Command Station ")
    crt_input=["armoury","command","command station"]
    usr_input=input(out["in"]);usr_input=usr_input.lower()

    while usr_input not in crt_input:
        print(out["un"])
        usr_input=input(out["in"])
    if usr_input=="armoury":
        clear();print(rdict["armour"])
        time.sleep(2)
        armoury()
    elif usr_input=="command" or usr_input=="command station":
        clear();print(rdict["cmd"])
        command()


def security():
    global usr_input
    clear();print("This is security, where you can look at cameras to find where the Imposter is\nYou can go back to the Hallway ")
    crt_input=["hall","hallway"]
    usr_input=input(out["in"]);usr_input=usr_input.lower()

    while usr_input not in crt_input:
        print(out["un"])
        usr_input=input(out["in"])
    if usr_input=="hall" or usr_input=="hallway":
        clear();print(rdict["hall"]);time.sleep(2)
        hallway()



def electrical():
    global usr_input
    clear();print("This is electrical, where all of the electrical components of the ship are. This is the main hiding place for the Imposter. \nYou can go to the armoury")
    crt_input=["armoury", ]
    rand=random.randint(0,3)
    radn=random.randint(0,3)
    if rand is radn:
        print("You face the imposter.")
        usr_input=input("What do you do?\n [F] Fight\n [R] Run")
        usr_input=usr_input.upper()
        while usr_input not in crt_input:
            print(out["un"])
            usr_input=input("what do you do?\n [F] Fight\n [R] Run")
            usr_input=usr_input.upper()
        if usr_input=="F":
            fight()
        elif usr_input=="R":
            rand=random.randint(0,5)
            if rand <=4:
                print("You attempt to flee, unfortunately the imposter gets you")
                death=True
                medbay()


    usr_input=input(out["in"])
    usr_input=usr_input.lower()
    while usr_input not in crt_input:
        print(out["un"])
        usr_input=input(out["in"])
    if usr_input=="armoury":
        clear();print(rdict["armour"]);time.sleep(2)
        armoury()
def fight():
    global health, energy, heals
    clear();print("You try fighting the imposter")
    crt_move=["A","S","H","R"]
    def subf():
        global health, energy,heals
        usr_input=input("IMPOSTER FIGHT\n [A] Regular Attack\n [S] Strong Attack\n [H] Heal\n [R] Run")
        while usr_input not in crt_move:
            print(out["un"])
            usr_input=input("IMPOSTER FIGHT\n [A] Regular Attack\n [S] Strong Attack\n [H] Heal\n [R] Run")

            if usr_input=="A":
                rand=random.randint(5,25)
                if rand<=7:
                    print("You missed")
                    subf()
                elif rand:
                    rand-=iHealth
                    print("You attack")
    subf()

cafeteria()

#Replit is atrocious
