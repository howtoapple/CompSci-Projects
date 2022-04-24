#Arch Simple, [Do not touch, already done.]
import os, time
cont="";term="";clear = lambda:os.system('clear')
help=["pacman -Syu | Updates System", "credits | Display's credits"]

def inst_bar():
    global prog
    prog =" community             256.0 KiB   816 KiB/s 00:01 [---Co o  o  o  o  o  o  ]  21%"
    print(prog);time.sleep(1);clear
    prog =" community             624.0 KiB   957 KiB/s 00:02 [--------Co  o  o  o  o  ]  36%"
    print(prog);time.sleep(1);clear
    prog =" community             1245.0 KiB   892 KiB/s 00:03 [----------------Co  o  ]  62%"
    print(prog);time.sleep(1);clear
    prog =" community             1967.0 KiB   926 KiB/s 00:04 [-----------------------]  100%\n multilib"
    print(prog);time.sleep(1);clear


def linux_cmd():
    global term
    while term == "pacman -Syu":
        p = input("Sudo Password?")
        while True:
            if p == password:
                print(":: Syncronizing package databases...")
                time.sleep(1)
                print("archlinux_repo\narchlinux_repo_3party\ncore\nextra")
                inst_bar()
                term=""
                break
            else:
                print("Incorrect Password")
            continue
    if term == "warp-cli connect":
        print("Success!")
        term =""
    elif term.upper() == "CONTENT NOT INCLUDED" or term.upper() == ("CONTENTNOTINCLUDED"):
        import ContentNotIncluded
    elif term == "credits":
        print("Developers  :   Jakeob \n                XeonElemental\n                ")
        print("Special Mentions:   Rory The Cat!\n                 Jared Merrill\n                 Stryxu\n")

    elif term == "help":
        print(help)

def interface():
    global cont, term
    cont = input("What would you like to do?\n [P] Play 'Content Not Included'\n [T] Open Terminal\n [S] Shutdown\n");cont=cont.upper()

    while term == "" and cont=="T":
        print(f"""                    /-
                   ooo:
                  yoooo/
                 yooooooo
                yooooooooo
               yooooooooooo
             .yooooooooooooo                GenicStudios™ Presents...
            .oooooooooooooooo
           .oooooooarcoooooooo              ArchSimple
          .ooooooooo-oooooooooo             ---------------------- 
         .ooooooooo-  oooooooooo            
        :ooooooooo.    :ooooooooo           Made with <3
       :ooooooooo.      :ooooooooo          DE: Hawaii Part II
      :oooarcooo         .oooarcooo         Kernal: x86_64 Linux 5.16.5-ARCH
     :ooooooooy           .ooooooooo        Terminal: Content Not Included
    :ooooooooo   /ooooooooooooooooooo       
   :ooooooooo      .-ooooooooooooooooo.   
  ooooooooo-             -ooooooooooooo.  
 ooooooooo-                 .-oooooooooo. 
ooooooooo.                     -ooooooooo

    """)
    
        term = input(f"[{user}@DefaultSystem ~]$ ")
        linux_cmd()

        cont = input("\nWhat would you like to do?\n [P] Play 'Content Not Included'\n [T] Open Terminal\n [S] Shutdown\n");cont=cont.upper()
        continue
    if cont =="P":
        os.system('clear');print("Starting..");time.sleep(2)
        import ContentNotIncluded
    else:
        exit()

user, password = input("Your name?\n"), input("Password?\n")
interface()