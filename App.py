#This portion of the Package is where the actual game is played by using input and print systems.
#The game will give a short description of the game as well as import the roles and game systems for then user to play
#
import random

import Game
import Role1
import Role2
import time 
print("Hello Player, Welcome to the Forfur Manor heist.") #Introduces Player to the game
time.sleep(5)
print("You job will be to break into the Forfur Manor and steal the Gem that rest in the display. you'll have to get pass security, get through the guests, get into the room and get the gem.")
print("in order to pick what to do, please type the word that with be in the square brackets like this [example] exactly as written.")
time.sleep(10)
Char_Choice = input("Please pick a Character 1.[Thug] 2. [Spy]: ")
if Char_Choice == "Thug":
    
    Game.stat_phy = Role1.t_Phy
    Game.stat_IQ = Role1.t_IQ
    Game.stat_CHA = Role1.t_CHA
    print("You chose the brutal Thug")
elif Char_Choice == "Spy":
    
    print("You chose the sneaky Spy")
else:
    print ("not a valid option")

Chal_1 = input("First you'll have to get past the security of the party.are you gonna [charm] him to let them pass or [knock] him out?: ")
if Chal_1 == "knock":
    Roll = Game.roll_phy(Game.stat_phy)
if Chal_1 == "charm":
    Roll = Game.roll_CHA(Game.stat_CHA)

Chal_2 = input("The party is in full swing, but now you have to slip past, do you plot the best [route] to slip by undetected or [blend] in with the guest and wait for your time to strike: ")
if Chal_2 == "route":
    Roll = Game.roll_IQ(Game.stat_IQ)
if Chal_2 == "blend":
    Roll = Game.roll_CHA(Game.stat_CHA)

Chal_3 = input("you found the room where the Gem is being kept, but it's locked. do you [break] the door down or [pick] the lock?: ")
if Chal_3 == "break":
    Roll = Game.roll_phy(Game.stat_phy)
if Chal_3 == "pick":
    Roll = Game.roll_IQ(Game.stat_IQ)

print("You're finally into the room. the Gem is seating inside a glass case, there's a key pass and multiple cameras watching the gem.")
time.sleep(5)
Chal_4 = input("do you [shatter] the glass case, [decrypt] the key code or [disguise] yourself to fool the cameras?: ")
if Chal_4 == "shatter":
    Roll = Game.roll_phy(Game.stat_phy)
if Chal_4 == "decrypt":
    Roll = Game.roll_IQ(Game.stat_IQ)
if Chal_4 == "disguise":
    Roll = Game.roll_CHA(Game.stat_CHA)

print("congrats, you slipped away with the Gem in your hands, you're gonna be flithy rich!")
time.sleep(4)
exit()