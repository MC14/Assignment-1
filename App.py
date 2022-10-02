#This portion of the Package is where the actual game is played by using input and print systems.
#The game will give a short description of the game as well as import the roles and game systems for then user to play
#
import random
from unittest import result
import Game

print("Hello Player, Welcome to the heist") #Introduces Player to the game
Char_Choice = input("Please pick a Character 1.Thug 2. Spy: ")
if Char_Choice == "Thug":
    import Role1
    Game.stat_phy = Role1.t_Phy
    Game.stat_IQ = Role1.t_IQ
    Game.stat_CHA = Role1.t_CHA
    Game.stat_HP = Role1.t_HP
    print("You chose the brutal Thug")
if Char_Choice == "Spy":
    import Role2
    print("You chose the sneaky Spy")

print("You job will be to break into the Forfur Manor and steal the Gem that rest in the display. you'll have to get pass security, get through the guests, sneak into the room and get the gem.")

Chal_1 = input("First you'll have to getb past the security of the party. are you [charm] them or [knock] him out?:")
if Chal_1 == "knock":
    Game.roll.phy(result)
    print(result)



