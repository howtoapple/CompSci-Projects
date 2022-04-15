#Arch?
import os, time

user = input("What is your name?")
cont="";term="";clear = os.system('clear')

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
        print(":: Syncronizing package databases...")
        time.sleep(1)
        print("archlinux_repo\narchlinux_repo_3party\ncore\nextra")
        inst_bar()
        term=""
    if term == "warp-cli connect":
        print("Success!")
    

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
        linux_cmd()

        cont = input("\nWhat would you like to do next?\n [P] Play 'Content Not Included'\n [T] Open Terminal\n [S] Shutdown\n");cont=cont.upper()
        continue
    if cont =="P":
        os.system('clear')
        import ContentNotIncluded
    else:
        exit()

print("Boot Options:\nArch Linux\nArch Linux")

interface()