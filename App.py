#This portion of the Package is where the actual game is played by using input and print systems.
#The game will give a short description of the game as well as import the roles and game systems for then user to play
#
import random

import Game
import Role1
import Role2
print("Hello Player, Welcome to the heist") #Introduces Player to the game
Char_Choice = input("Please pick a Character 1.Thug 2. Spy: ")
if Char_Choice == "Thug":
    
    Game.stat_phy = Role1.t_Phy
    print(Game.stat_phy)
    Game.stat_IQ = Role1.t_IQ
    Game.stat_CHA = Role1.t_CHA
    Game.stat_HP = Role1.t_HP
    print("You chose the brutal Thug")
elif Char_Choice == "Spy":
    
    print("You chose the sneaky Spy")
else:
    print ("not a valid option")


print("You job will be to break into the Forfur Manor and steal the Gem that rest in the display. you'll have to get pass security, get through the guests, get into the room and get the gem.")

Chal_1 = input("First you'll have to get past the security of the party. are you [charm] them or [knock] him out?:")
if Chal_1 == "knock":
    Roll = Game.roll_phy(Game.stat_phy, Game.stat_HP)
if Chal_1 == "charm":
    Roll = Game.roll_CHA(Game.stat_CHA, Game.stat_HP)

Chal_2 = input("The party is in full swing, but now you have to slip past, do you plot a [route] to slip by undetected or [blend] in with the guest and wait for your time to strike")
if Chal_2 == "route":
    Roll = Game.roll_IQ(Game.stat_IQ, Game.stat_HP)
if Chal_2 == "blend":
    Roll = Game.roll_CHA(Game.stat_CHA, Game.stat_HP)

Chal_3 = input("you found the room where the Gem is being kept, but it's locked. do you [break] the door down or [pick] the lock")
if Chal_3 == "break":
    Roll = Game.roll_phy(Game.stat_phy, Game.stat_HP)
if Chal_3 == "pick":
    Roll = Game.roll_IQ(Game.stat_IQ, Game.stat_HP)


