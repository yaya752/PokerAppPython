from wsgiref.util import setup_testing_defaults
import numpy as np
def list_Straight_flush(row):
    num = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
    suits = ['s','h','d','c']
    suit = suits[row]
    poss = []
    for i in range (9):
        poss.append([num[i] +suit,num[i+1]+suit,num[i+2]+suit,num[i+3]+suit,num[i+4]+suit])
    poss.append(['T'+suit,'J'+suit,'Q'+suit,'K'+suit,'A'+suit])

    return poss
def list_Straight():
    num = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
    poss = []
    for i in range (9):
        poss.append([num[i] ,num[i+1],num[i+2],num[i+3],num[i+4]])
    poss.append(['T','J','Q','K','A'])
    return poss
def list_remove_straight_flush(poss,i,j):
    num = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
    suit = ['s','h','d','c']
    card = num[j] + suit[i]
    new_poss = []
    k = 0
    for k in range (len(poss)):
        if not (card in poss[k]):
            new_poss.append(poss[k])
    return poss
def odd_card(card,occur,street,list_numplayers):
    num = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
    suit = ['s','h','d','c']
    i= suit.index(card[1])
    j= num.index(card[0])
    if occur[i][j] == 1:
        odd = 1
    elif occur[i][j] == -1:
        odd = 0
    else:
        if street == "4th":
            poss = (52 - 3 * list_numplayers[0]) * (51 - 4 * list_numplayers[0]) * (50 - 5 * list_numplayers[0]) * (49 - 6 * list_numplayers[0])
            case_fav = poss - (52 - 3 * list_numplayers[0] -1) * (51 - 4 * list_numplayers[0] - 1) * (50 - 5 * list_numplayers[0] - 1) * (49 - 6 * list_numplayers[0] - 1)
            odd = (1 / (52 - 3 * list_numplayers[0])) + (1 / (52 - 4 * list_numplayers[0]) ) + (1 / (52 - 5 * list_numplayers[0]) ) + (1 /( 52 - 6 * list_numplayers[0]))
        elif street == "5th":
            poss = (51 - 3 * list_numplayers[0]-list_numplayers[1]) * (50 -3 * list_numplayers[0]- 2 * list_numplayers[1]) * (49-3 * list_numplayers[0] - 3 * list_numplayers[1])
            case_fav = poss - (51 - 3 * list_numplayers[0]-list_numplayers[1] - 1) * (50 -3 * list_numplayers[0]- 2 * list_numplayers[1] - 1) * (49-3 * list_numplayers[0] - 3 * list_numplayers[1] - 1)
            odd = (case_fav / poss) * ((52-(3*list_numplayers[0]+list_numplayers[1]))/(52-(list_numplayers[0]+2+list_numplayers[1])))   
        elif street == "6th":
            poss = (50 - 3 * list_numplayers[0] - list_numplayers[1]- list_numplayers[2]) * (49 - 3 * list_numplayers[0]- list_numplayers[1]- 2 * list_numplayers[2])
            case_fav = poss - (50 - 3 * list_numplayers[0] - list_numplayers[1]- list_numplayers[2]- 1) * (49 - 3 * list_numplayers[0]- list_numplayers[1]- 2 * list_numplayers[2]- 1)
            odd = (case_fav / poss) * ((52-(3 * list_numplayers[0]+list_numplayers[1]+list_numplayers[2]))/(52-(list_numplayers[0]+2+list_numplayers[1]+list_numplayers[2])))
 
        elif street == "RIVER": 
            poss = (49 - 3 * list_numplayers[0]-list_numplayers[1]-list_numplayers[2]-list_numplayers[3])
            case_fav = 1
            odd = (case_fav / poss) * ((52-(3 * list_numplayers[0]+list_numplayers[1]+list_numplayers[2]+list_numplayers[3]))/(52-(list_numplayers[0]+2+list_numplayers[1]+list_numplayers[2]+list_numplayers[3])))
        else:
            odd = 0.

    return odd 
