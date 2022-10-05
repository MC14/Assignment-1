
import App
import random #imports Random in order to be used in the program
import Role1 #allows you to use the Role 1 stats
import Role2 #allows you to use the Role 2 stats

stat_phy = 0 #variables for the stats in order to put the Role stats into for the functions
stat_IQ = 0
stat_CHA = 0

def roll_phy(stat_phy):

    dice_roll1 = random.randrange (1,7)
    dice_roll2 = random.randrange (1,7)
    dice_result = dice_roll1 +dice_roll2 + stat_phy
    
    print(dice_roll1,"+",dice_roll2,"+",stat_phy,"=",dice_result)
    if dice_result <= 3:
        print("Mega Failure!")
        print("Game over!, you only get once chance to steal the Gem")
        exit()
    if dice_result > 3 and dice_result <= 6:
        print("Failure")
        print("Game over!, you only get once chance to steal the Gem")
        exit()
    if dice_result > 6 and dice_result <=10:
        print("Success, you made it")
        App.loopy = 1
    if dice_result > 10:
        print("Super Success!") 
        stat_phy = stat_phy + 1
        print(stat_phy)
        App.loopy = 1
    

    return dice_result

def roll_IQ(stat_IQ):
    dice_roll1 = random.randrange (1,7)
    dice_roll2 = random.randrange (1,7)
    dice_result = dice_roll1 +dice_roll2 + stat_IQ
    
    print(dice_roll1,"+",dice_roll2,"+",stat_IQ,"=",dice_result)
    if dice_result <= 3:
        print("Mega Failure!")
        print("Game over!, you only get once chance to steal the Gem")
        exit()
    if dice_result > 3 and dice_result <= 6:
        print("Failure")
        print("Game over!, you only get once chance to steal the Gem")
        exit()
    if dice_result > 6 and dice_result <=10:
        print("Success, you made it")
        App.loopy = 1
    if dice_result > 10:
        print("Super Success!") 
        stat_IQ = stat_IQ + 1
        
    return dice_result

def roll_CHA(stat_CHA):
    dice_roll1 = random.randrange (1,7)
    dice_roll2 = random.randrange (1,7)
    dice_result = dice_roll1 +dice_roll2 + stat_CHA
    
    print(dice_roll1,"+",dice_roll2,"+",stat_CHA,"=",dice_result)
    if dice_result <= 3:
        print("Mega Failure!")
        print("Game over!, you only get once chance to steal the Gem")
        exit()
    if dice_result > 3 and dice_result <= 6:
        print("Failure")
        print("Game over!, you only get once chance to steal the Gem")
        exit()
    if dice_result > 6 and dice_result <=10:
        print("Success, you made it")
        App.loopy = 1
    if dice_result > 10:
        print("Super Success!") 
        stat_CHA = stat_CHA + 1
        print(stat_CHA)
        App.loopy = 1
    return dice_result
