print("Unrecognized input")
usr_input=input("\n>");usr_input=usr_input.lower()

if usr_input == "roll":

    if play == 0:
        dice[0]=rand(); dice[1]=rand(); dice[2]=rand()
        print(dice)
        usr_input=input("Re-'roll' or Choose a dice to keep. [1] [2] [3]\n>")

        while usr_input not in appint:
            print("Unrecognized input")
            usr_input=input("\n>");usr_input=usr_input.lower()

        if usr_input == "1":
            dice[2] = (dice[0])
        elif usr_input =="2":
            dice[2] = (dice[1])
        elif usr_input=="3":
            dice[2] = (dice[2])
        elif usr_input=="roll":
            roll()

        play=+1
        roll()


    elif play == 1:
        dice[0]=rand(); dice[1]=rand()
        print(dice)
        play=+1

        usr_input=input("Choose a dice to keep. [1] [2]\n>")

        while usr_input not in appint:
            print("Unrecognized input")
            usr_input=input("\n>");usr_input=usr_input.lower()

        if usr_input == "1":
            dice[1] = (dice[0])
        elif usr_input =="2":
            dice[1] = (dice[1])
        play+=1
        roll()

    elif play == 2:
        dice[0]=rand()
        if dice[0] != dice[1]:
            print("You lose!")
        elif dice[0] == dice[1]:
            print("You win!")

    print(dice)
roll()