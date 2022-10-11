
import random #imports andom in order to be used in the program
import Role1 #allows you to use the Role 1 stats
import Role2 #allows you to use the Role 2 stats


loop_trigger = 0


def roll_phy(role_d):

    dice_roll1 = random.randrange (5,7)
    dice_roll2 = random.randrange (5,7)
    dice_result = dice_roll1 +dice_roll2 + role_d.r_phy
    
    print(dice_roll1,"+",dice_roll2,"+",role_d.r_phy,"=",dice_result)
    if dice_result <= 3:
        print("Mega Failure!")
        print("Game over!, you only get once chance to steal the Gem")
        exit()

    if dice_result > 3 and dice_result <= 6:
        print("Failure")
        print("So close! but....Game over, you only get once chance to steal the Gem")
        exit()

    if dice_result > 6 and dice_result <=10:
        print("Success, you made it")
    if dice_result > 10:
        print("Super Success! You're really strong") 
        role_d.r_phy = role_d.r_phy + 1
        print(role_d.r_phy)
    

    return dice_result

def roll_IQ(role_d):
    dice_roll1 = random.randrange (1,7)
    dice_roll2 = random.randrange (1,7)
    dice_result = dice_roll1 +dice_roll2 + role_d.r_IQ
    
    print(dice_roll1,"+",dice_roll2,"+",role_d.r_IQ,"=",dice_result)
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
    if dice_result > 10:
        print("Super Success!") 
        role_d.r_IQ = role_d.r_IQ + 1
        
    return dice_result

def roll_CHA(role_d):
    dice_roll1 = random.randrange (5,7)
    dice_roll2 = random.randrange (5,7)
    dice_result = dice_roll1 +dice_roll2 + role_d.r_CHA
    
    print(dice_roll1,"+",dice_roll2,"+",role_d.r_CHA,"=",dice_result)
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
    if dice_result > 10:
        print("Super Success!") 
        role_d.r_CHA = role_d.r_CHA + 1
        print(role_d.r_CHA)
    return dice_result
