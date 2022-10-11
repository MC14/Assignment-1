#This portion of the Package is where the actual game is played by using input and print systems.
#The game will give a short description of the game as well as import the roles and game systems for then user to play
#then it will use function calls to the other programs in order to roll nice and continue the game
import Game # The Game module, imports it so that I can call functions from the Game program like loop.trigger
import time # the time module, I imported it to use the sleep function, this will help give pauses to the game, allowing text to be read and not spit out super fast


print("Hello Player, Welcome to the Forfur Manor heist.") #Introduces Player to the game

time.sleep(4) #gives a break in the message in order form the player to read it easier

print("You job will be to break into the Forfur Manor and steal the Gem that rest in the display. you'll have to get pass security, get through the guests, get into the room and get the gem.") #explaining the backstory to the game

print("in order to pick what to do, please type the word that with be in the square brackets like this [example] exactly as written.") #explains how to use the input command and what to type in in order to reduce confusion

time.sleep(6)
while Game.loop_trigger == 0 :#a simple while loop using a variable from the program that makes sure you stay in the loop until loop becomes 1
    
    Char_Choice = input("Please pick a Character 1.[Thug] 2. [Spy]: ") #gives the input command to choose what type of role you wanna play
    
    if Char_Choice == "Thug": #an if statement saying that if they type Thug, it will make the Game stats used for rolls the same value as the role pick, either Thug or Spy
        import Role1 #import info from Role 1 program
        role_d = Role1.Thug() #adds a refrence variable to the class Thug in order to be able to pull variables from it 
        print("You chose the brutal Thug") #Prints message to tell player they're choice was recieved
        Game.loop_trigger = 1 #make the loop variable 1 in order to break the loop and continue the game in the next loop/ 
    
    elif Char_Choice == "Spy": #an elif (else-if) statement so if Spy is chosen instead of Thug, it grabs the stuff from the Spy class in role 2
        import Role2 #import info from Role 2 program
        role_d = Role2.Spy() ##adds a refrence variable to the class Spy in order to be able to pull variables from it
        print("You chose the sneaky Spy") #Prints a message to tell player they're choice was recieved
        Game.loop_trigger = 1
    
    else: #else means any other input/message besides the ones describe fall under here
        print("not a valid option") #tells the player the message wasn't correct
        continue# continues the loop and keeps it going


Game.loop_trigger = 0 #makes loop 0 again in order to make another loop for the input decision
while Game.loop_trigger == 0 : #this while loop is for first choice of the game, rather "charm" or "knock"
    
    Chal_1 = input("First you'll have to get past the security of the party.are you gonna [charm] him to let them pass or [knock] him out?: ") #input command with a set-up for story reasons
    
    if Chal_1 == "knock": #if statement for typing "knock"
        Roll = Game.roll_phy(role_d) #Calls Game function roll_phy using role_d, this rolls the dice and then continues once done
        Game.loop_trigger = 1 #once again loop = 1 to break the loop and continue the game
    
    elif Chal_1 == "charm": #elif statement for the choice "charm"
        Roll = Game.roll_CHA(role_d) #rolls the Cha version for the roll function
        Game.loop_trigger = 1
    
    else:
         print ("not a valid option") #prints this and then continues the loop to try again

Game.loop_trigger = 0
while Game.loop_trigger == 0: #while loop for next challenge, this continues for the next couple of while loops with different combinations of stats to test your luck
    
    Chal_2 = input("The party is in full swing, but now you have to slip past, do you plot the best [route] to slip by undetected or [blend] in with the guest and wait for your time to strike: ")
    
    if Chal_2 == "route":
        Roll = Game.roll_IQ(role_d) #this variable calls the IQ version of the Roll function within the Game program
        Game.loop_trigger = 1
    
    elif Chal_2 == "blend":
        Roll = Game.roll_CHA(role_d)
        Game.loop_trigger = 1
    
    else:
        print ("not a valid option")
Game.loop_trigger = 0

while Game.loop_trigger == 0:
    
    Chal_3 = input("you found the room where the Gem is being kept, but it's locked. do you [break] the door down or [pick] the lock?: ")
    
    if Chal_3 == "break":
        Roll = Game.roll_phy(role_d)
        Game.loop_trigger = 1
    
    elif Chal_3 == "pick":
        Roll = Game.roll_IQ(role_d)
        Game.loop_trigger = 1
    
    else:
        print ("not a valid option")
Game.loop_trigger = 0

print("You're finally into the room. the Gem is seating inside a glass case, there's a key pass and multiple cameras watching the gem.")

time.sleep(2)

while Game.loop_trigger == 0: #In this loop, it gives three potential answer, one for each stat to allow you to use whatever stat is best to finish the job
    
    Chal_4 = input("do you [shatter] the glass case, [decrypt] the key code or [disguise] yourself to fool the cameras?: ")
    
    if Chal_4 == "shatter":
        Roll = Game.roll_phy(role_d)
        Game.loop_trigger = 1
    
    elif Chal_4 == "decrypt":
        Roll = Game.roll_IQ(role_d)
        Game.loop_trigger = 1
    
    elif Chal_4 == "disguise":
        Roll = Game.roll_CHA(role_d)
        Game.loop_trigger = 1
    
    else:
        print ("not a valid option")

print("congrats, you slipped away with the Gem in your hands, you're gonna be flithy rich!")
time.sleep(4)
exit() #closes the program, stops it 
