from numpy import zeros

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
                odd = 1/(52-(2 + num3))
        elif street == "5th":
                num3 = list_numplayers[0]
                num4 = list_numplayers[1]
                odd = 1/(52-(2 + num3+num4))
        elif street == "6th":
                num3 = list_numplayers[0]
                num4 = list_numplayers[1]
                num5 = list_numplayers[2]
                odd = 1/(52-(2 + num3+num4+num5))
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
                odd = (51-(2+ num3+num4))*(51-(2+ num3+2*num4))/((52-(2+ num3+num4))*(52-(2+ num3+2*num4))*(52-(2+ num3+3*num4)))
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
    nums = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
    suits = ['s','h','d','c']
    odd = 0.
    hand = 0
    remaining = []
    other = 0
    for card in straight:
        j = nums.index(card[0])
        i = suits.index(card[1])
        if occur[i][j] == 1:
            hand += 1
        elif occur[i][j] == 0:
            remaining.append(card)
        else:
            other +=1
    if hand == 5:
        return 1.
    elif other>0:
        return 0.
    else:
        if  street != "SUMMARY" or street != "SHOW":
            if hand == 0:
                 odd = 0.
            elif hand == 1:
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
            elif hand == 2:
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
                                        
                                        odd9 = list_function[o](card1,occur,street,list_numplayers)
                                        odd10 = list_function[o](card2,occur,street,list_numplayers)
                                        odd11 = list_function[o](card3,occur,street,list_numplayers)
                                        odd += (odd1*odd6*odd11+
                                                odd1*odd7*odd10+
                                                odd2*odd5*odd11+
                                                odd2*odd7*odd9+
                                                odd3*odd5*odd10+
                                                odd3*odd6*odd9) 
            elif hand == 3:
                for i in range (0,len(remaining)-1):
                    card1 = remaining[i]
                    for j in range (i+1,len(remaining)):
                        card2 = remaining[j]
                        for m in range (0,len(list_function)-1):
                            odd1 = list_function[m](card1,occur,street,list_numplayers)
                            odd2 = list_function[m](card2,occur,street,list_numplayers)
                            for n in range (m+1,len(list_function)):
                                
                                odd5 = list_function[n](card1,occur,street,list_numplayers)
                                odd6 = list_function[n](card2,occur,street,list_numplayers)
                                odd += (odd1*odd6 + odd2*odd5)
            elif hand == 4:
                for i in range (0,len(remaining)):
                    card1 = remaining[i]
                    for m in range (0,len(list_function)):
                        
                        odd += list_function[m](card1,occur,street,list_numplayers)
        else:
            odd = 0
    return odd
def count_card(j,occur):
    S = 0
    for i in range (4):
        if occur[i][j] == 0:
            S+=1
    return S
low_hand = [['5','4','3','2','A'],
            ['6','4','3','2','A'],
            ['6','5','4','3','2'],
            ['7','5','4','3','2'],
            ['7','6','5','2','A'],
            ['7','6','5','4','2'],
            ['8','4','3','2','A'],
            ['8','6','4','2','A'],
            ['8','7','6','5','3'],
            ['8','7','6','5','4']]

def low_hand_odd(occur,street,list_numplayers):
    odd = 0.
    low_hand_odds = []
    for hand in low_hand :
        low_hand_odds.append([hand,round(odd_Straight(hand,occur,street,list_numplayers),3)])
    return low_hand_odds

