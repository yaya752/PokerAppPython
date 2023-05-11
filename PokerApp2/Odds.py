
import numpy as np
def Straight(occur,i,cards,street,players):
    odd = 0
    return odd

def Straight_flush(occur,i,cards,street,players):
    odd = 0
    return odd

def Flush(occur,i,cards,street,players):
    odd = 0
    return odd

def Pair(occur, column, street, list_numplayers):
    odd = 0.
    hand = 0
    remaining = 0
    other = 0
    for i in range(len(occur)-3):
        if occur[i][column] == 1:
            hand += 1
        elif occur[i][column] == 0:
            remaining +=1
        else:
            other +=1
    if hand >= 2:
        return 1.
    elif other > 2:
        return 0.
    else:
        if street != "river" or street != "Summary" or street != "SHOW":
            if hand ==1:
                if street == "4th":
                    poss = (52 - 3 * list_numplayers[0]) * (51 - 4 * list_numplayers[0]) * (50 - 5 * list_numplayers[0]) * (49 - 6 * list_numplayers[0])
                    case_fav = poss - (52 - 3 * list_numplayers[0] - remaining) * (51 - 4 * list_numplayers[0] - remaining) * (50 - 5 * list_numplayers[0] - remaining) * (49 - 6 * list_numplayers[0] - remaining)
                    odd = case_fav / poss
                elif street == "5th":
                    poss = (51 - 3 * list_numplayers[0]-list_numplayers[1]) * (50 -3 * list_numplayers[0]- 2 * list_numplayers[1]) * (49-3 * list_numplayers[0] - 3 * list_numplayers[1])
                    case_fav = poss - (51 - 3 * list_numplayers[0]-list_numplayers[1] - remaining) * (50 -3 * list_numplayers[0]- 2 * list_numplayers[1] - remaining) * (49-3 * list_numplayers[0] - 3 * list_numplayers[1] - remaining)
                    odd = case_fav / poss   
                elif street == "6th":
                    poss = (50 - 3 * list_numplayers[0] - list_numplayers[1]) * (49 - 3 * list_numplayers[0]- 2 * list_numplayers[1])
                    case_fav = poss - (50 - 3 * list_numplayers[0] - list_numplayers[1]- remaining) * (49 - 3 * list_numplayers[0]- 2 * list_numplayers[1]- remaining)
                    odd = case_fav / poss
 
                elif street == "RIVER": 
                    poss = (49 - 3 * list_numplayers[0]-list_numplayers[1]-list_numplayers[2])
                    case_fav = remaining
                    odd = case_fav / poss
                else:
                    odd = 0.
            else:
                
                if street == "4th":
                    poss = (52 - 3 * list_numplayers[0]) * (51 - 4 * list_numplayers[0]) * (50 - 5 * list_numplayers[0]) * (49 - 6 * list_numplayers[0])
                    case_fav =poss -((52 - 3 * list_numplayers[0] - remaining) * (51 - 4 * list_numplayers[0] - remaining) * (50 - 5 * list_numplayers[0] - remaining) * (49 - 6 * list_numplayers[0] - remaining)+(52 - 3 * list_numplayers[0] - remaining) * (51 - 4 * list_numplayers[0] - remaining) * (50 - 5 * list_numplayers[0] - remaining) * (remaining)+(52 - 3 * list_numplayers[0] - remaining) * (51 - 4 * list_numplayers[0] - remaining) * (remaining) * (49 - 6 * list_numplayers[0] - remaining)+(52 - 3 * list_numplayers[0] - remaining) * (remaining) * (50 - 5 * list_numplayers[0] - remaining) * (49 - 6 * list_numplayers[0] - remaining)+(remaining) * (51 - 4 * list_numplayers[0] - remaining) * (50 - 5 * list_numplayers[0] - remaining) * (49 - 6 * list_numplayers[0] - remaining))
                    odd = case_fav / poss
                    print("********")
                    print(odd)
                elif street == "5th":
                    poss = (51 - 3 * list_numplayers[0]-list_numplayers[1]) * (50 -3 * list_numplayers[0]- 2 * list_numplayers[1]) * (49-3 * list_numplayers[0] - 3 * list_numplayers[1])
                    case_fav = poss -((remaining) *(50 -3 * list_numplayers[0]- 2 * list_numplayers[1] - remaining) * (49-3 * list_numplayers[0] - 3 * list_numplayers[1] - remaining)+(51 - 3 * list_numplayers[0]-list_numplayers[1] - remaining) *(remaining) * (49-3 * list_numplayers[0] - 3 * list_numplayers[1] - remaining)+(51 - 3 * list_numplayers[0]-list_numplayers[1] - remaining) *(50 -3 * list_numplayers[0]- 2 * list_numplayers[1] - remaining) * (remaining)+(51 - 3 * list_numplayers[0]-list_numplayers[1] - remaining) *(50 -3 * list_numplayers[0]- 2 * list_numplayers[1] - remaining) * (49-3 * list_numplayers[0] - 3 * list_numplayers[1] - remaining))
                    odd = case_fav / poss   
                elif street == "6th":
                    poss = (50 - 3 * list_numplayers[0] - list_numplayers[1]) * (49 - 3 * list_numplayers[0]- 2 * list_numplayers[1])
                    case_fav = (remaining)*(remaining-1)
                    odd = case_fav / poss
                else:
                    odd = 0.
        else:
            odd = 0
    return round(odd,3)

