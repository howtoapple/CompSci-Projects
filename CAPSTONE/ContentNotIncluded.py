#Content Not Included! The whole point of this project
from arch import clear, user,time; import random

wait = time.sleep(5);rand = random.randint(0,20)
begin=True;note_o=False;willmet=False
s_code=3284;dlc=0
    
def startup():
    print(f"Welcome to:")
    print("""░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░   ░░░░░░░░░░░░░░░░░░░░░░░░░░░   ░░░░░░░░░░░░░░░░░░░░░░░░░░   ░░░░░░░░░    ░░░░░   ░░░░░░░░░░░░░░   ░░░░░░░░░   ░░░░░░░░░░░░░░░░░░░   ░░░░░░░░░░░░░░░   ░░░░░░░░░░░░░░░░░░   ░
▒▒   ▒▒▒   ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒   ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒   ▒▒▒▒▒▒▒▒▒  ▒   ▒▒▒   ▒▒▒▒▒▒▒▒▒▒▒▒▒▒   ▒▒▒▒▒▒▒▒▒   ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒   ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒   ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒   ▒
▒   ▒▒▒▒▒▒▒▒▒▒▒   ▒▒▒▒▒   ▒   ▒▒▒    ▒  ▒▒▒▒   ▒▒▒▒▒   ▒   ▒▒▒    ▒  ▒▒▒▒▒▒▒   ▒   ▒▒   ▒▒▒▒   ▒▒▒▒▒    ▒  ▒▒▒▒▒▒▒   ▒   ▒   ▒▒▒▒▒▒    ▒   ▒   ▒▒   ▒▒▒▒▒▒   ▒▒▒▒▒   ▒▒▒▒▒▒▒▒▒▒   ▒
▓   ▓▓▓▓▓▓▓▓▓   ▓▓   ▓▓▓   ▓▓   ▓▓▓   ▓▓▓▓  ▓▓▓   ▓▓▓   ▓▓   ▓▓▓   ▓▓▓▓▓▓▓▓▓   ▓▓   ▓   ▓▓   ▓▓   ▓▓▓▓   ▓▓▓▓▓▓▓▓▓   ▓▓   ▓▓   ▓▓   ▓▓▓▓   ▓   ▓▓   ▓▓       ▓▓▓  ▓▓▓   ▓▓▓       ▓
▓   ▓▓▓▓▓▓▓▓   ▓▓▓▓   ▓▓   ▓▓   ▓▓▓   ▓▓▓         ▓▓▓   ▓▓   ▓▓▓   ▓▓▓▓▓▓▓▓▓   ▓▓▓  ▓   ▓   ▓▓▓▓   ▓▓▓   ▓▓▓▓▓▓▓▓▓   ▓▓   ▓▓   ▓   ▓▓▓▓▓   ▓   ▓▓   ▓  ▓▓▓   ▓▓         ▓▓  ▓▓▓   ▓
▓▓   ▓▓▓   ▓▓   ▓▓   ▓▓▓   ▓▓   ▓▓▓   ▓ ▓  ▓▓▓▓▓▓▓▓▓▓   ▓▓   ▓▓▓   ▓ ▓▓▓▓▓▓▓   ▓▓▓▓  ▓  ▓▓   ▓▓   ▓▓▓▓   ▓ ▓▓▓▓▓▓▓   ▓▓   ▓▓   ▓▓   ▓▓▓▓   ▓   ▓▓   ▓  ▓▓▓   ▓▓  ▓▓▓▓▓▓▓▓▓  ▓▓▓   ▓
████     ██████   █████    ██   ████   ████     ████    ██   ████   ████████   ██████   ████   ████████   ████████   █    ██   ████    █   ███      ██       ████     █████       █
███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████                                             
A programming Project
    """);wait
    bedroom()

#The code for the players bedroom... a bit long
def bedroom():
    global begin
    clear
    if begin == True:
        start="You wake up in your house, you feel a bit drowsy. but you decide to have a look around..."
        begin=False
    else:
        start=""

    moveset = ["grab note","open note","hallway","hall"]
    print(f"{start}\nThere is a note on your desk and a door that goes out to a hallway")
    usr_input=input("What would you like to do?\n");usr_input=usr_input.lower()

    while usr_input not in moveset:
        print("Unrecognized Option")
        usr_input=input("What would you like to do?\n")
    if usr_input== "hallway" or usr_input=="hall":
        home_hallway()
    elif usr_input=="grab note" or usr_input=="open note" or usr_input:
        
        clear;print(f"You pick up the note, it reads...\nHello {user}, Thank you for your $69 purchase of [CONTENT NOT INCLUDED]\nWe at \033[1;36;48mGenicStudios™\033[1;0;48m are grateful of your patronage. In return, we offer more content in the form of DLC's (Sold Seperately) for only! $23 per DLC!\nNo need to thank us. We humbly do request that you buy these immedietly")
        sub_input=input("Would you like to purchase the DLC? [Y/n]\n")
        submove = ["y","n","yes","no"];sub_input=sub_input.lower()

        while sub_input not in submove:
            print("unrecognized option")
            sub_input=input("Would you like to purchase the DLC? [Y/n]\n")
        if sub_input=="y" or sub_input=="yes":
            print("Uh oh! Looks like you have insufficient funds!")
            bedroom()
        elif sub_input=="n" or sub_input=="no":
            print("Oh well, Next time...")
            bedroom()

