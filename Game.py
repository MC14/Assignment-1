

import random
import Role1
import Role2

stat_phy = 0
stat_IQ = 0
stat_CHA = 0
stat_HP = 0

def roll_phy(result):
    dice_roll = random.randrange (2, 13)
    result = dice_roll + stat_phy
    return result