def Three_Kind(occur,column,street,list_numplayers):
    odd = 0.
    hand = 0
    remaining = 0
    other = 0
    for i in range(len(occur)-3):
        if occur[i][column] == 1:
            hand += 1
        elif occur[i][column] == 0:
            remaining +=1
        else:
            other +=1
    if hand >= 3:
        return 1.
    elif other > 1:
        return 0.
    else:
        if street != "river" or street != "Summary" or street != "SHOW":
            if hand ==0:
                if street == "4th":
                    
                    poss = (52 - 3 * list_numplayers[0]) * (51 - 4 * list_numplayers[0]) * (50 - 5 * list_numplayers[0]) * (49 - 6 * list_numplayers[0])
                    case_fav = remaining*(remaining-1)*(remaining-2)*(remaining-3)+(52 - 3 * list_numplayers[0] - remaining)*remaining*(remaining-1)*(remaining-2)+remaining*(51 - 4 * list_numplayers[0] - remaining)*(remaining-2)*(remaining-3)+remaining*(remaining-1)*(50 - 5 * list_numplayers[0] - remaining)*(remaining-3)+remaining*(remaining-1)*(remaining-2)*(49 - 6 * list_numplayers[0] - remaining)
                    odd = case_fav / poss
                    print("---------")
                    print(odd)
                elif street == "5th":
                    poss = (51 - 3 * list_numplayers[0]-list_numplayers[1]) * (50 -3 * list_numplayers[0]- 2 * list_numplayers[1]) * (49-3 * list_numplayers[0] - 3 * list_numplayers[1])
                    case_fav = remaining*(remaining-1)*(remaining-2)
                    odd = case_fav / poss   
                else:
                    odd = 0.
            if hand ==1:
                if street == "4th":
                    poss = (52 - 3 * list_numplayers[0]) * (51 - 4 * list_numplayers[0]) * (50 - 5 * list_numplayers[0]) * (49 - 6 * list_numplayers[0])
                    case_fav = poss - (52 - 3 * list_numplayers[0] - remaining) * (51 - 4 * list_numplayers[0] - remaining) * (50 - 5 * list_numplayers[0] - remaining) * (49 - 6 * list_numplayers[0] - remaining)
                    odd = case_fav / poss
                elif street == "5th":
                    poss = (51 - 3 * list_numplayers[0]-list_numplayers[1]) * (50 -3 * list_numplayers[0]- 2 * list_numplayers[1]) * (49-3 * list_numplayers[0] - 3 * list_numplayers[1])
                    case_fav = poss - (51 - 3 * list_numplayers[0]-list_numplayers[1] - remaining) * (50 -3 * list_numplayers[0]- 2 * list_numplayers[1] - remaining) * (49-3 * list_numplayers[0] - 3 * list_numplayers[1] - remaining)
                    odd = case_fav / poss   
                elif street == "6th":
                    poss = (50 - 3 * list_numplayers[0] - list_numplayers[1]) * (49 - 3 * list_numplayers[0]- 2 * list_numplayers[1])
                    case_fav = remaining*(remaining-1)
                    odd = case_fav / poss
                else:
                    odd = 0.
            else:
                if street == "4th":
                    poss = (52 - 3 * list_numplayers[0]) * (51 - 4 * list_numplayers[0]) * (50 - 5 * list_numplayers[0]) * (49 - 6 * list_numplayers[0])
                    case_fav =poss -((52 - 3 * list_numplayers[0] - remaining) * (51 - 4 * list_numplayers[0] - remaining) * (50 - 5 * list_numplayers[0] - remaining) * (49 - 6 * list_numplayers[0] - remaining)+(52 - 3 * list_numplayers[0] - remaining) * (51 - 4 * list_numplayers[0] - remaining) * (50 - 5 * list_numplayers[0] - remaining) * (remaining)+(52 - 3 * list_numplayers[0] - remaining) * (51 - 4 * list_numplayers[0] - remaining) * (remaining) * (49 - 6 * list_numplayers[0] - remaining)+(52 - 3 * list_numplayers[0] - remaining) * (remaining) * (50 - 5 * list_numplayers[0] - remaining) * (49 - 6 * list_numplayers[0] - remaining)+(remaining) * (51 - 4 * list_numplayers[0] - remaining) * (50 - 5 * list_numplayers[0] - remaining) * (49 - 6 * list_numplayers[0] - remaining))
                    odd = case_fav / poss
                elif street == "5th":
                    poss = (51 - 3 * list_numplayers[0]-list_numplayers[1]) * (50 -3 * list_numplayers[0]- 2 * list_numplayers[1]) * (49-3 * list_numplayers[0] - 3 * list_numplayers[1])
                    case_fav = poss -((remaining) *(50 -3 * list_numplayers[0]- 2 * list_numplayers[1] - remaining) * (49-3 * list_numplayers[0] - 3 * list_numplayers[1] - remaining)+(51 - 3 * list_numplayers[0]-list_numplayers[1] - remaining) *(remaining) * (49-3 * list_numplayers[0] - 3 * list_numplayers[1] - remaining)+(51 - 3 * list_numplayers[0]-list_numplayers[1] - remaining) *(50 -3 * list_numplayers[0]- 2 * list_numplayers[1] - remaining) * (remaining)+(51 - 3 * list_numplayers[0]-list_numplayers[1] - remaining) *(50 -3 * list_numplayers[0]- 2 * list_numplayers[1] - remaining) * (49-3 * list_numplayers[0] - 3 * list_numplayers[1] - remaining))
                    odd = case_fav / poss   
                elif street == "6th":
                    poss = (50 - 3 * list_numplayers[0] - list_numplayers[1]) * (49 - 3 * list_numplayers[0]- 2 * list_numplayers[1])
                    case_fav = (remaining)*(remaining-1)
                    odd = case_fav / poss
                elif street == "RIVER": 
                    odd=0.
                else:
                    odd = 0.
        else:
            odd = 0
    return round(odd,3)


def Four_Kind(tab_occur,column,cards,street,players):
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
    if (hand >=4):
        return 1.
    elif other >0:
        return 0.
    else:
        if street != "river" or street != "Summary" or street != "SHOW":
            odd = remaining/cards

        else:
            odd = 0.
    return round(odd,2)

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
def Calculate_odds(occur,street,list_numplayers):
    occur1 = np.zeros((len(occur),len(occur[0])))
    for i in range (len(occur)):
        for j in range(len(occur[1])):
            occur1[i][j] = occur[i][j]
    cards = NumCards(occur)
    for i in range (len(occur)-3):
        occur1[i][13] = Straight(occur,i,cards,street,list_numplayers)
        occur1[i][14] = Flush(occur,i,cards,street,list_numplayers)
        occur1[i][15] = Straight_flush(occur,i,cards,street,list_numplayers)
    for j in range (len(occur[0])-3):
        occur1[4][j] = Pair(occur,j,street,list_numplayers)
        occur1[5][j] = Three_Kind(occur,j,street,list_numplayers)
        occur1[6][j] = Four_Kind(occur,j,cards,street,list_numplayers)
    print(street)
    print(occur1)
    return occur1