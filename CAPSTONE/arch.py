#Arch?
import os, time

user = input("What is your name?")
cont="";term=""

def interface():
    global cont, term
    cont = input("What would you like to do next?\n [P] Play 'Content Not Included'\n [T] Open Terminal\n [S] Shutdown");cont=cont.upper()

    while term == "" and cont=="T":
        print(f"""                    /-
                   ooo:
                  yoooo/
                 yooooooo
                yooooooooo
               yooooooooooo
             .yooooooooooooo                GenicStudios Presents...
            .oooooooooooooooo
           .oooooooarcoooooooo              ArchLinux
          .ooooooooo-oooooooooo             ---------------------- 
         .ooooooooo-  oooooooooo            The Video Game
        :ooooooooo.    :ooooooooo           ----------------------
       :ooooooooo.      :ooooooooo          Created with <3
      :oooarcooo         .oooarcooo         Kernal: 5.16.5-arch
     :ooooooooy           .ooooooooo        Terminal: Content Not Included
    :ooooooooo   /ooooooooooooooooooo       
   :ooooooooo      .-ooooooooooooooooo.   
  ooooooooo-             -ooooooooooooo.  
 ooooooooo-                 .-oooooooooo. 
ooooooooo.                     -ooooooooo

    """)
        term = input(f"[{user}@DefaultSystem ~]$ ")
    if cont =="P":
        os.system('clear')
        import ContentNotIncluded
    else:
        exit()


print("""


 
                 .88888888:.
                88888888.88888.
              .8888888888888888.
              888888888888888888
              88' _`88'_  `88888
              88 88 88 88  88888
              88_88_::_88_:88888
              88:::,::,:::::8888              Tux The Penguin
              88`:::::::::'`8888              ------------------
             .88  `::::'    8:88.             Linux
            8888            `8:888.           For more info:
          .8888'             `888888.         https://linux.org/
         .8888:..  .::.  ...:'8888888:.
        .8888.'     :'     `'::`88:88888
       .8888        '         `.888:8888.
      888:8         .           888:88888
    .888:88        .:           888:88888:
    8888888.       ::           88:888888
    `.::.888.      ::          .88888888
   .::::::.888.    ::         :::`8888'.:.
  ::::::::::.888   '         .::::::::::::
  ::::::::::::.8    '      .:8::::::::::::.
 .::::::::::::::.        .:888:::::::::::::
 :::::::::::::::88:.__..:88888:::::::::::'
  `'.:::::::::::88888888888.88:::::::::'
miK     `':::_:' -- '' -'-' `':_::::'`""")

inst = input("Proceed with Install?\n [Y] [N]? ");inst=inst.upper()

if inst == "Y":
    os.system('clear')
    print("Processing...")
    time.sleep(5);print("Download complete!\nYou now have the sudden urge to tell everyone that you use Arch")
    interface();
elif inst == "N":
    exit()