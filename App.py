#This portion of the Package is where the actual game is played by using input and print systems.
#The game will give a short description of the game as well as import the roles and game systems for then user to play
#
import random

print("Hello Player, Welcome to the heist") #Introduces Player to the game
Char_Choice = input("Please pick a Character 1.Thug 2. Spy: ")
if Char_Choice == "Thug":
    import Role1
    print("You chose the brutal Thug")
if Char_Choice == "Spy":
    import Role2
    print("You chose the sneaky Spy")


