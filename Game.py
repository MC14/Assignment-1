

import random
import Role1
import Role2

stat_phy = 0
stat_IQ = 0
stat_CHA = 0
stat_HP = 0

def roll_phy(stat_phy):

    dice_roll1 = random.randrange (1,7)
    dice_roll2 = random.randrange (1,7)
    dice_result = dice_roll1 +dice_roll2 + stat_phy
    
    print(dice_roll1,"+",dice_roll2,"+",stat_phy,"=",dice_result)
    if dice_result <= 3:
        print("Mega Failure!")
        stat_phy = stat_phy - 1
        stat_HP = stat_HP - 1
    if dice_result > 3 and dice_result <= 7:
        print("Failure")
        stat_HP = stat_HP - 1
    if dice_result > 7 and dice_result <=10:
        print("Success, you made it")
    if dice_result > 10:
        print("Super Success!") 
        stat_phy = stat_phy + 1
    

    return dice_result

def roll_IQ():
    dice_roll1 = random.randrange (1,7)
    dice_roll2 = random.randrange (1,7)
    dice_result = dice_roll1 +dice_roll2 + stat_IQ
    
    print(dice_roll1,"+",dice_roll2,"+",stat_IQ,"=",dice_result)
    if dice_result <= 3:
        print("Mega Failure!")
        stat_IQ = stat_IQ - 1
        stat_HP = stat_HP - 1
    if dice_result > 3 and dice_result <= 7:
        print("Failure")
        stat_HP = stat_HP - 1
    if dice_result > 7 and dice_result <=10:
        print("Success, you made it")
    if dice_result > 10:
        print("Super Success!") 
        stat_IQ = stat_IQ + 1
    return dice_result

def roll_CHA():
    dice_roll1 = random.randrange (1,7)
    dice_roll2 = random.randrange (1,7)
    dice_result = dice_roll1 +dice_roll2 + stat_CHA
    
    print(dice_roll1,"+",dice_roll2,"+",stat_CHA,"=",dice_result)
    if dice_result <= 3:
        print("Mega Failure!")
        stat_CHA = stat_CHA - 1
        stat_HP = stat_HP - 1
    if dice_result > 3 and dice_result <= 7:
        print("Failure")
        stat_HP = stat_HP - 1
    if dice_result > 7 and dice_result <=10:
        print("Success, you made it")
    if dice_result > 10:
        print("Super Success!") 
        stat_CHA = stat_CHA + 1
    return dice_result