def home_hallway():
    global dlc
    clear;print("The hallway is warmly lit by sun entering the room, with a nice painting on the wall\n There is your bedroom, kitchen, and the front door")
    usr_input=input("What would you like to do?\n");moveset=["painting","bedroom","move painting","kitchen","front door"];usr_input=usr_input.lower()
    while usr_input not in moveset:
        print("Unrecognized Option")
        usr_input=input("What would you like to do?\n")
    if usr_input=="painting":
        print("""You look at the painting\nThe person in the painting looks oddly similar to yourself\nit seems quite loose from the wall, maybe you can move it?""")
    elif usr_input=="move painting":
        print("You move the painting and find a safe with a four digit passcode")
        sub_input =input("What is the code? [] [] [] []")
        if sub_input==s_code:
            print("You found a Divine Luminince Crystal! (DLC)")
            dlc + 1
        elif sub_input!=s_code:
            print("The code is incorrect")
            home_hallway()
    elif usr_input=="bedroom":
        bedroom()
    elif usr_input=="kitchen":
        kitchen()
    elif usr_input=="front door":
        suburbia()

def kitchen():
    clear;print("Sunlight bleeds into the room revealing your unfortunately messy kitchen... you feel the urge to go for a snack.\nThere is a hallway, locked washroom door, and the front door.")
    usr_input=input("What would you like to do?\n");usr_input=usr_input.lower()

    if usr_input=="snack" or usr_input=="eat":
        Snack()
    elif usr_input=="hallway":
        home_hallway()
    elif usr_input=="washroom":
        washroom()
    elif usr_input=="front door":
        suburbia()
#Do not fear! The snacks are here!
    def Snack():
        if usr_input=="eat" or usr_input=="snack" and snack >=0:
            print("You reach into your pantry and find a snack! You eat it.");snack=snack+1
            kitchen()
        elif usr_input=="eat" or usr_input=="snack" and snack>=2:
            print("Snacks!");snack=snack+1
            kitchen()
        elif usr_input=="eat" or usr_input=="snack" and snack>=5:
            print("Wow, very well deserved...");snack=snack+1
            kitchen()
        elif usr_input=="eat" or usr_input=="snack" and snack>=10:
            print("You have ran out of snacks...");snack=snack+1
            kitchen()

#I don't think I'll make this do anything
def washroom():
    print("The Washroom is locked. Try again later.")

#Suburbia | this one is big!
def suburbia():

    if sub==False:
        srt="You step out into the blinding light. What surrounds you are big suburb homes and townhomes, you see your neighbour Will watering their plants.\nYou also notice your 'mailbox' is overflowing\nYou can travel in 4 directions, North, East, South, and West"
        sub = True
    elif sub==True:
        srt="You are standing next to your house where you are surrounded by homes, your neighbour will is sitting on their porch.\nYou can go inside your 'Home' or travel, North, East, West, or South."

    clear;print(srt)
    usr_input =input("What would you like to do?\n");usr_input=usr_input.lower()

    #Chkmoves
    moveset=["mailbox","open mailbox","north","go north","east","go east","south","go south","west","go west","house","home"]
    submoves=["y","yes","n","no"]

