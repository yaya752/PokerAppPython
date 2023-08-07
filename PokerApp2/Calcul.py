from Odds import Table
from High import *
from Low import *


def Calculate_odds(occur,street,list_numplayers):
    
    occur1 = Table()
    low_hand_odds = []
    for i in range (len(occur)):
        for j in range(len(occur[1])):
            occur1[i][j] = occur[i][j]
    

    '''staight_odds = round(Straight(occur,street,list_numplayers),2)'''
    low_hand_odds = low_hand_odd(occur1,street,list_numplayers)
    high_hand_odds = high_hand_odd(occur1,street,list_numplayers)
    '''for i in range (len(occur)-3):
        poss = list_Straight_flush(i)
        occur1[i][13] = staight_odds
        occur1[i][14] = round(Flush(occur, i, street, list_numplayers),2)
        occur1[i][15] = round(Straight_flush(occur,street,list_numplayers,poss),2)
    for j in range (len(occur[0])-3):
        occur1[4][j] = round(Pair(occur,j,street,list_numplayers),2)
        occur1[5][j] = round(Three_Kind(occur,j,street,list_numplayers),2)
        occur1[6][j] = round(Four_Kind(occur,j,street,list_numplayers),2)'''
    return (occur1,low_hand_odds,high_hand_odds)