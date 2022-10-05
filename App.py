#This portion of the Package is where the actual game is played by using input and print systems.
#The game will give a short description of the game as well as import the roles and game systems for then user to play
#then it will use function calls to the other programs in order to roll nice and continue the game
import Game
import Role1
import Role2
import time # the time module, I imported it to use the sleep function, this will help give pauses to the game, allowing text to be read and not spit out super fast
loopy = 0
print("Hello Player, Welcome to the Forfur Manor heist.") #Introduces Player to the game
time.sleep(2)
print("You job will be to break into the Forfur Manor and steal the Gem that rest in the display. you'll have to get pass security, get through the guests, get into the room and get the gem.") #explaining the backstory to the game
print("in order to pick what to do, please type the word that with be in the square brackets like this [example] exactly as written.") #explains how to use the input command and what to type in in order to reduce confusion
time.sleep(2)
 #gives the input command to choose what type of role you wanna play
while loopy == 0 :
    Char_Choice = input("Please pick a Character 1.[Thug] 2. [Spy]: ")
    if Char_Choice == "Thug": #an if statement saying that if they type Thug, it will make the Game stats used for rolls the same value as the role pick, either Thug or Spy
    
        Game.stat_phy = Role1.t_Phy #game stats refer to the varaible that will be in the roll functions being made to fit the role
        Game.stat_IQ = Role1.t_IQ
        Game.stat_CHA = Role1.t_CHA #the three stats for this game are Phy,IQ and CHA 
        print("You chose the brutal Thug")
        loopy = 1
    elif Char_Choice == "Spy": #an elif (else-if) statement so if Spy is chosen instead of Thug, 
    
        print("You chose the sneaky Spy")
        loopy = 1
    else:
        print("not a valid option")
        continue


loopy = 0
while loopy == 0 :
    Chal_1 = input("First you'll have to get past the security of the party.are you gonna [charm] him to let them pass or [knock] him out?: ")
    if Chal_1 == "knock":
        Roll = Game.roll_phy(Game.stat_phy)
    elif Chal_1 == "charm":
        Roll = Game.roll_CHA(Game.stat_CHA)
    else:
         print ("not a valid option")

loopy = 0
while loopy == 0:
    Chal_2 = input("The party is in full swing, but now you have to slip past, do you plot the best [route] to slip by undetected or [blend] in with the guest and wait for your time to strike: ")
    if Chal_2 == "route":
        Roll = Game.roll_IQ(Game.stat_IQ)
    elif Chal_2 == "blend":
        Roll = Game.roll_CHA(Game.stat_CHA)
    else:
        print ("not a valid option")
loopy = 0

while loopy == 0:
    Chal_3 = input("you found the room where the Gem is being kept, but it's locked. do you [break] the door down or [pick] the lock?: ")
    if Chal_3 == "break":
        Roll = Game.roll_phy(Game.stat_phy)
    elif Chal_3 == "pick":
        Roll = Game.roll_IQ(Game.stat_IQ)
    else:
        print ("not a valid option")
loopy = 0
print("You're finally into the room. the Gem is seating inside a glass case, there's a key pass and multiple cameras watching the gem.")
time.sleep(2)
while loopy == 0:
    Chal_4 = input("do you [shatter] the glass case, [decrypt] the key code or [disguise] yourself to fool the cameras?: ")
    if Chal_4 == "shatter":
        Roll = Game.roll_phy(Game.stat_phy)
    elif Chal_4 == "decrypt":
        Roll = Game.roll_IQ(Game.stat_IQ)
    elif Chal_4 == "disguise":
        Roll = Game.roll_CHA(Game.stat_CHA)
    else:
        print ("not a valid option")

print("congrats, you slipped away with the Gem in your hands, you're gonna be flithy rich!")
time.sleep(4)
exit()