#
    while usr_input not in moveset:
        print("Unrecognized Option")
        usr_input=input("What would you like to do?\n");usr_input=usr_input.lower()

    if usr_input =="open mailbox" or usr_input=="mailbox":
        print(f"You open your mailbox, nothing but junk mail and useless ads\nAlthough one note has 'IMPORTANT' as the title\nIt reads 'Dear {user}, due to some questionable... practices, we at \033[1;36;48mGenicStudios™\033[1;0;48m WILL disable your game if you do not purchase one of our various DLC's")
        sub_input=input("Please, would you like to buy our DLC's? [Y/n]?");sub_input=sub_input.lower()
        if sub_input=="y" and "yes":
            less_input=input("Please enter your payment info.")
            if rand <= 3:
                print("Accepted!\nPlease check later for your content to load!")
                suburbia()
            else:
                print("PAYMENT DECLINED, please try again later.")
                suburbia()
    elif usr_input=="go north" or usr_input=="north":
        if willmet==False:
            print("You start walking North, unfortunately your neighbour Will stops you");willmet==True
            will()
        elif willmet==True:
            print("You walk north and stop next to wills house")
            sub_input=input("Would you like to continue north? [Y/n]?\n");sub_input=sub_input.lower()

            while sub_input not in submoves:
                print("Unrecognized Option")
                sub_input=input("Would you like to continue North? [Y/n]?\n");sub_input=sub_input.lower()
            if sub_input=="y" or sub_input=="yes":
                print("You decide to stop by Will's house, because why not?")
                will_house()
            elif sub_input=="n" or sub_input=="no":
                print(f"You continue walking up north, you pass rows of homes and you see kids playing up and down the suburban streets.\n you can't help but notice that some parts of the neighbourhood are missing textures, symbolized by the black and purple checkered patterns on certain objects\nYou now finally reach the forest")
                forest()
    elif usr_input=="go east" or usr_input=="east":
        print("You start heading east, as you walk down you notice that a whole road is missing! did the devs really forget to add a road here? anyways, you see a bakesale down the block")
        sub_input=input("Would you like to go to the bakesale? [Y/n]?");sub_input=sub_input.lower()

        while sub_input not in submoves:
            print("Unrecognized Option")
            sub_input=input("would you like to go to the bakesale? [Y/n]?");sub_input=sub_input.lower()
        if sub_input=="y" or sub_input=="yes":
            print("You change route and head to the bakesale")
            bakesale()
        elif sub_input=="n" or sub_input=="no":
            print("You continue north and near the downtown area of your city. You look up; only to see skyscrapers bound up, creating a formidable skyline")
            downtown()
    elif usr_input=="go west" or usr_input=="west":
        print("You head west, this area of the neighbourhood has an unsually high amount of flowers, you reach your destination")
        west()
    elif usr_input=="go south" or usr_input=="south":
        print("You head south, the roads start getting steeper up hill, you then see the mountains in the distance... How did you not see this before?")
        pleateu()
    elif usr_input=="home" or usr_input=="house":
        print("You walk up to your front door; open it and head inside")
        home_hallway()


def will():
    pass
def will_house():
    pass
def bakesale():
    pass
def forest():
    pass
def downtown():
    clear;print("You walk through Downtown and it's packed, masses of people pass you, you aren't quite sure where to go from here. Although a building with big flashy lettering spelling out C A S I N O catches your eye\nYou can travel North, East, West or go to the Casino, Arcade, and/or the Recreation of the \033[1;36;48m'GenicStudios'™\033[1;0;48m Office building...")
    moveset=["go north","north","go east","east","go west","west","casino","arcade","genic studios","genic","genicstudios"]
    usr_input=input("What would you like to do?");usr_input=usr_input.lower()


    while usr_input not in moveset:
        print("Unrecongnized Option")
        usr_input=input("What would you like to do?\n");usr_input=usr_input.lower()
    if usr_input=="genic studios" or usr_input=="genic" or usr_input=="genicstudios":
        print("You walk towards the \033[1;36;48mGenicStudios™\033[1;0;48m Office, it looks way nicer in the game than in real life.")


def casino():
    pass
def arcade():
    pass
def genic():
    pass

def west():
    clear;print("As you apporach you unexpectedly hit a wall. Ouch*")
    print("""   ___     _       ___              ___     ___    ___     _   _    ___     ___     ___     ___   
  |   \   | |     / __|            | _ \   | __|  / _ \   | | | |  |_ _|   | _ \   | __|   |   \  
  | |) |  | |__  | (__             |   /   | _|  | (_) |  | |_| |   | |    |   /   | _|    | |) | 
  |___/   |____|  \___|            |_|_\   |___|  \__\_\   \___/   |___|   |_|_\   |___|   |___/  
  Please buy the required DLC (More Area DLC) from the official \033[1;36;48mGenicStudios™\033[1;0;48m store in order to pass
  """)
    print("It seems that a lovely pop-up has appeared\nYou can go back East or try heading 'West' again")
    usr_input=input("What would you like to do?");usr_input=usr_input.lower()
    moveset=["east","west"]

    while usr_input not in moveset:
        print("Unrecognized Option")
        usr_input=input("What would you like to do?");usr_input=usr_input.lower()
    if usr_input=="west":
        west()
    elif usr_input=="east":
        print("You head east, back to the Suburbs.")
        suburbia()
    

def pleateu():
    pass
def mountain():
    pass


startup()

"""
Side notes for later!:

GenicStudios™ will be the antogonist of the story


Labyrinth, Tom, Blockage Videogames
Jenkins Marvin~
Charlie Roberts?
Garlic Jim's Pizza place?
Destroying a sweater...

Linus Tech Tips
Gambling.. Of course
fighting (will? the neighbour)
Tuesday, finest day in existance?
pay2win
"""