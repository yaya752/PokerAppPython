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
def odd_first_card(card,occur,street,list_numplayers):
    odd = 0
    num = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
    suit = ['s','h','d','c']
    i= suit.index(card[1])
    j= num.index(card[0])
    if occur[i][j] == 1.:
        odd = 1
    elif occur[i][j] == -1.:
        odd = 0
    else:
        if street == "4th":
                num3 = list_numplayers[0]
                odd = 1/(52-(2+ num3))
        elif street == "5th":
                num3 = list_numplayers[0]
                num4 = list_numplayers[1]
                odd = 1/(52-(2+ num3+num4))
        elif street == "6th":
                num3 = list_numplayers[0]
                num4 = list_numplayers[1]
                num5 = list_numplayers[2]
                odd = 1/(52-(2+ num3+num4+num5))
        elif street == "RIVER": 
                num3 = list_numplayers[0]
                num4 = list_numplayers[1]
                num5 = list_numplayers[2]
                num6 = list_numplayers[3]
                odd = 1/(52-(2+ num3+num4+num5+num6))
    return odd
def odd_second_card(card,occur,street,list_numplayers):
    odd = 0
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
                num3 = list_numplayers[0]
                odd = (51-(2+num3))/((52-(2+ num3))*(52-(2+ 2*num3)))
        elif street == "5th":
                num3 = list_numplayers[0]
                num4 = list_numplayers[1]
                odd = (51-(2+ num3+num4))/((52-(2+ num3+num4))*(52-(2+ num3+2*num4)))
        elif street == "6th":
                num3 = list_numplayers[0]
                num4 = list_numplayers[1]
                num5 = list_numplayers[2]
                odd = (51-(2+ num3+num4+num5))/((52-(2+ num3+num4+num5))*(52-(2+num3+num4+2*num5)))
        elif street == "RIVER": 
                odd = 0
    return odd
def odd_third_card(card,occur,street,list_numplayers):
    odd = 0
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
                num3 = list_numplayers[0]
                odd = ((51-(2+num3))*(51-(2+ 2*num3)))/((52-(2+ num3))*(52-(2+ 2*num3))*(52-(2+ 3*num3)))
        elif street == "5th":
                num3 = list_numplayers[0]
                num4 = list_numplayers[1]
                odd = (51-(2+ num3+num4))*(51-(2+ num3+2*num4))/((52-(2+ num3+num4))*(52-(2+ num3+2*num4)))
        elif street == "6th":
                odd = 0
        elif street == "RIVER": 
                odd = 0
    return odd
def odd_fourth_card(card,occur,street,list_numplayers):
    odd = 0
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
                num3 = list_numplayers[0]
                odd = ((51-(2+num3))*(51-(2+ 2*num3))*(51-(2+ 3*num3)))/((52-(2+ num3))*(52-(2+ 2*num3))*(52-(2+ 3*num3))*(52-(2+ 4*num3)))
        elif street == "5th":
                odd = 0
        elif street == "6th":
                odd = 0
        elif street == "RIVER": 
                odd = 0
    return odd
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
            odd = odd_first_card(card,occur,street,list_numplayers)+odd_second_card(card,occur,street,list_numplayers)+odd_third_card(card,occur,street,list_numplayers)+odd_fourth_card(card,occur,street,list_numplayers)
        elif street == "5th":
            odd = odd_first_card(card,occur,street,list_numplayers)+odd_second_card(card,occur,street,list_numplayers)+odd_third_card(card,occur,street,list_numplayers)   
        elif street == "6th":
            odd = odd_first_card(card,occur,street,list_numplayers)+odd_second_card(card,occur,street,list_numplayers) 
        elif street == "RIVER": 
            odd = odd_first_card(card,occur,street,list_numplayers) 
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
    if street == "4th":
        if remaining > 4 : 
            return 0
    elif street == "5th":
        if remaining > 3 : 
            return 0
    elif street == "6th":
        if remaining > 2 : 
            return 0
    else:
        if remaining > 1 : 
            return 0
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
        if odd > len(poss):
            return 1.
    return odd/len(poss)

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