def odd_Straight(straight,occur,street,list_numplayers):
    nums = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
    suits = ['s','h','d','c']
    odd = 0.
    hand = 0
    remaining = []
    count = []
    for k in range (len(straight)):
        pres = 0
        j = nums.index(straight[k])
        for i in range (0,4):
            if occur[i][j] == 1 and pres!=1:
                hand += 1
                pres = 1    
        for i in range (0,4):
            if occur[i][j] == 0 and pres !=1:
                remaining.append(nums[j] + suits[i])
                count.append(count_card(j,occur))
                pres = 1
            
    if hand >= 5:
        return 1.
    elif len(remaining)>=5:
        return 0.
    else:
        if  street != "SUMMARY" or street != "SHOW":
            if hand == 0:
                 odd = 0.
            elif hand == 1:
                for i in range (0,len(remaining)-3):
                    card1 = remaining[i]
                    for j in range (i+1,len(remaining)-2):
                        card2 = remaining[j]
                        for k in range (j+1,len(remaining)-1):
                            card3 = remaining[k]
                            for l in range (k+1,len(remaining)):
                                card4 = remaining[l]
                                for m in range (len(list_function)-3):
                                    odd1 = count[0]*list_function[m](card1,occur,street,list_numplayers)
                                    odd2 = count[1]*list_function[m](card2,occur,street,list_numplayers)
                                    odd3 = count[2]*list_function[m](card3,occur,street,list_numplayers)
                                    odd4 = count[3]*list_function[m](card4,occur,street,list_numplayers)
                                    for n in range (m+1,len(list_function)-2):
                                        odd5 = count[0]*list_function[n](card1,occur,street,list_numplayers)
                                        odd6 = count[1]*list_function[n](card2,occur,street,list_numplayers)
                                        odd7 = count[2]*list_function[n](card3,occur,street,list_numplayers)
                                        odd8 = count[3]*list_function[n](card4,occur,street,list_numplayers)
                                        for o in range (n+1,len(list_function)-1):
                                            odd9 = count[0]*list_function[o](card1,occur,street,list_numplayers)
                                            odd10 = count[1]*list_function[o](card2,occur,street,list_numplayers)
                                            odd11 = count[2]*list_function[o](card3,occur,street,list_numplayers)
                                            odd12 = count[3]*list_function[o](card4,occur,street,list_numplayers)
                                            for p in range (o+1,len(list_function)):
                                                odd13 = count[0]*list_function[p](card1,occur,street,list_numplayers)
                                                odd14 = count[1]*list_function[p](card2,occur,street,list_numplayers)
                                                odd15 = count[2]*list_function[p](card3,occur,street,list_numplayers)
                                                odd16 = count[3]*list_function[p](card4,occur,street,list_numplayers)
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
            elif hand == 2:
               for i in range (0,len(remaining)-2):
                    card1 = remaining[i]
                    for j in range (i+1,len(remaining)-1):
                        card2 = remaining[j]
                        for k in range (j+1,len(remaining)):
                            card3 = remaining[k]
                            for m in range (0,len(list_function)-2):
                                odd1 = count[0]*list_function[m](card1,occur,street,list_numplayers)
                                odd2 = count[1]*list_function[m](card2,occur,street,list_numplayers)
                                odd3 = count[2]*list_function[m](card3,occur,street,list_numplayers)
                                for n in range (m+1,len(list_function)-1):
                                    odd5 = count[0]*list_function[n](card1,occur,street,list_numplayers)
                                    odd6 = count[1]*list_function[n](card2,occur,street,list_numplayers)
                                    odd7 = count[2]*list_function[n](card3,occur,street,list_numplayers)
                                    for o in range (n+1,len(list_function)):
                                        odd9 = count[0]*list_function[o](card1,occur,street,list_numplayers)
                                        odd10 = count[1]*list_function[o](card2,occur,street,list_numplayers)
                                        odd11 = count[2]*list_function[o](card3,occur,street,list_numplayers)
                                        odd += (odd1*odd6*odd11+
                                                odd1*odd7*odd10+
                                                odd2*odd5*odd11+
                                                odd2*odd7*odd9+
                                                odd3*odd5*odd10+
                                                odd3*odd6*odd9) 
            elif hand == 3:
                for i in range (0,len(remaining)-1):
                    card1 = remaining[i]
                    for j in range (i+1,len(remaining)):
                        card2 = remaining[j]
                        for m in range (0,len(list_function)-1):
                            odd1 = count[0]*list_function[m](card1,occur,street,list_numplayers)
                            odd2 = count[1]*list_function[m](card2,occur,street,list_numplayers)
                            for n in range (m+1,len(list_function)):
                                odd5 = count[0]*list_function[n](card1,occur,street,list_numplayers)
                                odd6 = count[1]*list_function[n](card2,occur,street,list_numplayers)
                                odd += (odd1*odd6 + odd2*odd5)
            elif hand == 4:
                for i in range (0,len(remaining)):
                    card1 = remaining[i]
                    for m in range (0,len(list_function)):
                        odd += count[0]*list_function[m](card1,occur,street,list_numplayers)
        else:
            odd = 0
    return odd
def Straight(occur,street,list_numplayers):
    odd = 0.
    poss = list_Straight()
    for straight in poss :
        odd+=odd_Straight(straight,occur,street,list_numplayers)
        if odd_Straight(straight,occur,street,list_numplayers) == 1:
            return 1. 
    return odd
def Straight_flush(occur,street,list_numplayers,poss):
    odd = 0.
    for straight in poss :
        odd+=odd_Straight_flush(straight,occur,street,list_numplayers)
        if odd > len(poss):
            return 1.
    return odd/len(poss)

def Flush(occur, row, street, list_numplayers):
    num = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
    suit = ['s','h','d','c']
    odd = 0.
    hand = 0
    remaining = []
    other = 0
    count = 0
    for j in range(len(occur[0])-3):
        if occur[row][j] == 1:
            hand += 1
        elif occur[row][j] == 0:
            remaining.append(num[j] + suit[row])
        else:
            other +=1
    if hand >= 5:
        return 1.
    elif len(remaining) + hand < 5:
        return 0.
    else:
        if  street != "SUMMARY" or street != "SHOW":
            if hand == 0:
                 odd = 0.
            elif hand == 1:
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
            elif hand == 2:
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
            elif hand == 3:
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
            elif hand == 4:
                for i in range (0,len(remaining)):
                    card1 = remaining[i]
                    for m in range (0,len(list_function)):
                        count+=1
                        odd += list_function[m](card1,occur,street,list_numplayers)
        else:
            odd = 0
    return odd

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
        if occur[i][column] == 0 :
            remaining.append(num[column] + suit[i])
        elif occur[i][column] == 1:
            hand +=1            
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
                        odd1 = list_function[k](card1,occur,street,list_numplayers)
                        odd += list_function[k](card1,occur,street,list_numplayers)
        else:
            odd = 0
    return odd

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
        else:
            odd = 0
    return odd
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
        else:
            odd = 0
    return odd

def Table():
    num = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
    suit = ['s','h','d','c']
    occur = zeros((len(suit)+3,len(num)+3))
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
    occur1 = zeros((len(occur),len(occur[0])))
    low_hand_odds = []
    for i in range (len(occur)):
        for j in range(len(occur[1])):
            occur1[i][j] = occur[i][j]
    staight_odds = round(Straight(occur,street,list_numplayers),2)
    low_hand_odds = low_hand_odd(occur,street,list_numplayers)
    for i in range (len(occur)-3):
        poss = list_Straight_flush(i)
        occur1[i][13] = staight_odds
        occur1[i][14] = round(Flush(occur, i, street, list_numplayers),2)
        occur1[i][15] = round(Straight_flush(occur,street,list_numplayers,poss),2)
    for j in range (len(occur[0])-3):
        occur1[4][j] = round(Pair(occur,j,street,list_numplayers),2)
        occur1[5][j] = round(Three_Kind(occur,j,street,list_numplayers),2)
        occur1[6][j] = round(Four_Kind(occur,j,street,list_numplayers),2)
    return (occur1,low_hand_odds)