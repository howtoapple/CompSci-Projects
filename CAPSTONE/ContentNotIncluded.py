#Content Not Included! The whole point of this project
from arch import clear, user,time; import random

wait = time.sleep(5);rand = random.randint(0,20)
begin=1;note_o=False;s_code=3284;dlc=0
    
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
    clear
    if begin == 1:
        start="You wake up in your house, you feel a bit drowsy. but you decide to have a look around..."
    else:
        start=""
    moveset = ["grab note","open note","hallway","hall"]
    print(f"{start}\nThere is a note on your desk and a door that goes out to a hallway");begin==0
    usr_input= input("What would you like to do?\n")

    if usr_input.lower() == "hallway" or usr_input.lower() =="hall":
        home_hallway()
    elif usr_input.lower()=="grab note" or usr_input.lower()=="open note":
        clear;print(f"You pick up the note, it reads...\nHello {user}, Thank you for your $69 purchase of [CONTENT NOT INCLUDED]\nWe at GenicStudios™ are grateful of your patronage. In return, we offer more content in the form of DLC's (Sold Seperately) for only! $23 per DLC!\nNo need to thank us. We humbly do request that you buy these immedietly")
        sub_input=input("Would you like to purchase the DLC? [Y/n]\n")
        submove = ["y","n","yes","no"];sub_input=sub_input.lower()

        if sub_input=="y" or sub_input=="yes":
            print("Uh oh! Looks like you have insufficient funds!")
            bedroom()
        elif sub_input=="n" or sub_input=="no":
            print("Oh well, Next time...")
            bedroom()
        else:
            print("Invalid Input")
            bedroom()
    else:
        print("Invalid Input")
        bedroom()

def home_hallway():
    global dlc
    clear;print("The hallway is warmly lit by sun entering the room, with a nice painting on the wall\n There is your bedroom, kitchen, and the front door")
    usr_input=input("What would you like to do?\n");moveset=["painting","bedroom","move painting","kitchen"];usr_input=usr_input.lower()
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
            print("You feel you may be eating a bit too many snacks.");snack=snack+1
            kitchen()
        elif usr_input=="eat" or usr_input=="snack" and snack>=5:
            print("More!? wow, very well deserved...");snack=snack+1
            kitchen()
        elif usr_input=="eat" or usr_input=="snack" and snack>=10:
            print("You have ran out of snacks...");snack=snack+1
            kitchen()

#I don't think i'll make this do anything
def washroom():
    print("The Washroom is locked. Try again later.")

def suburbia():
    crt_info="debit card"
    clear;print("You step out into the blinding light. What surrounds you are nice homes and townhomes, you see your neighbour Will watering their plants.\nYou also notice your 'mailbox' is overflowing\nYou can travel in 4 directions, North, East, South, and West")
    usr_input =input("What would you like to do?\n");usr_input=usr_input.lower()
    if usr_input =="open mailbox" or usr_input=="mailbox":
        print(f"You open your mailbox, nothing but junk mail and useless ads\nAlthough one note has 'IMPORTANT' as the title\nIt reads 'Dear {user}, due to some questionable... practices, we at GenicStudios™ WILL disable your game if you do not purchase one of our various DLC's")
        sub_input=input("Please, would you like to buy our DLC's? [Y/n]?");sub_input=sub_input.lower()
        if sub_input=="y" and "yes":
            less_input=input("Please enter your payment info.")
            if rand <= 3:
                print("Accepted!\nPlease check later for your content to load!")
            else:
                print("PAYMENT DECLINED, please try again later.")
    


def will():
    pass
def will_house():
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