#Content Not Included! The whole point of this project
from arch import clear, user,time; import random

rand = random.randint(0,20)
begin=True;note_o=False;willmet=False;man=False;gen=False;app=False;sub=False;employee=False
horse_dlc=False; expansion_dlc=False; gambling_dlc=False
s_code=3284;dlc=0; value=0; money=0;i=0;snack=0
stats=lambda:print("Here is what you got.\n Health: {hp}\n Money: ${money}\n DLC's: {dlc}")


out = {
    "opt": "\033[1;32;48mWhat would you like to do?\033[1;0;48m\n\033[1;49;48m",
    "un": "Unrecognized Option"
}

def mon():
    global money
    if value <= money:
        def deduct(n):
            global money
            return lambda money : money+n
        money=deduct(money)
        money=(money(-value))
    else:
        print("Balance too low!")

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
    by GenicStudios™
    """);time.sleep(5)
    bedroom()

def move():
    global usr_input, moveset
    usr_input=input(out["opt"])
    print("\033[1;0;48m")
    usr_input=usr_input.lower()

    while usr_input not in moveset:
        print(out["un"])
        usr_input=input(out["opt"])
        print("\033[1;0;48m")
        usr_input=usr_input.lower()

#The code for the players bedroom... a bit long
def bedroom():
    global begin,value,usr_input,moveset,money,i
    clear()
    if begin == True:
        start="You wake up in your house, you feel a bit drowsy. but you decide to have a look around..."
        begin=False
    else:
        start=""
    
    moveset = ["grab note","note","hallway","hall","wallet","grab wallet"]
    print(f"{start}\nThere is a 'note' and a 'wallet' on your desk and a door that goes out to a hallway")

    move()
    if usr_input== "hallway" or usr_input=="hall":
        home_hallway()
    elif usr_input=="note" or usr_input=="open note":

        clear();print(f"You pick up the note, it reads...\nHello {user}, Thank you for your $69 purchase of [CONTENT NOT INCLUDED]\nWe at \033[1;36;48mGenicStudios™\033[1;0;48m are grateful of your patronage. In return, we offer more content in the form of DLC's (Sold Seperately) for only! $23 per DLC!\nNo need to thank us. We humbly do request that you buy these immedietly")
        sub_input=input("\033[1;32;48mWould you like to purchase the DLC?\033[1;0;48m [Y/n]\n")
        submove = ["y","n","yes","no"];sub_input=sub_input.lower()


        while sub_input not in submove:
            print(out["un"])
            sub_input=input("Would you like to purchase the DLC? [Y/n]\n")
        if sub_input=="y" or sub_input=="yes":
            print("Uh oh! Looks like you have insufficient funds!")
            time.sleep(3)
            bedroom()
        elif sub_input=="n" or sub_input=="no":
            print("Oh well, Next time...")
            time.sleep(3)
            bedroom()
    elif usr_input=="grab wallet" or usr_input=="wallet":
        if i<=2:
            clear();print("You grab your wallet, it has a few things inside; which could be important but most notably it has some cash inside.")
            i+=1
            value=-20;mon()
            print(f"you now have ${money} in your pocket")
            usr_input=input("Press \033[1;36;48m[Enter]\033[1;0;48m to continue...\033[1;39;48m")
            print("\033[1;0;48m")
            bedroom()
        else:
            clear();print("stop taking advantage of the bug!! not very nice!")
            money -= 10
            print(f"You now have ${money} in your pocket");time.sleep(4)
            bedroom()


def home_hallway():
    global dlc, usr_input, moveset
    clear();print("The hallway is warmly lit by sun entering the room, with a nice painting on the wall\nThere is your bedroom, kitchen, and the front door")
    moveset=["painting","bedroom","move painting","kitchen","front door"]

    move()
    if usr_input=="painting":
        clear();print("""You look at the painting\nThe person in the painting looks oddly similar to yourself\nit seems quite loose from the wall, maybe you can move it?""")
        time.sleep(5)
        home_hallway()
    elif usr_input=="move painting":
        print("You move the painting and find a safe with a four digit passcode")
        sub_input =input("What is the code? [] [] [] []")
        if sub_input==s_code:
            expansion_dlc=True
            dlc=dlc+1
            print(f"You found a Divine Luminince Crystal! (Expansion DLC Acquired!)\n DLC's: {dlc}")
            time.sleep(5)
            home_hallway()
        elif sub_input!=s_code:
            print("The code is incorrect")
            time.sleep(4)
            home_hallway()
            
    elif usr_input=="bedroom":
        bedroom()
    elif usr_input=="kitchen":
        kitchen()
    elif usr_input=="front door":
        suburbia()

def kitchen():
    global usr_input,moveset,snack
    clear();print("Sunlight bleeds into the room revealing your unfortunately messy kitchen... you feel the urge to go for a snack.\nThere is a hallway, locked washroom door, and the front door.")
    moveset=["snack","eat","hallway","hall","washroom","front door"]
    
    move()
    if usr_input=="snack" or usr_input=="eat":
        if snack >=0:
            print("\nYou reach into your pantry and find a snack! You eat it.")
            time.sleep(4)
            snack+=1
            kitchen()
        elif snack>=2:
            ("\nSnacks!")
            snack+=1
            time.sleep(4)
            kitchen()
        elif snack>=5:
            print("\nWow, very well deserved...")
            time.sleep(4)
            snack+=1
            kitchen()
        elif snack>=10:
            print("\nYou have ran out of snacks...")
            time.sleep(4)
            kitchen()
    elif usr_input=="hallway" or usr_input=="hall":
        home_hallway()
    elif usr_input=="washroom":
        washroom()
    elif usr_input=="front door":
        suburbia()


def washroom():
    print("\nThe Washroom is locked. Try again later.");time.sleep(4)
    kitchen()

#Suburbia | this one is big!
def suburbia():
    global usr_input,moveset,sub
    if sub==False:
        srt="You step out into the blinding light. What surrounds you are big suburb homes and townhomes, you see your neighbour Will watering their plants.\nYou also notice your 'mailbox' is overflowing\nYou can travel in 4 directions, North, East, South, and West"
        sub = True
    elif sub==True:
        srt="You are standing next to your house where you are surrounded by homes, your neighbour will is sitting on their porch.\nYou can go inside your 'Home' or travel, North, East, West, or South."

    clear();print(srt)
    moveset=["mailbox","open mailbox","north","go north","east","go east","south","go south","west","go west","house","home"]; submoves=["y","yes","n","no"]

    move()
    if usr_input =="open mailbox" or usr_input=="mailbox":
        clear();print(f"You open your mailbox, nothing but junk mail and useless ads\nAlthough one note has 'IMPORTANT' as the title\nIt reads 'Dear {user}, due to some questionable... practices, we at \033[1;36;48mGenicStudios™\033[1;0;48m WILL disable your game if you do not purchase one of our various DLC's")
        sub_input=input("Please, would you like to buy our DLC's? [Y/n]? ");sub_input=sub_input.lower()
        if sub_input=="y" and "yes":
            clear();less_input=input("Please enter your payment info.\n")
            if rand <= 3:
                print("\nAccepted!\nPlease check later for your content to load!")
                time.sleep(4)
                suburbia()
            else:
                print("\nPAYMENT DECLINED, please try again later.")
                time.sleep(4)
                suburbia()
    elif usr_input=="go north" or usr_input=="north":
        if willmet==False:
            clear();print("You start walking North, unfortunately your neighbour Will stops you");willmet==True
            time.sleep(3)
            will()
        elif willmet==True:

            while sub_input not in submoves:
                print(out["un"])
                sub_input=input("Would you like to continue North? [Y/n]?\n");sub_input=sub_input.lower()
            if sub_input=="y" or sub_input=="yes":
                print("You decide to stop by Will's house, because why not?")
                time.sleep(3)
                will_house()
            elif sub_input=="n" or sub_input=="no":
                print(f"You continue walking up north, you pass rows of homes and you see kids playing up and down the suburban streets.\n you can't help but notice that some parts of the neighbourhood are missing textures, symbolized by the black and purple checkered patterns on certain objects\nYou now finally reach the forest")
                time.sleep(6)
                forest()
    elif usr_input=="go east" or usr_input=="east":
        print("You start heading east, as you walk down you notice that a whole road is missing! did the devs really forget to add a road here? anyways, you see a bakesale down the block")
        sub_input=input("Would you like to go to the bakesale? [Y/n]? ");sub_input=sub_input.lower()

        while sub_input not in submoves:
            print(out["un"])
            sub_input=input("would you like to go to the bakesale? [Y/n]? ");sub_input=sub_input.lower()
        if sub_input=="y" or sub_input=="yes":
            print("You change route and head to the bakesale")
            time.sleep(4)
            bakesale()
        elif sub_input=="n" or sub_input=="no":
            print("You continue north and near the downtown area of your city. You look up; only to see skyscrapers bound up, creating a formidable skyline")
            time.sleep(5)
            downtown()
    elif usr_input=="go west" or usr_input=="west":
        print("You head west, this area of the neighbourhood has an unsually high amount of flowers, you reach your destination")
        time.sleep(4)
        west()
    elif usr_input=="go south" or usr_input=="south":
        print("You head south, the roads start getting steeper up hill, you then see the mountains in the distance... How did you not see this before?")
        time.sleep(5)
        pleateu()
    elif usr_input=="home" or usr_input=="house":
        print("You walk up to your front door; open it and head inside")
        time.sleep(3)
        home_hallway()


def will():
    print("Will starts talking about plants, then something about Divine Luminence Crystals (DLC's) and something to do with a painting?\nWill then invites you inside")
    moveset=[] subset
    move()
def will_house():
    pass
def bakesale():
    pass
def forest():
    pass


def downtown():
    global usr_input,moveset,man
    clear();print("You walk through Downtown and it's packed, masses of people pass you, you aren't quite sure where to go from here. Although a building with big flashy lettering spelling out C A S I N O catches your eye\nYou can travel North, East, West or go to the Casino, Arcade, Pizza place, and/or the Recreation of the \033[1;36;48m'GenicStudios'™\033[1;0;48m Office building...")
    moveset=["go north","north","go east","east","go west","west","casino","arcade","genic studios","genic","genicstudios","pizza","garlic jims","pizza place"]
    submoves=["y","yes","n","no"]

    move()
    if usr_input=="genic studios" or usr_input=="genic" or usr_input=="genicstudios":
  
        if man==False:
            str="You suddenly get stopped by a man claiming to be able to give you DLC for cheap."
        elif man==True:
            str=""
        print(f"You walk towards the \033[1;36;48mGenicStudios™\033[1;0;48m Office, it looks way nicer in the game than in real life.\n{str}")
        while man==False:
            sub_input=input("Do you accept? [Y/n]? ")
            man=True
        while sub_input not in submoves:
            print(out["un"])
            sub_input=input("Do you accept? [Y/n]? ")
        if sub_input=="y" or sub_input=="yes":
            print("You just purchased unlicensed DLC!")
            less_input=input("Would you like to restart your game to apply DLC? [Y/n]? ")
            while less_input not in submoves:
                print(out["un"])
                less_input=input("Would you like to restart your game?")
            if less_input=="y" or "yes":
                clear();print("Restarting...");time.sleep(3)
                from stuff import illegal;illegal()
        elif sub_input=="n" or sub_input=="no":
            print("You tell the man no, and you continue on your path over to the\033[1;36;48m'GenicStudios'™\033[1;0;48m Building")
            time.sleep(4)
            genic()

    elif usr_input=="go north" or usr_input=="north":
        print("You go north and approach a grand building, It's the Capitol of where you live.")
        time.sleep(5)
        capitol()
    elif usr_input=="go east" or usr_input=="east":
        print("You head east to a different part of the city, It's called the Uptown")
        time.sleep(4)
        uptown()
    elif usr_input=="go west" or usr_input=="west":
        clear();print("You head west, over through the suburbs, a road appears to be missing from the game...")
        time.sleep(4)
        suburbia()
    elif usr_input=="casino":
        clear();print("You head over to the casino.")
        time.sleep(2)
        casino()
    elif usr_input=="arcade":
        clear();print("You go to the arcade, maybe you can play some games in there. Who knows?")
        time.sleep(3)
        arcade()
    elif usr_input=="pizza" or usr_input=="pizza place" or usr_input=="garlic jims":
        clear();print("You go to the pizza place, it has a sign above it 'Garlic Jims Famous Gourmet Pizza', a bit odd, and a lengthy name. but you decide you could go for something to eat.")
        Gjims()

def capitol():
    pass   

def casino():
    pass
def arcade():
    global money, usr_input, moveset,value
    clear();print("You enter the arcade, you look at your surroundings, a big dark room filled with rows of arcade cabinets waiting to be used\nYou can 'leave', use the 'token' machine, or play with the 3 open arcade cabinets, 'Blockage', 'Tom', 'Labyrinth' ")
    moveset=["leave","downtown","token","token machine","blockage","tom","labyrinth"]; submoves=["y","yes","n","no"]

    move()
    if usr_input=="leave" or usr_input=="downtown":
        print("You decide to exit the arcade")
        time.sleep(3)
        downtown()
    elif usr_input=="token" or usr_input=="token machine":
        clear();print("You go over to the token machine, you can spend cash to recieve some tokens to play the games.")
        sub_input=input("Would you like to purchase some tokens? [Y/n]? ")

        while sub_input not in submoves:
            print(out["un"])
            sub_input=input(out["opt"])
        if sub_input=="y" or sub_input=="yes":
            less_input=int(input("($0.50 per token)\nEnter the amount:"))
            t_price=less_input * 0.5

            if money==0:
                print("You do not have any cash")
                time.sleep(3)
                arcade()
            elif t_price >= money:
                print("Balance too low!")
                time.sleep(3)
                arcade()
            elif t_price <= money:
                sub_input=input(f"Are you sure you want to spend ${t_price} on {less_input} tokens? [Y/n]? ")

                while sub_input not in submoves:
                    print(out["un"])
                    sub_input=input(out["opt"])
                if sub_input=="y" or "yes":
                    token=less_input
                    money-=t_price
                    print(f"Transaction complete!\nYou now have: ${money}\nYou have {token} tokens.")
                    time.sleep(4)
                    arcade()
                elif sub_input=="n" or sub_input=="no":
                    print("You have decided not to spend your 'hard earned' cash on tokens...")
                    time.sleep(4)
                    arcade()
    elif usr_input=="blockage":
        print("You look at the machine that is labled 'Blockage' by \033[1;36;48mGenicStudios™\033[1;0;48m")
        sub_input=input("Do you want to play blockage? [Y/n]?\n");sub_input=sub_input.lower()
        
        while sub_input not in submoves:
            print(out["un"])
            sub_input=input(out["opt"]);sub_input=sub_input.lower()
        if sub_input=="yes" or sub_input=="y" and token>=1:
            print("You put your token into the machine and start playing Blockage")
            token-=1
            from arcadeGames import blockage
            blockage()
        elif sub_input=="no" or usr_input=="n":
            print("You decide not to play Blockage")
            arcade()

    elif usr_input=="tom":
        print("You look at the machine that is labled 'Tom: The Video Game'")
        sub_input=input("Do you want to play blockage? [Y/n]?\n");sub_input=sub_input.lower()
        
        while sub_input not in submoves:
            print(out["un"])
            sub_input=input(out["opt"]);sub_input=sub_input.lower()
        if sub_input=="yes" or sub_input=="y" and token>=1:
            print("You put your token into the machine and start playing Tom: The Video Game")
            token-=1
            from arcadeGames import tom
            tom()
        elif sub_input=="no" or usr_input=="n":
            print("You decide not to play Tom: The Video Game")
            arcade()

    elif usr_input=="labyrinth":
        print("You look at the machine that is labled 'Labyrinth' by \033[1;36;48mミラクルミュージカル\033[1;0;48m or Miracle Musical")
        sub_input=input("Do you want to play Labyrinth? [Y/n]?\n")
        
        while sub_input not in submoves:
            print(out["un"])
            sub_input=input(out["opt"])
        if sub_input=="yes" or sub_input=="y" and token>=1:
            print("You put your token into the machine and start playing Blockage")
            token-=1
            from arcadeGames import labyrinth
            labyrinth()
        elif sub_input=="no" or usr_input=="n":
            print("You decide not to play Labyrinth")
            arcade()

#GenicStudios Office!
def genic():
    global usr_input, money, moveset, value,dlc
    clear();print("As you enter the \033[1;36;48mGenicStudios™\033[1;0;48m Headquarters you are greeted by a Receptionist\nYou notice how pristine, clean and \x1B[3mfinished\x1B[23m the interior of the building looks, it's like you entered a new reality. Everything is arranged almost perfectly, you feel a bit intimidated by the enviorment of it...\nYou can leave, talk to the 'receptionist' or get 'water' from the water cooler")
    moveset=["leave","receptionist","talk","water","water cooler","appointment","DLC"]; submoves=["y","yes","n","no"]

    move()
    if usr_input=="leave":
        print("You leave the \033[1;36;48mGenicStudios™\033[1;0;48m office building. Freakish place to be honest, I can see why you left.")
        downtown()
    if usr_input=="water" or usr_input=="water cooler":
        print("You walk over to the water cooler, understandably so considering where you are.")
        if gen==False:
            str=" You take a step back, not expecting for the water cooler to speak\nWell... Do you want water? [Y/n]?"
        elif gen==True:
            str="[Y/n]?"

        sub_input=input(f"\"Would you like some water? [Y/n]?\" The machine kindly asks you.\n{str}")
        gen=True
        
        while sub_input not in submoves:
            print(out["un"])
            sub_input=input("Would you like some water? [Y/n]?\n")
        if sub_input=="y" or sub_input=="yes":
            print("The machine dispenses a nice cold cup of water, you grab it and slowly drink it, something... something's not quite right about it.\nYou also can't help but feel like you're being watched...")
            sus=1
        elif sub_input=="n" or sub_input=="no":
            print("You pass the chance to get some water")
        elif sub_input=="n" or sub_input=="no" and sus==1:
            print("You pass the chance to get some water... You don't feel comfortable drinking it")
    
    elif usr_input=="receptionist" or usr_input=="talk":
        clear();print(f"You go over to talk to the receptionist.\n\"Welcome {user}, to the \033[1;36;48mGenicStudios™\033[1;0;48m office! are you here for an 'Appointment' or to buy a 'DLC'?\"")
        
        move()
        if usr_input=="appointment":
            sub_input=input("The Receptionist looks at their computer and responds \"Are you Mr. Watson?\"[Y/n]? ")

            while sub_input not in submoves:
                print(out["un"])
                sub_input=input("Are you?\n")
            if sub_input=="y" or sub_input=="yes" and app==False:
                print("The receptionist then says \"Alright Mr. Watson, just step into that elevator and head to the 68th floor..,\"\nYou step into the elevator and it starts heading up to floor 68, you didn't even have to press any buttons\nWhat is even odder is that the entire elevator is encompassed in mirrors, you look to find your reflection staring back at yourself")
                app=True
                clear();print("You arrive to your destination... The scenery is a stark contrast from downstairs, everything is less grand, neat, nor perfect, you continue on and are met by a man.\n\"Hello I am Mr. Scribner, its great to see you actually please sit down\" He says.\nYou're intrigued by it and decide to sit down.\n Mr. Scribner then explains\"As the Founder and CEO of GenicStudios it's my duty to ensure that we make revenue and that our investors are happy.\"\nYou start feling as if you aren't iu te g4m3 a- m ")
                print("plers sign conract here...")
                submoves=["y","yes","n","no"]
             
                sub_input=input("¿Te gustarías firmar el contratemos? [Y/n]?\n");sub_input=sub_input.lower()
                while sub_input not in submoves:
                    print(out["un"])
                    sub_input=input("Would you like to sign the contract?\n");sub_input=sub_input.lower()
                if sub_input=="y" or sub_input=="yes":
                    print("You scan the contract ready to sign it but there are a few things wrong with it\nIt seems as part of the agreement you'd have to give your soul and property to GenicStudios? odd...")
                    sub_input=input("Do you still want to sign the contract?\n")
                    while sub_input not in submoves:
                        print(out["un"])
                        sub_input=input("Do you still want to sign the contract?\n")
                    if sub_input=="y" or sub_input=="yes":
                        less_input=input("Please print your name: ")
                        print("Signature"+less_input+"X")
                        print("You have signed your life, soul, property away to GenicStudios.")
                        print("""  ___  ___  __  __  ___         ___  __   __ ___  ___ 
                / __|/   \|  \/  || __|       / _ \ \ \ / /| __|| _ \
                | (_ || - || |\/| || _|       | (_) | \   / | _| |   /
                \___||_|_||_|  |_||___|       \___/   \_/  |___||_|_\
                            """)
                        usr_input=input("[T] Try Again?\n[R] Restart Game?\n[Q] Quit");usr_input=usr_input.upper()
                        if usr_input=="T":
                            clear();print("Processing...");time.sleep(3)
                            genic()
                        elif usr_input=="R":
                            clear();print("Restarting Game...");time.sleep(3)
                            startup()
                        elif usr_input=="Q":
                            clear();print("Exiting...");time.sleep(3)
                            exit
                    elif sub_input=="n" or sub_input=="no":
                        print("You refuse signing the contract and now Mickey Scribner is furious")
                        mick=True
                        fight()
                elif sub_input=="n" or sub_input=="no":
                    print("you reject the contract, Mickey Scribner, The CEO of GenicStudios is now furious and calls security to throw you out...")
                    mick=True
                    fight()

            elif sub_input=="n" or sub_input=="no":
                print("The receptionist then looks at the computer and responds \"It doesn't seem there's any other appointments today\"\nGreat... You screwed up, should have said you were this Mr. Watson person")
                genic()
            else:
                print("The receptionist tells you there are no appointmens.\nNo appointments?")
                genic()
    
        elif usr_input=="dlc" and horse_dlc==False:
            sub_input=input("\"There is one DLC avaible to pruchase, would you like to do so?\" Says the receptionist [Y/n]?")

            while sub_input not in submoves:
                print(out["un"])
                sub_input=input("Would you like to purchase DLC? [Y/n]?\n")
            if sub_input=="y" or sub_input=="yes" and money>=23:
                money -= 23
                dlc+=dlc
                print(f"You have purchased a DLC! for $23 (Horse Armor DLC Acquired!)\nWell... Was it worth it?\n Balance: {money}\nDLC's:{dlc}")
                horse_dlc=True

            elif sub_input=="n" or sub_input=="no":
                print("You decide to not purchase a DLC")
        else:
            print("There don't seem to be options here...")


def Gjims():
    global usr_input, moveset, money, value, employee
    print("You enter Garlic Jim's Pizza, and the smell of Garlic immedietly hits you. There is a cashier waiting patiently\nYou can, leave, order, or 'insult' the employee")
    moveset=["leave","order","insult","insult employee"];lessmoves=["P","C","M","H","S","J","K"]

    move()
    if usr_input=="leave":
        print("You leave the pizza place")
        downtown()
    elif usr_input=="order":
        less_input=("There are many things to order but it seems every option is only $12\n [C] Cheese Pizza\n [P] Pepperioni Pizza\n [M] Meat Lovers Pizza\n [H] Gourmet Hawaiian Pizza\n [S] Supreme Pizza\n [J] The Big Jimmy Pizza\n [K] Kiwi on Pizza\n");less_input=less_input.upper()

        while less_input not in lessmoves:
            print(out["un"])
            less_input("What would you like to order?");less_input=less_input.upper()
        if money <=12:
            print("Balance not enough")
        elif less_input=="C" or less_input=="P" or less_input=="M" or less_input=="S":
            mon();value=12
            b_pizza=True
            print("You order your Pizza of choice, kind of basic... (Pizza acquired!)")
        elif less_input=="H":
            u_pizza=True
            print("You order your... is that? p- p... Pineapple... on your pizza? ew. (Undesirable Pizza Aqcuired!)")
            mon();value=12

        elif less_input=="K":
            mon();value=12
            u_pizza=True
            print("You order your... okay... Kiwi? Really? who decided to put kiwi on their fucking pizza?! (Undesirable Pizza Acquired!)")
        elif less_input=="J":
            mon();value=12
            p_pizza=True
            print("You order the Big Jimmy, a glorious pizza! (Preminum Pizza Acquired!)")
    elif usr_input=="insult" or usr_input=="insult employee":
        print("You insult the employee, but they* doesn't seem to appreciate that...")
        employee=True
        fight()

def uptown():
    pass
def west():

    if expansion_dlc==True:
        print("Welcome to this area...\nWhat did you expect..? well... go on now, feel proud that you purchased this DLC.")
        fake=input("Press [ENTER] to continue")

    elif expansion_dlc==False:
        clear();print("As you apporach you unexpectedly hit a wall. Ouch*")
        print("""   ___     _       ___              ___     ___    ___     _   _    ___     ___     ___     ___   
    |   \   | |     / __|            | _ \   | __|  / _ \   | | | |  |_ _|   | _ \   | __|   |   \  
    | |) |  | |__  | (__             |   /   | _|  | (_) |  | |_| |   | |    |   /   | _|    | |) | 
    |___/   |____|  \___|            |_|_\   |___|  \__\_\   \___/   |___|   |_|_\   |___|   |___/  
    Please buy the required DLC (Expansion DLC) from the official \033[1;36;48mGenicStudios™\033[1;0;48m store in order to pass
        """)
        print("It seems that a lovely pop-up has appeared\nYou can go back East or try heading 'West' again")
        moveset=["east","west"]
        move()
        if usr_input=="west":
            west()
        elif usr_input=="east":
            print("You head east, back to the Suburbs.")
            suburbia()
    

def pleateu():
    pass
def mountain():
    pass

def fight():
    pass

startup()
"""
Side notes for later!:

Jenkins Marvin~
Charlie Roberts?
Destroying a sweater...

Linus Tech Tips
Tuesday, finest day in existance?
pay2win
"""