def odd_Straight_flush(straight,occur,street,list_numplayers):
    odd = 1
    remaining = 5 
    for cards in straight: 
        odd *= odd_card(cards,occur,street,list_numplayers)
        if odd_card(cards,occur,street,list_numplayers) == 1:
            remaining-=1
    if street == '4th' and remaining > 4:
        odd = 0
    elif street == '5th' and remaining > 3:
        odd = 0
    elif street == '6th' and remaining > 2:
        odd = 0
    elif street == 'RIVER' and remaining > 1:
        odd = 0
    elif street == 'SHOW' :
        odd = 0
    elif street == 'SUMMARY':
        odd = 0
    return odd
def odd_Straight(straight,occur,street,list_numplayers):
    odd = 1
    remaining = 5
    suits = ['s','h','d','c']
    for card in straight:
        odd_num = 0
        for suit in suits:
            cards =card+suit
            if odd_card(cards,occur,street,list_numplayers) == 1:
                odd_num = 1
                remaining-=1
            else:
                odd_num += odd_card(cards,occur,street,list_numplayers)
            print(odd_num)
        if (odd_num>1):
            odd *= 1
            if remaining == 0:
                return 1.
        else:
            odd *= odd_num
    if street == '4th' and remaining > 4:
        odd = 0
    elif street == '5th' and remaining > 3:
        odd = 0
    elif street == '6th' and remaining > 2:
        odd = 0
    elif street == 'RIVER' and remaining > 1:
        odd = 0
    elif street == 'SHOW' :
        odd = 0
    elif street == 'SUMMARY':
        odd = 0
    print("-------",odd )
    return odd
def Straight(occur,street,list_numplayers):
    odd = 0.
    poss = list_Straight()
    for straight in poss :
        odd+=odd_Straight(straight,occur,street,list_numplayers)
        if odd_Straight(straight,occur,street,list_numplayers) == 1:
            return 1. 
    return round(odd/len(poss),3)
def Straight_flush(occur,street,list_numplayers,poss):
    odd = 0.
    for straight in poss :
        odd+=odd_Straight_flush(straight,occur,street,list_numplayers)
        if odd_Straight_flush(straight,occur,street,list_numplayers) == 1:
            return 1.
    return round(odd/len(poss),3)