list_function=[odd_first_card,odd_second_card,odd_third_card,odd_fourth_card]
def Pair(occur, column, street, list_numplayers):
    num = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
    suit = ['s','h','d','c']
    odd = 0.
    hand = 0
    remaining = []
    other = 0
    count = 0
    for i in range(len(occur)-3):
        if occur[i][column] == 0 or occur[i][column] == 1:
            if occur[i][column] == 1:
                hand +=1
            else:
                remaining.append(num[column] + suit[i])
        else:
            other +=1
    if hand >= 2:
        return 1.
    elif other > 2:
        return 0.
    else:
        if street != "SUMMARY" or street != "SHOW":
            if hand == 0:
                for i in range (0,len(remaining)-1):
                    card1 = remaining[i]
                    for j in range (i+1,len(remaining)):
                        card2 = remaining[j]
                        for k in range (0,len(list_function)-1):
                            odd1 = list_function[k](card1,occur,street,list_numplayers)
                            odd2 = list_function[k](card2,occur,street,list_numplayers)
                            for l in range (k+1,len(list_function)):
                                count+=2
                                odd3 = list_function[l](card2,occur,street,list_numplayers)
                                odd4 = list_function[l](card1,occur,street,list_numplayers)
                                odd += (odd1*odd3+
                                        odd2*odd4)
            elif hand == 1 : 
                for i in range (0,len(remaining)):
                    card1 = remaining[i]
                    for k in range (0,len(list_function)):
                        count+=1
                        odd += list_function[k](card1,occur,street,list_numplayers)                    
                
            odd = odd/(count)
            if odd > 1:
                odd = 1
        else:
            odd = 0
    return round(odd,4)

def Three_Kind(occur,column,street,list_numplayers):
    num = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
    suit = ['s','h','d','c']
    odd = 0.
    hand = 0
    remaining = []
    other = 0
    count = 0
    for i in range(len(occur)-3):
        if occur[i][column] == 0 or occur[i][column] == 1:
            if occur[i][column] == 1:
                hand +=1
                
            else:
                remaining.append(num[column] + suit[i])
        else:
            other +=1
    if hand >= 3:
        return 1.
    elif other > 1:
        return 0.
    
    else:
        print(hand,num[column])
        if street != "SUMMARY" or street != "SHOW":
            if hand == 0:
                for i in range (0,len(remaining)-2):
                    card1 = remaining[i]
                    for j in range (i+1,len(remaining)-1):
                        card2 = remaining[j]
                        for k in range (j+1,len(remaining)):
                            card3 = remaining[k]
                            for l in range (0,len(list_function)-2):
                                odd1 = list_function[l](card1,occur,street,list_numplayers)
                                odd2 = list_function[l](card2,occur,street,list_numplayers)
                                odd3 = list_function[l](card3,occur,street,list_numplayers)
                                for m in range (l+1,len(list_function)-1):
                                    odd4 = list_function[m](card1,occur,street,list_numplayers)
                                    odd5 = list_function[m](card2,occur,street,list_numplayers)
                                    odd6 = list_function[m](card3,occur,street,list_numplayers)
                                    for n in range (m+1,len(list_function)):
                                        count +=6
                                        odd7 = list_function[n](card1,occur,street,list_numplayers)
                                        odd8 = list_function[n](card2,occur,street,list_numplayers)
                                        odd9 = list_function[n](card3,occur,street,list_numplayers)
                                        odd += (odd1*odd5*odd9+
                                                odd1*odd6*odd8+
                                                odd2*odd4*odd9+
                                                odd2*odd6*odd7+
                                                odd3*odd4*odd8+
                                                odd3*odd5*odd7)
            elif hand == 1:
                for i in range (0,len(remaining)-1):
                    card1 = remaining[i]
                    for j in range (i+1,len(remaining)):
                        card2 = remaining[j]
                        for l in range (0,len(list_function)-1):
                            odd1 = list_function[l](card1,occur,street,list_numplayers)
                            odd2 = list_function[l](card2,occur,street,list_numplayers)
                            for n in range (l+1,len(list_function)):
                                count +=2
                                odd3 = list_function[n](card1,occur,street,list_numplayers)
                                odd4 = list_function[n](card2,occur,street,list_numplayers)
                                odd += (odd1*odd4+
                                        odd2*odd3)
            elif hand == 2:
                for i in range (0,len(remaining)):
                    card1 = remaining[i]
                    for l in range (0,len(list_function)):
                        count +=1
                        odd += list_function[l](card1,occur,street,list_numplayers)
            odd /=count
            if odd > 1:
                odd = 1
        else:
            odd = 0
    return round(odd,6)
