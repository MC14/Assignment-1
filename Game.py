#This is the Game Program, this is where all of the Game's functions and work. it has three functions for each stat you can roll in the game
#It uses the random module in order to gives us random numbers from a range to simulate dice and give a result that, if high enough passes the test and continue the game
#but if too low, it gives a game over and ends the program


import random #imports andom in order to be used in the program
import Role1 #allows you to use the Role 1 stats
import Role2 #allows you to use the Role 2 stats


loop_trigger = 0 #starts loop at zero so it can be used in App program


def roll_phy(role_d): #a function that takes the class from whatever role given in order to get the stats needed 

    dice_roll1 = random.randrange (1,7) #a variable that uses randrange in order to give a random number from 1 to 6
    dice_roll2 = random.randrange (1,7) # a second variable with the same purpose, but used for the print statement
    dice_result = dice_roll1 +dice_roll2 + role_d.r_phy #variable gives the total from the two dice_roll variables and adds the phy stat from the role 
    
    print(dice_roll1,"+",dice_roll2,"+",role_d.r_phy,"=",dice_result) #print the outline of all the variables to show the player how it exactly added up
    if dice_result <= 3: #start of the if statement to show what the exact result is, if less than 3, it games over and stops the game
        print("Mega Failure!")
        print("Game over!, you only get once chance to steal the Gem") #tells the player they lost
        exit() #exits the program

    elif dice_result > 3 and dice_result <= 6: #if the result number is greater than 3 but less than or equal to 6, give this print statement
        print("Failure")
        print("So close! but....Game over, you only get once chance to steal the Gem") #tells the player they lost
        exit()

    elif dice_result > 6 and dice_result <=10: #greater than 7 and less than or equal to 10, succeed and continue the game
        print("Success, you made it")
    elif dice_result > 10: #if the result is greater than 10
        print("Super Success! You're really strong") 
        role_d.r_phy = role_d.r_phy + 1 #gives a little bonus for having a really good score, it ups the stat by 1, making it easier to get better scores
    

    return dice_result #returns the dice_result and goes back to the App when done

def roll_IQ(role_d): #follows many of the same code as roll_Phy but using the IQ stat instead of the Class Phy stat
    dice_roll1 = random.randrange (1,7)
    dice_roll2 = random.randrange (1,7)
    dice_result = dice_roll1 +dice_roll2 + role_d.r_IQ
    
    print(dice_roll1,"+",dice_roll2,"+",role_d.r_IQ,"=",dice_result)
    if dice_result <= 3:
        print("Mega Failure!")
        print("Game over!, you only get once chance to steal the Gem")
        exit()
    elif dice_result > 3 and dice_result <= 6:
        print("Failure")
        print("Game over!, you only get once chance to steal the Gem")
        exit()
    elif dice_result > 6 and dice_result <=10:
        print("Success, you made it")
    elif dice_result > 10:
        print("Super Success!") 
        role_d.r_IQ = role_d.r_IQ + 1
        
    return dice_result

def roll_CHA(role_d): #follows many of the same code as the other two but instead for the Class CHA stat
    dice_roll1 = random.randrange (1,7)
    dice_roll2 = random.randrange (1,7)
    dice_result = dice_roll1 +dice_roll2 + role_d.r_CHA
    
    print(dice_roll1,"+",dice_roll2,"+",role_d.r_CHA,"=",dice_result)
    if dice_result <= 3:
        print("Mega Failure!")
        print("Game over!, you only get once chance to steal the Gem")
        exit()
    elif dice_result > 3 and dice_result <= 6:
        print("Failure")
        print("Game over!, you only get once chance to steal the Gem")
        exit()
    elif dice_result > 6 and dice_result <=10:
        print("Success, you made it")
    elif dice_result > 10:
        print("Super Success!") 
        role_d.r_CHA = role_d.r_CHA + 1
    return dice_result