def Flush(occur, row, street, list_numplayers):
    odd = 0.
    other = 0
    remaining = 0
    hand = 0
    for j in range(len(occur[0])-3):
        if occur[row][j] == 1:
            hand += 1
        elif occur[row][j] == 0:
            remaining +=1
        else:
            other +=1
    if hand >= 5:
        return 1.
    elif remaining + hand <5:
        return 0.
    else:
        if  street != "SUMMARY" or street != "SHOW":
            if hand == 0:
                 odd = 0.
            elif hand == 1:
                if street == "4th":
                    poss = (52 - 3 * list_numplayers[0]) * (51 - 4 * list_numplayers[0]) * (50 - 5 * list_numplayers[0]) * (49 - 6 * list_numplayers[0])
                    case_fav = remaining*(remaining-1)*(remaining-2)*(remaining-3)
                    odd = case_fav / poss
                else:
                    odd = 0.
            elif hand == 2:
                if street == "4th":
                    poss = (52 - 3 * list_numplayers[0]) * (51 - 4 * list_numplayers[0]) * (50 - 5 * list_numplayers[0]) * (49 - 6 * list_numplayers[0])
                    case_fav = remaining*(remaining-1)*(remaining-2)*(remaining-3)+remaining*(remaining-1)*(remaining-2)*(52 - 6 * list_numplayers[0] - remaining +3)+remaining*(remaining-1)*(remaining-2)*(52 - 5 * list_numplayers[0] - remaining + 2)+remaining*(remaining-1)*(remaining-2)*(52 - 3 * list_numplayers[0])+remaining*(remaining-1)*(remaining-2)*(52 - 4 * list_numplayers[0] -(remaining-1))
                    odd = case_fav / poss
                elif street == "5th":
                    poss = (51 - 3 * list_numplayers[0]-list_numplayers[1]) * (50 -3 * list_numplayers[0]- 2 * list_numplayers[1]) * (49-3 * list_numplayers[0] - 3 * list_numplayers[1])
                    case_fav = remaining*(remaining-1)*(remaining-3)
                    odd = case_fav / poss   
                    odd = 0.
            elif hand == 3:
                if street == "4th":
                    poss = (52 - 3 * list_numplayers[0]) * (51 - 4 * list_numplayers[0]) * (50 - 5 * list_numplayers[0]) * (49 - 6 * list_numplayers[0])
                    case_fav = poss - (52 - 3 * list_numplayers[0] - remaining) * (51 - 4 * list_numplayers[0] - remaining) * (50 - 5 * list_numplayers[0] - remaining) * (49 - 6 * list_numplayers[0] - remaining)
                    odd = case_fav / poss
                elif street == "5th":
                    poss = (51 - 3 * list_numplayers[0]-list_numplayers[1]) * (50 -3 * list_numplayers[0]- 2 * list_numplayers[1]) * (49-3 * list_numplayers[0] - 3 * list_numplayers[1])
                    case_fav = remaining*(remaining-1)*(remaining-2)+remaining*(remaining-1)*(51 - 3 * list_numplayers[0]-list_numplayers[1]-remaining)+remaining*(remaining-1)*(50 -3 * list_numplayers[0]- 2 * list_numplayers[1]-remaining + 1)+remaining*(remaining-1)* (49-3 * list_numplayers[0] - 3 * list_numplayers[1]-remaining+2)
                    odd = case_fav / poss   
                elif street == "6th":
                    poss = (50 - 3 * list_numplayers[0] - list_numplayers[1]- list_numplayers[2]) * (49 - 3 * list_numplayers[0]- 2 * list_numplayers[1]- 2* list_numplayers[2])
                    case_fav = remaining*(remaining-1)
                    odd = case_fav / poss
                else:
                    odd = 0.
            elif hand == 4:
                if street == "5th":
                    poss = (51 - 3 * list_numplayers[0]-list_numplayers[1]) * (50 -3 * list_numplayers[0]- 2 * list_numplayers[1]) * (49-3 * list_numplayers[0] - 3 * list_numplayers[1])
                    case_fav = poss - (51 - 3 * list_numplayers[0]-list_numplayers[1] - remaining) * (50 -3 * list_numplayers[0]- 2 * list_numplayers[1] - remaining) * (49-3 * list_numplayers[0] - 3 * list_numplayers[1] - remaining)
                    odd = case_fav / poss
                elif street == "6th":
                    poss = (50 - 3 * list_numplayers[0] - list_numplayers[1]- list_numplayers[2]) * (49 - 3 * list_numplayers[0]- list_numplayers[1]- 2 * list_numplayers[2])
                    case_fav = remaining*(remaining-1)+(50 - 3 * list_numplayers[0] - list_numplayers[1]-remaining)*remaining+(49 - 3 * list_numplayers[0]- 2 * list_numplayers[1]-remaining+1)*remaining
                    odd = case_fav / poss
                elif street == "RIVER":
                    poss = (49 - 3 * list_numplayers[0]-list_numplayers[1]-list_numplayers[2]- list_numplayers[3])
                    case_fav = remaining
                    odd = case_fav / poss
                else:
                    odd = 0.
        else:
            odd = 0
    return round(odd,3)

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
        if street != "SUMMARY" or street != "SHOW":
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
                    poss = (50 - 3 * list_numplayers[0] - list_numplayers[1]- list_numplayers[2]) * (49 - 3 * list_numplayers[0]- list_numplayers[1]- 2 * list_numplayers[2])
                    case_fav = poss - (50 - 3 * list_numplayers[0] - list_numplayers[1]- list_numplayers[2]- remaining) * (49 - 3 * list_numplayers[0]- list_numplayers[1]- 2 * list_numplayers[2]- remaining)
                    odd = case_fav / poss
 
                elif street == "RIVER": 
                    poss = (49 - 3 * list_numplayers[0]-list_numplayers[1]-list_numplayers[2]-list_numplayers[3])
                    case_fav = remaining
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
                    poss = (50 - 3 * list_numplayers[0] - list_numplayers[1]- list_numplayers[2]) * (49 - 3 * list_numplayers[0]- list_numplayers[1]- 2 * list_numplayers[2])
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
        if street != "SUMMARY" or street != "SHOW":
            if hand ==0:
                if street == "4th":
                    poss = (52 - 3 * list_numplayers[0]) * (51 - 4 * list_numplayers[0]) * (50 - 5 * list_numplayers[0]) * (49 - 6 * list_numplayers[0])
                    case_fav = remaining*(remaining-1)*(remaining-2)*(remaining-3)+(52 - 3 * list_numplayers[0] - remaining)*remaining*(remaining-1)*(remaining-2)+remaining*(51 - 4 * list_numplayers[0] - (remaining-1))*(remaining-2)*(remaining-3)+remaining*(remaining-1)*(50 - 5 * list_numplayers[0] - (remaining-2))*(remaining-3)+remaining*(remaining-1)*(remaining-2)*(49 - 6 * list_numplayers[0] - (remaining-3))
                    odd = case_fav / poss
                elif street == "5th":
                    poss = (51 - 3 * list_numplayers[0]-list_numplayers[1]) * (50 -3 * list_numplayers[0]- 2 * list_numplayers[1]) * (49-3 * list_numplayers[0] - 3 * list_numplayers[1])
                    case_fav = remaining*(remaining-1)*(remaining-2)
                    odd = case_fav / poss   
                else:
                    odd = 0.
            elif hand ==1 :
                if street == "4th":
                    poss = (52 - 3 * list_numplayers[0]) * (51 - 4 * list_numplayers[0]) * (50 - 5 * list_numplayers[0]) * (49 - 6 * list_numplayers[0])
                    case_fav = poss - (((remaining) * (51 - 4 * list_numplayers[0] - (remaining-1)) * (50 - 5 * list_numplayers[0] - (remaining-1)) * (49 - 6 * list_numplayers[0] - (remaining-1)))+((52 - 3 * list_numplayers[0] - remaining) * (remaining) * (50 - 5 * list_numplayers[0] - (remaining-1)) * (49 - 6 * list_numplayers[0] - (remaining-1)))+((52 - 3 * list_numplayers[0] - remaining) * (51 - 4 * list_numplayers[0] - remaining) * (remaining) * (49 - 6 * list_numplayers[0] - (remaining-1)))+((52 - 3 * list_numplayers[0] - remaining) * (51 - 4 * list_numplayers[0] - remaining) * (50 - 5 * list_numplayers[0] - remaining) * (remaining))+(52 - 3 * list_numplayers[0] - remaining) * (51 - 4 * list_numplayers[0] - remaining) * (50 - 5 * list_numplayers[0] - remaining) * (49 - 6 * list_numplayers[0] - remaining))
                    odd = case_fav / poss
                elif street == "5th":
                    poss = (51 - 3 * list_numplayers[0]-list_numplayers[1]) * (50 -3 * list_numplayers[0]- 2 * list_numplayers[1]) * (49-3 * list_numplayers[0] - 3 * list_numplayers[1])
                    case_fav = poss - ((remaining) * (50 -3 * list_numplayers[0]- 2 * list_numplayers[1] - (remaining-1)) * (49-3 * list_numplayers[0] - 3 * list_numplayers[1] - (remaining-1))+(51 - 3 * list_numplayers[0]-list_numplayers[1] - remaining) * (remaining) * (49-3 * list_numplayers[0] - 3 * list_numplayers[1] - (remaining-1))+(51 - 3 * list_numplayers[0]-list_numplayers[1] - remaining) * (50 -3 * list_numplayers[0]- 2 * list_numplayers[1] - remaining) * (remaining)+(51 - 3 * list_numplayers[0]-list_numplayers[1] - remaining) * (50 -3 * list_numplayers[0]- 2 * list_numplayers[1] - remaining) * (49-3 * list_numplayers[0] - 3 * list_numplayers[1] - remaining))
                    odd = case_fav / poss   
                elif street == "6th":
                    poss = (50 - 3 * list_numplayers[0] - list_numplayers[1]- list_numplayers[2]) * (49 - 3 * list_numplayers[0]- list_numplayers[1]- 2 * list_numplayers[2])
                    case_fav = remaining*(remaining-1)
                    odd = case_fav / poss
                else:
                    odd = 0.
            else:
                if street == "4th":
                    poss = (52 - 3 * list_numplayers[0]) * (51 - 4 * list_numplayers[0]) * (50 - 5 * list_numplayers[0]) * (49 - 6 * list_numplayers[0])
                    case_fav = poss - (52 - 3 * list_numplayers[0] - remaining) * (51 - 4 * list_numplayers[0] - remaining) * (50 - 5 * list_numplayers[0] - remaining) * (49 - 6 * list_numplayers[0] - remaining)
                    odd = case_fav / poss

                elif street == "5th":
                    poss = (51 - 3 * list_numplayers[0]-list_numplayers[1]) * (50 -3 * list_numplayers[0]- 2 * list_numplayers[1]) * (49-3 * list_numplayers[0] - 3 * list_numplayers[1])
                    case_fav = poss - (51 - 3 * list_numplayers[0]-list_numplayers[1] - remaining) * (50 -3 * list_numplayers[0]- 2 * list_numplayers[1] - remaining) * (49-3 * list_numplayers[0] - 3 * list_numplayers[1] - remaining)
                    odd = case_fav / poss   
                elif street == "6th":
                    poss = (50 - 3 * list_numplayers[0] - list_numplayers[1]- list_numplayers[2]) * (49 - 3 * list_numplayers[0]- list_numplayers[1]- 2 * list_numplayers[2])
                    case_fav = poss - (50 - 3 * list_numplayers[0] - list_numplayers[1]- list_numplayers[2]- remaining) * (49 - 3 * list_numplayers[0]- list_numplayers[1]- 2 * list_numplayers[2]- remaining)
                    odd = case_fav / poss
 
                elif street == "RIVER": 
                    poss = (49 - 3 * list_numplayers[0]-list_numplayers[1]-list_numplayers[2]-list_numplayers[3])
                    case_fav = remaining
                    odd = case_fav / poss
                else:
                    odd = 0.
        else:
            odd = 0
    return round(odd,3)