def Four_Kind(occur,column,street,list_numplayers):
    num = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
    suit = ['s','h','d','c']
    odd = 0.
    hand = 0
    remaining = []
    other = 0
    count = 0
    for i in range(0,4):
        if occur[i][column] == 0 or occur[i][column] == 1:
            if occur[i][column] == 1:
                hand +=1
                
            else:
                remaining.append(num[column] + suit[i])
        else:
            other +=1
    if hand == 4:
        return 1.
    elif other > 0:
        return 0.
    else:
        if street != "SUMMARY" or street != "SHOW":
            if hand == 0:
                for i in range (0,len(remaining)-3):
                    card1 = remaining[i]
                    for j in range (i+1,len(remaining)-2):
                        card2 = remaining[j]
                        for k in range (j+1,len(remaining)-1):
                            card3 = remaining[k]
                            for l in range (k+1,len(remaining)):
                                card4 = remaining[l]
                                for m in range (len(list_function)-3):
                                    odd1 = list_function[m](card1,occur,street,list_numplayers)
                                    odd2 = list_function[m](card2,occur,street,list_numplayers)
                                    odd3 = list_function[m](card3,occur,street,list_numplayers)
                                    odd4 = list_function[m](card4,occur,street,list_numplayers)
                                    for n in range (m+1,len(list_function)-2):
                                        odd5 = list_function[n](card1,occur,street,list_numplayers)
                                        odd6 = list_function[n](card2,occur,street,list_numplayers)
                                        odd7 = list_function[n](card3,occur,street,list_numplayers)
                                        odd8 = list_function[n](card4,occur,street,list_numplayers)
                                        for o in range (n+1,len(list_function)-1):
                                            odd9 = list_function[o](card1,occur,street,list_numplayers)
                                            odd10 = list_function[o](card2,occur,street,list_numplayers)
                                            odd11 = list_function[o](card3,occur,street,list_numplayers)
                                            odd12 = list_function[o](card4,occur,street,list_numplayers)
                                            for p in range (o+1,len(list_function)):
                                                count +=24
                                                odd13 = list_function[p](card1,occur,street,list_numplayers)
                                                odd14 = list_function[p](card2,occur,street,list_numplayers)
                                                odd15 = list_function[p](card3,occur,street,list_numplayers)
                                                odd16 = list_function[p](card4,occur,street,list_numplayers)
                                                odd += (odd1*odd6*odd11*odd16+
                                                        odd1*odd6*odd12*odd15+
                                                        odd1*odd7*odd10*odd16+
                                                        odd1*odd7*odd12*odd14+    
                                                        odd1*odd8*odd10*odd15+
                                                        odd1*odd8*odd11*odd14+
                                                        odd2*odd5*odd11*odd16+
                                                        odd2*odd5*odd12*odd15+
                                                        odd2*odd7*odd9*odd16+
                                                        odd2*odd7*odd12*odd13+
                                                        odd2*odd8*odd9*odd15+
                                                        odd2*odd8*odd11*odd13+
                                                        odd3*odd5*odd10*odd16+
                                                        odd3*odd5*odd12*odd14+
                                                        odd3*odd6*odd9*odd16+
                                                        odd3*odd6*odd12*odd13+
                                                        odd3*odd8*odd9*odd14+
                                                        odd3*odd8*odd10*odd13+
                                                        odd4*odd5*odd10*odd15+
                                                        odd4*odd5*odd11*odd14+
                                                        odd4*odd6*odd9*odd15+
                                                        odd4*odd6*odd11*odd13+
                                                        odd4*odd7*odd9*odd14+
                                                        odd4*odd7*odd10*odd13)
            elif hand == 1:
                for i in range (0,len(remaining)-2):
                    card1 = remaining[i]
                    for j in range (i+1,len(remaining)-1):
                        card2 = remaining[j]
                        for k in range (j+1,len(remaining)):
                            card3 = remaining[k]
                            for m in range (0,len(list_function)-2):
                                odd1 = list_function[m](card1,occur,street,list_numplayers)
                                odd2 = list_function[m](card2,occur,street,list_numplayers)
                                odd3 = list_function[m](card3,occur,street,list_numplayers)
                                for n in range (m+1,len(list_function)-1):
                                    odd5 = list_function[n](card1,occur,street,list_numplayers)
                                    odd6 = list_function[n](card2,occur,street,list_numplayers)
                                    odd7 = list_function[n](card3,occur,street,list_numplayers)
                                    for o in range (n+1,len(list_function)):
                                        count+=6
                                        odd9 = list_function[o](card1,occur,street,list_numplayers)
                                        odd10 = list_function[o](card2,occur,street,list_numplayers)
                                        odd11 = list_function[o](card3,occur,street,list_numplayers)
                                        odd += (odd1*odd6*odd11+
                                                odd1*odd7*odd10+
                                                odd2*odd5*odd11+
                                                odd2*odd7*odd9+
                                                odd3*odd5*odd10+
                                                odd3*odd6*odd9)                
            elif hand == 2:
                for i in range (0,len(remaining)-1):
                    card1 = remaining[i]
                    for j in range (i+1,len(remaining)):
                        card2 = remaining[j]
                        for m in range (0,len(list_function)-1):
                            odd1 = list_function[m](card1,occur,street,list_numplayers)
                            odd2 = list_function[m](card2,occur,street,list_numplayers)
                            for n in range (m+1,len(list_function)):
                                count+=2
                                odd5 = list_function[n](card1,occur,street,list_numplayers)
                                odd6 = list_function[n](card2,occur,street,list_numplayers)
                                odd += (odd1*odd6 + odd2*odd5)
            elif hand ==3:
                for i in range (0,len(remaining)):
                    card1 = remaining[i]
                    for m in range (0,len(list_function)):
                        count+=1
                        odd += list_function[m](card1,occur,street,list_numplayers)   
            odd/=count
            if odd > 1:
                odd =1
        else:
            odd = 0
    return round(odd,6)

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