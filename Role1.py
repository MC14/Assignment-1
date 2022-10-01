from socket import TIPC_CONN_TIMEOUT


import random

t_Phy = 2 # The Physical stat for the Thug, will be used in challenges
t_IQ = 0 #The Intelligence stat for the Thug, will be used in challenges
t_CHA = -2 #The Charisma Stat for the Thug, will be used in challenges
t_HP = 3 #The Health Stat for the Thug, the amount of redo's the Thug has before getting a game over

def roll_Phy(result):
 dice_roll = random.randrange (1, 13)
 result = dice_roll + t_Phy
 return result

def roll_IQ(result):
 dice_roll = random.randrange (1, 13)
 result = dice_roll + t_IQ
 return result

def roll_CHA(result):
 dice_roll = random.randrange (1, 13)
 result = dice_roll + t_CHA
 return result