def Four_Kind(occur,column,street,list_numplayers):
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
        if street != "RIVER" or street != "SUMMARY" or street != "SHOW":
            if hand == 0:
                if street == "4th":
                    poss = (52 - 3 * list_numplayers[0]) * (51 - 4 * list_numplayers[0]) * (50 - 5 * list_numplayers[0]) * (49 - 6 * list_numplayers[0])
                    case_fav = remaining*(remaining-1)*(remaining-2)*(remaining-3)
                    odd = case_fav / poss
                else:
                    odd = 0.
            elif hand ==1 :
                if street == "4th":
                    poss = (52 - 3 * list_numplayers[0]) * (51 - 4 * list_numplayers[0]) * (50 - 5 * list_numplayers[0]) * (49 - 6 * list_numplayers[0])
                    case_fav = (52 - 3 * list_numplayers[0])*remaining*(remaining-1)*(remaining-2)+remaining*(51 - 4 * list_numplayers[0]-remaining+1)*(remaining-1)*(remaining-2)+remaining*(remaining-1)*(50 - 5 * list_numplayers[0] -remaining + 2)*(remaining-2)+remaining*(remaining-1)*(remaining-2)*(49 - 6 * list_numplayers[0] - remaining+3)
                    odd = case_fav / poss
                elif street == "5th":
                    poss = (51 - 3 * list_numplayers[0]-list_numplayers[1]) * (50 -3 * list_numplayers[0]- 2 * list_numplayers[1]) * (49-3 * list_numplayers[0] - 3 * list_numplayers[1])
                    case_fav = remaining*(remaining-1)*(remaining-2)
                    odd = case_fav / poss   
                
                else:
                    odd = 0.
            elif hand == 2 :
                if street == "4th":
                    poss = (52 - 3 * list_numplayers[0]) * (51 - 4 * list_numplayers[0]) * (50 - 5 * list_numplayers[0]) * (49 - 6 * list_numplayers[0])
                    case_fav = poss - (((remaining) * (51 - 4 * list_numplayers[0] - (remaining-1)) * (50 - 5 * list_numplayers[0] - (remaining-1)) * (49 - 6 * list_numplayers[0] - (remaining-1)))+((52 - 3 * list_numplayers[0] - remaining) * (remaining) * (50 - 5 * list_numplayers[0] - (remaining-1)) * (49 - 6 * list_numplayers[0] - (remaining-1)))+((52 - 3 * list_numplayers[0] - remaining) * (51 - 4 * list_numplayers[0] - remaining) * (remaining) * (49 - 6 * list_numplayers[0] - (remaining-1)))+((52 - 3 * list_numplayers[0] - remaining) * (51 - 4 * list_numplayers[0] - remaining) * (50 - 5 * list_numplayers[0] - remaining) * (remaining))+(52 - 3 * list_numplayers[0] - remaining) * (51 - 4 * list_numplayers[0] - remaining) * (50 - 5 * list_numplayers[0] - remaining) * (49 - 6 * list_numplayers[0] - remaining))
                    odd = case_fav / poss
                elif street == "5th":
                    poss = (51 - 3 * list_numplayers[0]-list_numplayers[1]) * (50 -3 * list_numplayers[0]- 2 * list_numplayers[1]) * (49-3 * list_numplayers[0] - 3 * list_numplayers[1])
                    case_fav = (51 - 3 * list_numplayers[0]-list_numplayers[1]-remaining)*(remaining)*(remaining-1)+remaining*(50 -3 * list_numplayers[0]- 2 * list_numplayers[1]-remaining+1)*(remaining-1)+remaining*(remaining-1)*(49-3 * list_numplayers[0] - 3 * list_numplayers[1]-remaining+2)
                    odd = case_fav / poss
                elif street == "6th":
                    poss = (50 -3 * list_numplayers[0]- list_numplayers[1]-list_numplayers[2]) * (49-3 * list_numplayers[0]-list_numplayers[1] - 2 * list_numplayers[2])
                    case_fav = remaining*(remaining-1)
                    odd = case_fav / poss   
                
                else:
                    odd = 0.
            else:
                if street == "4th":
                    poss = (52 - 3 * list_numplayers[0]) * (51 - 4 * list_numplayers[0]) * (50 - 5 * list_numplayers[0]) * (49 - 6 * list_numplayers[0])
                    case_fav = poss - (52 - 3 * list_numplayers[0] - remaining) * (51 - 4 * list_numplayers[0] - remaining) * (50 - 5 * list_numplayers[0] - remaining) * (49 - 6 * list_numplayers[0] - remaining)
                    odd = case_fav / poss
                    
                elif street == "5th":
                    poss = (51 - 3 * list_numplayers[0]-list_numplayers[1]) * (50 -3 * list_numplayers[0]- 2 * list_numplayers[1]) * (49-3 * list_numplayers[0] - 3 * list_numplayers[1])
                    case_fav = poss - (51 - 3 * list_numplayers[0]-list_numplayers[1] - remaining) * (50 -3 * list_numplayers[0]- 2 * list_numplayers[1] - remaining) * (49-3 * list_numplayers[0] - 3 * list_numplayers[1] - remaining)
                    odd = case_fav / poss   
                elif street == "6th":
                    poss = (50 - 3 * list_numplayers[0] - list_numplayers[1]-list_numplayers[2]) * (49 - 3 * list_numplayers[0]- 2 *list_numplayers[2]- list_numplayers[1])
                    case_fav = poss - (50 - 3 * list_numplayers[0] - list_numplayers[1]- remaining) * (49 - 3 * list_numplayers[0]- 2 * list_numplayers[1]- remaining)
                    odd = case_fav / poss
 
                elif street == "RIVER": 
                    poss = (49 - 3 * list_numplayers[0]-list_numplayers[1]-list_numplayers[2]-list_numplayers[3])
                    case_fav = remaining
                    odd = case_fav / poss
                else:
                    odd = 0.
        else:
            odd = 0
    return round(odd,4)

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
    staight_odds = Straight(occur,street,list_numplayers)
    for i in range (len(occur)-3):
        poss = list_Straight_flush(i)
        occur1[i][13] = staight_odds
        occur1[i][14] = Flush(occur, i, street, list_numplayers)
        occur1[i][15] = Straight_flush(occur,street,list_numplayers,poss)
    for j in range (len(occur[0])-3):
        occur1[4][j] = Pair(occur,j,street,list_numplayers)
        occur1[5][j] = Three_Kind(occur,j,street,list_numplayers)
        occur1[6][j] = Four_Kind(occur,j,street,list_numplayers)
    return occur1