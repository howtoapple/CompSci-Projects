#Main structure of the MadLibs program
print("Hello")
name = input("What is your name? ")
print("Hello " + name + "!")
print("This is a MadLibs program, I will ask you...")

#user questions
Ad1 = input("Enter an Adjective ")
Ad2 = input("Enter a second Adjective ")
Ad3 = input("Enter a third Adjective ")
Adverb = input ("Enter a Adverb ")
Noun1 = input("Enter a noun ")
Noun2 = input("Enter a second noun ")
Noun3 = input("Enter a thrid noun ")
Noun4 = input("Enter a fourth noun ")
Noun5 = input("Enter a fitfh noun ")
Noun6 = input("Enter a sixth noun ")
PlNoun = input ("Now finally enter a plural noun ")

#stringing all the variables together
print ("Driving a car can be fun if you follow this " + Ad1 + " advice: When approaching a " + Noun1 + " on the right, always blow your " + Noun2 + " Before making an " + Ad2 + " turn, always stick your " + Noun3 + ". out of the window. Every 2000 miles, have your " + Noun4 + " inspected and your " + Noun5 + " checked. When approaching a school, watch out for " + Ad3 + " " + PlNoun + " Above all, drive " + Adverb + " The " + Noun6 + " you save may be your own! ")