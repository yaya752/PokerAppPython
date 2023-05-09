
import numpy as np
def Straight(occur,i,cards,street):
    odd = 0
    return odd

def Straight_flush(occur,i,cards,street):
    odd = 0
    return odd

def Flush(occur,i,cards,street):
    odd = 0
    return odd

def Pair(tab_occur,column,cards,street):
    odd = 0.
    hand = 0
    remaining = 0
    other = 0 
    for i in range (len(tab_occur)-3):
        if tab_occur[i][column] == 1:
            hand += 1
        elif tab_occur[i][column] == 0:
            remaining +=1
        else:
            other +=1
    if (hand >=2):
        return 1.
    elif other >2:
        return 0.
    else:
        if street == "3rd":
            odd = 1-((cards-remaining)*(cards-remaining-1)*(cards-remaining-2)*(cards-remaining-3))/(cards*(cards-1)*(cards-2)*(cards-3))
        elif street =="4th":
            odd = 1-((cards-remaining)*(cards-remaining-1)*(cards-remaining-2))/(cards*(cards-1)*(cards-2))
        elif street == "5th":
            odd = 1-((cards-remaining)*(cards-remaining-1))/(cards*(cards-1))
        elif street == "6th":
            odd = 1-(cards-remaining)/cards
        elif street == "river":
            odd = 0.
        else:
            odd = 0.
    return round(odd,2)

def Three_Kind(tab_occur,column,cards,street):
    #for i in range (len(tab_occur)-3):
    odd = 0
    return odd

def Four_Kind(tab_occur,column,cards,street):
    #for i in range (len(tab_occur)-3):
    odd = 0
    return odd

def Table():
    num = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
    suit = ['s','h','d','c']
    occur = np.zeros((len(suit)+3,len(num)+3))
    return occur
def Append_cards(hand,occur,mainplayer,player):
    num = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
    suit = ['s','h','d','c']
    for card in hand:
        i= suit.index(card[1])
        j= num.index(card[0])
        if occur[i][j] == 0 :
            if mainplayer == player:
                occur[i][j] = 1
            else:
                occur[i][j] = -1
    return occur
def NumCards(occur):
    S = 0
    for i in range (len(occur)-3):
        for j in range (len(occur[0])-3):
            if occur[i][j] == 1 or occur[i][j] == -1:
                S+=1
    return 52-S
def Calculate_odds(occur,street):
    occur1 = np.zeros((len(occur),len(occur[0])))
    for i in range (len(occur)):
        for j in range(len(occur[1])):
            occur1[i][j] = occur[i][j]
    cards = NumCards(occur)
    for i in range (len(occur)-3):
        occur1[i][13] = Straight(occur,i,cards,street)
        occur1[i][14] = Flush(occur,i,cards,street)
        occur1[i][15] = Straight_flush(occur,i,cards,street)
    for j in range (len(occur[0])-3):
        occur1[4][j] = Pair(occur,j,cards,street)
        occur1[5][j] = Three_Kind(occur,j,cards,street)
        occur1[6][j] = Four_Kind(occur,j,cards,street)
    return occur1