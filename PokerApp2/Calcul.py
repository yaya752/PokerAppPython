from Odds import Table
from HighV2 import *
from Low import *

def Calculate_odds(occur,street,list_numplayers):
    occur1 = Table()
    low_hand_odds = []
    for i in range (len(occur)):
        for j in range(len(occur[1])):
            occur1[i][j] = occur[i][j]
    low_hand_odds = low_hand_odd(occur1,street,list_numplayers)
    high_hand_odds = all_prob(occur,street,list_numplayers)
    return (occur1,low_hand_odds,high_hand_odds)