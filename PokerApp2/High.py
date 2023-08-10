from Odds import *
import itertools

def count_occurrences(lst):
    occurrences = {}
    for element in lst:
        
        element_tuple = tuple(element)
        
        occurrences[element_tuple] = occurrences.get(element_tuple, 0) + 1

    liste_occurrences = [[list(element), count] for element, count in occurrences.items()]
    return liste_occurrences

def Union(lst_to_union):
    new_list = []
    for lst in lst_to_union:
        new_list += lst
    return list(set(new_list))

def intersection(Hands):
    intersection = [Hands]
    intersection_i = []
    intersection_hand = []
    i = 2
    while i  < len(Hands):
    
        intersection_i = []
        intersection_hand = []
        intersection_hand = list(itertools.combinations(Hands, i))
        for hand in intersection_hand:
            intersection_i.append(Union(hand))
        intersection_i = count_occurrences(intersection_i)
        intersection.append(intersection_i)
        i+=1
    return intersection
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
def odd_two_pairs(occur):
    num = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
    shape = ['s','h','d','c']
    odd=0
    odd_max = 0
    best_hand = []
    index_pair1 = -1
    index_pair2 = -1
    count1 = 0
    count2= 0
    l = 0
    for j in range (len(occur[0])-4):
        for k in range (len(occur[0])-3):
            odd_two_pairs = occur[4][k]*occur[4][j]
            odd+= odd_two_pairs
            if odd_two_pairs >  odd_max:
                odd_max = odd_two_pairs
                index_pair1 = j
                index_pair2 = k
    if index_pair1 != -1:
        for i in range (len(occur)-3):
            if occur[i][index_pair1] == 1:
                best_hand.append(num[index_pair1] + shape[i])
                count1+= 1
            if occur[i][index_pair2] == 1:
                best_hand.append(num[index_pair2] + shape[i])
                count2+= 1
        while count1 !=2 and l < 4:
            if occur[l][index_pair1] == 0:
                best_hand.append(num[index_pair1] + shape[i])
                count1+= 1
            l+=1
        l =0
        while count2 !=2:
            if occur[l][index_pair2] == 0:
                best_hand.append(num[index_pair2] + shape[i])
                count2+= 1
    return(odd,best_hand,odd_max)
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


def Flush(occur, row, street, list_numplayers):
    num = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
    suit = ['s','h','d','c']
    odd = 0.
    hand = 0
    other=0
    remaining = []
    
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
                                                
                                                odd13 = list_function[p](card1,occur,street,list_numplayers)
                                                odd14 = list_function[p](card2,occur,street,list_numplayers)
                                                odd15 = list_function[p](card3,occur,street,list_numplayers)
                                                odd16 = list_function[p](card4,occur,street,list_numplayers)
                                                odd_4 = (odd1*odd6*odd11*odd16+
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
                                                odd+= odd_4
                                                    

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
                                        odd_3 = (odd1*odd6*odd11+
                                                odd1*odd7*odd10+
                                                odd2*odd5*odd11+
                                                odd2*odd7*odd9+
                                                odd3*odd5*odd10+
                                                odd3*odd6*odd9)
                                        odd+=odd_3
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
                                odd_2 = (odd1*odd6 + odd2*odd5)
                                odd+=odd_2
            elif hand == 4:
                for i in range (0,len(remaining)):
                    card1 = remaining[i]
                    for m in range (0,len(list_function)):
                        
                        odd += list_function[m](card1,occur,street,list_numplayers)
                        odd_1 = (odd1*odd6 + odd2*odd5)
                        odd+=odd_1
        else:
            odd = 0
    return odd
def odd_full_house(occur):
    num_cards = ['A','2','3','4','5','6','7','8','9','T','J','C','Q','K']
    shape_card = ['s','h','d','c']
    odd = 0
    column = -1
    column1 = -1
    best_hand = []
    odd_max=0.
    for j in range(0,13):
        if occur[5][j] == 1:
            column = j
        elif occur[4][j] == 1 and occur[5][j] != 1:
            column1 = j
    for j in range(0,13):
        if occur[4][j] == 1 and j != column and column != -1:
            best_hand =[]
            for i in range (4):
                if occur[i][j] == 1 :
                    best_hand.append(num_cards.index(j) + shape_card.index(i))
                if occur[i][column] == 1 :
                    best_hand.append(num_cards.index(column) + shape_card.index(i))
            return  (1,1,best_hand)
        elif j != column and column != -1:
            odd += occur[4][j]
            if occur[4][j] > odd_max:
                odd_max = occur[4][j]
                best_hand = []
                count = 0
                for i in range (4):
                    if occur[i][j] == 1 :
                        count += 1
                for i in range (4):
                    if occur[i][j] == 1 :
                        best_hand.append(num_cards.index(j) + shape_card.index(i))
                    elif count == 1 and occur[i][j] == 0:
                        best_hand.append(num_cards.index(j) + shape_card.index(i))
                        count+=1
                    elif count == 0 and occur[i][j] == 0:
                        best_hand.append(num_cards.index(j) + shape_card.index(i))
                        count+=1
                    if occur[i][column] == 1 :
                        best_hand.append(num_cards.index(column) + shape_card.index(i))
        if occur[5][j] == 1 and j != column1 and column1 != -1:
            best_hand =[]

            for i in range (4):
                if occur[i][j] == 1 :
                    best_hand.append(num_cards.index(j) + shape_card.index(i))
                if occur[i][column1] == 1 :
                    best_hand.append(num_cards.index(column1) + shape_card.index(i))
            return  (1,1,best_hand)
        elif j != column1 and column1 != -1:
            odd += occur[5][j]
            if occur[5][j] > odd_max:
                odd_max = occur[5][j]
                best_hand = []
                count = 0
            for i in range (4):
                if occur[i][j] == 1 :
                    count += 1
            for i in range (4):
                if occur[i][j] == 1 :
                    best_hand.append(num_cards.index(j) + shape_card.index(i))
                elif count == 2 and occur[i][j] == 0:
                    best_hand.append(num_cards.index(j) + shape_card.index(i))
                    count+=1
                elif count == 1 and occur[i][j] == 0:
                    best_hand.append(num_cards.index(j) + shape_card.index(i))
                    count+=1
                elif count == 0 and occur[i][j] == 0:
                    best_hand.append(num_cards.index(j) + shape_card.index(i))
                    count+=1
                if occur[i][column1] == 1 :
                    best_hand.append(num_cards.index(column1) + shape_card.index(i))        
    return (odd,odd_max,best_hand)

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

def list_Straight_flush(row):
    num = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
    suits = ['s','h','d','c']
    suit = suits[row]
    poss = []
    for i in range (9):
        poss.append([num[i] +suit,num[i+1]+suit,num[i+2]+suit,num[i+3]+suit,num[i+4]+suit])
    poss.append(['T'+suit,'J'+suit,'Q'+suit,'K'+suit,'A'+suit])
    return poss
def Royal_flush(occur,street,list_numplayers):
    odd = 0
    suits = ['s','h','d','c']
    for s in suits:
        odd+=odd_Straight_flush(['T'+s,'J'+s,'Q'+s,'K'+s,'A'+s],occur,street,list_numplayers)
    return odd
def list_Straight():
    num = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
    poss = []
    for i in range (9):
        poss.append([num[i] ,num[i+1],num[i+2],num[i+3],num[i+4]])
    poss.append(['T','J','Q','K','A'])
    
    return poss

all_straight_flush_0 = intersection(list_Straight_flush(0))
all_straight_flush_1 = intersection(list_Straight_flush(1))
all_straight_flush_2 = intersection(list_Straight_flush(2))
all_straight_flush_3 = intersection(list_Straight_flush(3))
all_straight = intersection(list_Straight())


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


lst_straight_flush = [['A','2','3','4','5'],
                ['2','3','4','5','6'],
                ['3','4','5','6','7'],
                ['4','5','6','7','8'],
                ['5','6','7','8','9'],
                ['6','7','8','9','T'],
                ['7','8','9','T','J'],
                ['8','9','T','J','Q'],
                ['9','T','J','Q','K'],
                ['T','J','Q','K','A']]
def possible_hand_straight_flush(hand,row,occur,street):
    nums = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
    avoid_cards = []
    if nums.index(hand[0]) >=1 and nums.index(hand[4]) < 12:
        avoid_cards.append(nums[nums.index(hand[0]) - 1])
        avoid_cards.append(nums[nums.index(hand[4]) + 1])
    elif nums.index(hand[0]) == 0:
        avoid_cards.append(nums[nums.index(hand[4]) + 1])
    elif nums.index(hand[4]) == 0:
        avoid_cards.append(nums[nums.index(hand[0]) - 1])
    required_card = 5
    for card in hand:
        k = nums.index(card)
        if occur[row][k] == 1:
            required_card -= 1
    for card in avoid_cards:
        k = nums.index(card)
        if occur[row][k] == 1:
            if required_card != 0:
                return (False,5)
            else:
                return (False,-1)
    if street == "4th" and required_card > 4:
        possible = False
    elif street == "5th" and required_card > 3:
        possible = False
    elif street == "6th" and required_card > 2:
        possible = False
    elif street == "RIVER" and required_card > 1:
         possible = False
    elif (street == "SHOW" or street == "SUMMARY" ) and required_card == 0:
        possible = True
    elif street == "SHOW" or street == "SUMMARY" :
        possible = False
    else:
        return (True,required_card)
    return (possible,required_card)
def Avoid_straight_flush(hand,occur):
    nums = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
    avoid_cards = []
    if nums.index(hand[0]) >=1 and nums.index(hand[4]) < 12:
        avoid_cards.append(nums[nums.index(hand[0]) - 1])
        avoid_cards.append(nums[nums.index(hand[4]) + 1])
    elif nums.index(hand[0]) == 0:
        avoid_cards.append(nums[nums.index(hand[4]) + 1])
    elif nums.index(hand[4]) == 0:
        avoid_cards.append(nums[nums.index(hand[0]) - 1])
    remaining_cards = []
    remaining_cards_with_occurence= []
    for card in nums:
        if not(card in avoid_cards):
            remaining_cards.append(card)
    for card in remaining_cards:
        remaining_cards_with_occurence.append([card,count_cards([card],occur)])
    return (count_cards(avoid_cards,occur),remaining_cards_with_occurence)
def straight_flush_probability(hand,row,occur,street,list_numplayers):
    (possible,required_card)  = possible_hand_straight_flush(hand,row,occur,street)
    permutations = 0
    spare = 0
    probability = 0
    (avoid,remaining_cards_with_occur) =Avoid_straight_flush(hand,occur)
    if required_card == 0 :
        return 1
    if street == "4th" and possible:
        spare = 4 - required_card
        num3 = list_numplayers[0]
        permutations = ((52-(2 + num3)))*((51-(2 + num3)))*((50-(2 + num3)))*((49-(2 + num3)))
        probability = factorial(4)*Spare(spare,avoid, count_remaining_cards(occur),remaining_cards_with_occur)*Required(hand,occur)/permutations
    elif street == "5th" and possible:
        spare = 3 - required_card
        num3 = list_numplayers[0]
        num4 = list_numplayers[1]
        permutations = ((52-(2 + num3+num4)))*((51-(2 + num3+num4)))*((50-(2 + num3+num4)))
        probability = factorial(3)*Spare(spare,avoid, count_remaining_cards(occur),remaining_cards_with_occur)*Required(hand,occur)/permutations
    elif street == "6th" and possible:
        spare = 2 - required_card
        num3 = list_numplayers[0]
        num4 = list_numplayers[1]
        num5 = list_numplayers[2]
        permutations = ((52-(2 + num3+num4+num5)))*((51-(2 + num3+num4+num5)))
        probability = factorial(2)*Spare(spare,avoid, count_remaining_cards(occur),remaining_cards_with_occur)*Required(hand,occur)/permutations
    elif street == "RIVER" and possible: 
        spare = 1 - required_card
        num3 = list_numplayers[0]
        num4 = list_numplayers[1]
        num5 = list_numplayers[2]
        num6 = list_numplayers[3]
        permutations = (52-(2+ num3+num4+num5+num6))
        probability = factorial(1)*Spare(spare,avoid,count_remaining_cards(occur),remaining_cards_with_occur)*Required(hand,occur)/permutations
    else:
        if possible:
            probability = 1
        else:
            return 0
    
    return probability 
def generate_all_four():
    nums = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
    lst_full = []
    hand=[]
    for i in range (13):
        hand = []
        hand.append(nums[i])
        hand.append(nums[i])
        
        hand.append(nums[i])
        hand.append(nums[i])
        lst_full.append(hand)
    return lst_full
lst_four = generate_all_four()
def Required_four(hand,occur):
    pro_cards = 1
    number_card=1
    have  = False
    nums = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
    remaining_four = 0
    count_four = 0
    index_four = nums.index(hand[0])
    for i in range (4):
        if occur[i][index_four] == 0: 
            remaining_four +=1
        elif occur[i][index_four] == 1: 
            count_four +=1
    if count_four == 0:
        pro_cards *= remaining_four*(remaining_four-1)*(remaining_four-2)*(remaining_four-3)
    elif count_four == 1:
        pro_cards *= remaining_four*(remaining_four-1)*(remaining_four-2)
    elif count_four == 2:
        pro_cards *= remaining_four*(remaining_four-1)
    elif count_four == 3:
        pro_cards *= remaining_four
    return pro_cards
def possible_hand_four(hand,occur,street):
    nums = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
    count_four = 0
    required_card = 4
    index_four = nums.index(hand[0])
    for i in range (4):
        if occur[i][index_four] == 1:
            count_four +=1
    else:
        required_card-= ( count_four)

    if street == "4th" and required_card > 4:
        possible = False
    elif street == "5th" and required_card > 3:
        possible = False
    elif street == "6th" and required_card > 2:
        possible = False
    elif street == "RIVER" and required_card > 1:
         possible = False
    elif (street == "SHOW" or street == "SUMMARY" ) and required_card == 0:
        possible = True
    elif street == "SHOW" or street == "SUMMARY" :
        possible = False
    else:
        return (True,required_card)
    return (possible,required_card)
def Avoid_four(hand,occur):
    nums = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
    avoid_cards = []
    remaining_cards = []
    remaining_cards_with_occurence= []
    for card in nums:
        if not(card in avoid_cards):
            remaining_cards.append(card)
    for card in remaining_cards:
        remaining_cards_with_occurence.append([card,count_cards([card],occur)])
    return (count_cards(avoid_cards,occur),remaining_cards_with_occurence)

def Four_probability(hand,occur,street,list_numplayers):
    (possible,required_card)  = possible_hand_four(hand,occur,street)

    permutations = 0
    spare = 0
    probability = 0
    (avoid,remaining_cards_with_occur) =Avoid_four(hand,occur)
    if required_card == 0 :
        return 1
    elif street == "4th" and possible:
        spare = 4 - required_card
        num3 = list_numplayers[0]
        permutations = ((52-(2 + num3)))*((51-(2 + num3)))*((50-(2 + num3)))*((49-(2 + num3)))
        probability = factorial(4)*Spare(spare,avoid, count_remaining_cards(occur),remaining_cards_with_occur)*Required_four(hand,occur)/permutations
    elif street == "5th" and possible:
        spare = 3 - required_card
        num3 = list_numplayers[0]
        num4 = list_numplayers[1]
        permutations = ((52-(2 + num3+num4)))*((51-(2 + num3+num4)))*((50-(2 + num3+num4)))
        probability = factorial(3)*Spare(spare,avoid, count_remaining_cards(occur),remaining_cards_with_occur)*Required_four(hand,occur)/permutations
    elif street == "6th" and possible:
        spare = 2 - required_card
        num3 = list_numplayers[0]
        num4 = list_numplayers[1]
        num5 = list_numplayers[2]
        permutations = ((52-(2 + num3+num4+num5)))*((51-(2 + num3+num4+num5)))
        probability = factorial(2)*Spare(spare,avoid, count_remaining_cards(occur),remaining_cards_with_occur)*Required_four(hand,occur)/permutations
    elif street == "RIVER" and possible: 
        spare = 1 - required_card
        num3 = list_numplayers[0]
        num4 = list_numplayers[1]
        num5 = list_numplayers[2]
        num6 = list_numplayers[3]
        permutations = (52-(2+ num3+num4+num5+num6))
        probability = factorial(1)*Spare(spare,avoid,count_remaining_cards(occur),remaining_cards_with_occur)*Required_four(hand,occur)/permutations
    else:
        if possible:
            probability = 1
        elif required_card == -1:
            return -1
        else:
            return 0
    return probability 
def generate_all_full():
    nums = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
    lst_full = []
    hand=[]
    for i in range (12):
        for j in range (i+1,13):
            hand = []
            hand.append(nums[i])
            hand.append(nums[i])
            hand.append(nums[j])
            hand.append(nums[j])
            hand.append(nums[j]) 
            lst_full.append(hand)
    return lst_full
lst_full = generate_all_full()
def Required_full(hand,occur):
    pro_cards = 1
    number_card=1
    have  = False
    nums = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
    remaining_pair = 0
    remaining_three = 0
    count_three = 0
    count_pair = 0
    index_pair = nums.index(hand[0])
    index_three = nums.index(hand[2])
    for i in range (4):
        if occur[i][index_pair] == 0: 
            remaining_pair +=1
        elif occur[i][index_pair] == 1: 
            count_pair +=1
        if occur[i][index_three] == 0:
            remaining_three +=1
        elif occur[i][index_three] == 1:
            count_three +=1
    if count_pair == 0:
        pro_cards *=remaining_pair*(remaining_pair-1)
    elif count_pair == 1:
        pro_cards *=remaining_pair
    if count_three == 0:
        pro_cards *= remaining_three*(remaining_three-1)*(remaining_three-2)
    elif count_three == 1:
        pro_cards *= remaining_three*(remaining_three-1)
    elif count_three == 2:
        pro_cards *= remaining_three
    return pro_cards
def possible_hand_full(hand,occur,street):
    nums = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
    count_pair = 0
    count_three = 0
    required_card = 5
    index_pair = nums.index(hand[0])
    index_three = nums.index(hand[2])
    for i in range (4):
        if occur[i][index_pair] == 1:
            count_pair +=1
        if occur[i][index_three] == 1:
            count_three +=1

    if count_three> 3 or count_pair > 2:
        possible = False
        required_card = 5
    else:
        required_card-= (count_three + count_pair)

    if street == "4th" and required_card > 4:
        possible = False
    elif street == "5th" and required_card > 3:
        possible = False
    elif street == "6th" and required_card > 2:
        possible = False
    elif street == "RIVER" and required_card > 1:
         possible = False
    elif (street == "SHOW" or street == "SUMMARY" ) and required_card == 0:
        possible = True
    elif street == "SHOW" or street == "SUMMARY" :
        possible = False
    else:
        return (True,required_card)
    return (possible,required_card)
def Avoid_full(hand,occur):
    nums = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
    avoid_cards = [hand[0],hand[2]]
    remaining_cards = []
    remaining_cards_with_occurence= []
    for card in nums:
        if not(card in avoid_cards):
            remaining_cards.append(card)
    for card in remaining_cards:
        remaining_cards_with_occurence.append([card,count_cards([card],occur)])
    return (count_cards(avoid_cards,occur),remaining_cards_with_occurence)

def full_probability(hand,occur,street,list_numplayers):
    (possible,required_card)  = possible_hand_full(hand,occur,street)
    permutations = 0
    spare = 0
    probability = 0
    (avoid,remaining_cards_with_occur) =Avoid_full(hand,occur)
    if required_card == 0 :
        return 1
    if street == "4th" and possible:
        spare = 4 - required_card
        num3 = list_numplayers[0]
        permutations = ((52-(2 + num3)))*((51-(2 + num3)))*((50-(2 + num3)))*((49-(2 + num3)))
        probability = factorial(4)*Spare(spare,avoid, count_remaining_cards(occur),remaining_cards_with_occur)*Required_full(hand,occur)/permutations
    elif street == "5th" and possible:
        spare = 3 - required_card
        num3 = list_numplayers[0]
        num4 = list_numplayers[1]
        permutations = ((52-(2 + num3+num4)))*((51-(2 + num3+num4)))*((50-(2 + num3+num4)))
        probability = factorial(3)*Spare(spare,avoid, count_remaining_cards(occur),remaining_cards_with_occur)*Required_full(hand,occur)/permutations
    elif street == "6th" and possible:
        spare = 2 - required_card
        num3 = list_numplayers[0]
        num4 = list_numplayers[1]
        num5 = list_numplayers[2]
        permutations = ((52-(2 + num3+num4+num5)))*((51-(2 + num3+num4+num5)))
        probability = factorial(2)*Spare(spare,avoid, count_remaining_cards(occur),remaining_cards_with_occur)*Required_full(hand,occur)/permutations
    elif street == "RIVER" and possible: 
        spare = 1 - required_card
        num3 = list_numplayers[0]
        num4 = list_numplayers[1]
        num5 = list_numplayers[2]
        num6 = list_numplayers[3]
        permutations = (52-(2+ num3+num4+num5+num6))
        probability = factorial(1)*Spare(spare,avoid,count_remaining_cards(occur),remaining_cards_with_occur)*Required_full(hand,occur)/permutations
    else:
        if possible:
            probability = 1
        elif required_card == -1:
            return -1
        else:
            return 0
    return probability 


def Required_flush(row,occur):
    pro_cards = 1
    number_card=1
    required_card = 5
    j = 0
    remaining = 0
    while  required_card!=0 and j < 13 :
        if occur[row][j] == 1:
            required_card -= 1
        j+=1
    for j in range (0,13):
        if occur[row][j] == 0:
            remaining+=1
    if required_card == 1:
        pro_cards *=remaining
    elif required_card == 2:
        pro_cards *=remaining*(remaining-1)
    elif required_card == 3:
        pro_cards *=remaining*(remaining-1)*(remaining-2)
    elif required_card == 4:
        pro_cards *=remaining*(remaining-1)*(remaining-2)*(remaining-3)
    
    return pro_cards

def possible_hand_flush(row,occur,street):
    required_card = 5

        
    j = 0
    while  required_card!=0 and j < 13 :
        if occur[row][j] == 1:
            required_card -= 1
        j+=1
    
    
    
    if street == "4th" and required_card > 4:
        possible = False
    elif street == "5th" and required_card > 3:
        possible = False
    elif street == "6th" and required_card > 2:
        possible = False
    elif street == "RIVER" and required_card > 1:
         possible = False
    elif (street == "SHOW" or street == "SUMMARY" ) and required_card == 0:
        possible = True
    elif street == "SHOW" or street == "SUMMARY" :
        possible = False
    else:
        return (True,required_card)
    return (possible,required_card)
def Avoid_flush(row,occur):
    nums = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
    avoid_cards = []
    avoid = 0
    remaining_cards = []
    remaining_cards_with_occurence= []
    for card in nums:
        if not(card in avoid_cards):
            remaining_cards.append(card)
    for card in remaining_cards:
        remaining_cards_with_occurence.append([card,count_cards([card],occur)])

    for j in range (13):
        if occur[row][j] != -1:
            avoid +=1
    avoid -= 5
    return (avoid,remaining_cards_with_occurence)
def flush_probability(occur,row,street,list_numplayers):
    (possible,required_card)  = possible_hand_flush(row,occur,street)
    
    permutations = 0
    spare = 0
    probability = 0
    (avoid,remaining_cards_with_occur) =Avoid_flush(row,occur)
    if required_card == 0:
        return 1
    elif street == "4th" and possible:
        spare = 4 - required_card
        num3 = list_numplayers[0]
        permutations = ((52-(2 + num3)))*((51-(2 + num3)))*((50-(2 + num3)))*((49-(2 + num3)))
        probability = factorial(4)*Spare(spare,avoid, count_remaining_cards(occur),remaining_cards_with_occur)*Required_flush(row,occur)/permutations
    elif street == "5th" and possible:
        spare = 3 - required_card
        num3 = list_numplayers[0]
        num4 = list_numplayers[1]
        permutations = ((52-(2 + num3+num4)))*((51-(2 + num3+num4)))*((50-(2 + num3+num4)))
        probability = factorial(3)*Spare(spare,avoid, count_remaining_cards(occur),remaining_cards_with_occur)*Required_flush(row,occur)/permutations
    elif street == "6th" and possible:
        spare = 2 - required_card
        num3 = list_numplayers[0]
        num4 = list_numplayers[1]
        num5 = list_numplayers[2]
        permutations = ((52-(2 + num3+num4+num5)))*((51-(2 + num3+num4+num5)))
        probability = factorial(2)*Spare(spare,avoid, count_remaining_cards(occur),remaining_cards_with_occur)*Required_flush(row,occur)/permutations
    elif street == "RIVER" and possible: 
        spare = 1 - required_card
        num3 = list_numplayers[0]
        num4 = list_numplayers[1]
        num5 = list_numplayers[2]
        num6 = list_numplayers[3]
        permutations = (52-(2+ num3+num4+num5+num6))
        probability = factorial(1)*Spare(spare,avoid,count_remaining_cards(occur),remaining_cards_with_occur)*Required_flush(row,occur)/permutations
    
    else:
        if possible:
            probability = 1
        else:
            return 0
    
    return probability



lst_straight = [['A','2','3','4','5'],
                ['2','3','4','5','6'],
                ['3','4','5','6','7'],
                ['4','5','6','7','8'],
                ['5','6','7','8','9'],
                ['6','7','8','9','T'],
                ['7','8','9','T','J'],
                ['8','9','T','J','Q'],
                ['9','T','J','Q','K'],
                ['T','J','Q','K','A']]
def possible_hand_straight(hand,occur,street):
    nums = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
    avoid_cards = []
    if nums.index(hand[0]) >=1 and nums.index(hand[4]) < 12:
        avoid_cards.append(nums[nums.index(hand[0]) - 1])
        avoid_cards.append(nums[nums.index(hand[4]) + 1])
    elif nums.index(hand[0]) == 0:
        avoid_cards.append(nums[nums.index(hand[4]) + 1])
    elif nums.index(hand[4]) == 0:
        avoid_cards.append(nums[nums.index(hand[0]) - 1])
    required_card = 5
    for card in hand:
        k = nums.index(card)
        i = 0
        while i < 4 and occur[i][k] != 1:
            i+=1
        if i !=4:
            required_card -= 1
    for card in avoid_cards:
        k = nums.index(card)
        for i in range (4):
            if occur[i][k] == 1:
                if required_card != 0:
                    return (False,5)
                else:
                    return (False,0)
    
    
    if street == "4th" and required_card > 4:
        possible = False
    elif street == "5th" and required_card > 3:
        possible = False
    elif street == "6th" and required_card > 2:
        possible = False
    elif street == "RIVER" and required_card > 1:
         possible = False
    elif (street == "SHOW" or street == "SUMMARY" ) and required_card == 0:
        possible = True
    elif street == "SHOW" or street == "SUMMARY" :
        possible = False
    else:
        return (True,required_card)
    return (possible,required_card)
def Avoid_straight(hand,occur):
    nums = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
    avoid_cards = []
    if nums.index(hand[0]) >=1 and nums.index(hand[4]) < 12:
        avoid_cards.append(nums[nums.index(hand[0]) - 1])
        avoid_cards.append(nums[nums.index(hand[4]) + 1])
    elif nums.index(hand[0]) == 0:
        avoid_cards.append(nums[nums.index(hand[4]) + 1])
    elif nums.index(hand[4]) == 0:
        avoid_cards.append(nums[nums.index(hand[0]) - 1])
    remaining_cards = []
    remaining_cards_with_occurence= []
    for card in nums:
        if not(card in avoid_cards):
            remaining_cards.append(card)
    for card in remaining_cards:
        remaining_cards_with_occurence.append([card,count_cards([card],occur)])
    return (count_cards(avoid_cards,occur),remaining_cards_with_occurence)
def straight_probability(hand,occur,street,list_numplayers):
    (possible,required_card)  = possible_hand_straight(hand,occur,street)
    
    permutations = 0
    spare = 0
    probability = 0
    (avoid,remaining_cards_with_occur) =Avoid_straight(hand,occur)
    if required_card == -1 or required_card == 0:
        return 1
    elif street == "4th" and possible:
        spare = 4 - required_card
        num3 = list_numplayers[0]
        permutations = ((52-(2 + num3)))*((51-(2 + num3)))*((50-(2 + num3)))*((49-(2 + num3)))
        probability = factorial(4)*Spare(spare,avoid, count_remaining_cards(occur),remaining_cards_with_occur)*Required(hand,occur)/permutations
    elif street == "5th" and possible:
        spare = 3 - required_card
        num3 = list_numplayers[0]
        num4 = list_numplayers[1]
        permutations = ((52-(2 + num3+num4)))*((51-(2 + num3+num4)))*((50-(2 + num3+num4)))
        probability = factorial(3)*Spare(spare,avoid, count_remaining_cards(occur),remaining_cards_with_occur)*Required(hand,occur)/permutations
    elif street == "6th" and possible:
        spare = 2 - required_card
        num3 = list_numplayers[0]
        num4 = list_numplayers[1]
        num5 = list_numplayers[2]
        permutations = ((52-(2 + num3+num4+num5)))*((51-(2 + num3+num4+num5)))
        probability = factorial(2)*Spare(spare,avoid, count_remaining_cards(occur),remaining_cards_with_occur)*Required(hand,occur)/permutations
    elif street == "RIVER" and possible: 
        spare = 1 - required_card
        num3 = list_numplayers[0]
        num4 = list_numplayers[1]
        num5 = list_numplayers[2]
        num6 = list_numplayers[3]
        permutations = (52-(2+ num3+num4+num5+num6))
        probability = factorial(1)*Spare(spare,avoid,count_remaining_cards(occur),remaining_cards_with_occur)*Required(hand,occur)/permutations
    
    else:
        if possible:
            probability = 1

        else:
            return 0
    
    return probability

def generate_all_three():
    nums = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
    lst_full = []
    hand=[]
    for i in range (13):
        hand = []
        hand.append(nums[i])
        hand.append(nums[i])
        hand.append(nums[i])

        lst_full.append(hand)
    return lst_full
lst_three = generate_all_three()
def Required_three(hand,occur):
    pro_cards = 1
    number_card=1
    have  = False
    nums = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']

    remaining_three = 0
    count_three = 0
    index_three = nums.index(hand[0])
    for i in range (4):
        if occur[i][index_three] == 0:
            remaining_three +=1
        elif occur[i][index_three] == 1:
            count_three +=1
    if count_three == 0:
        pro_cards *= remaining_three*(remaining_three-1)*(remaining_three-2)
    elif count_three == 1:
        pro_cards *= remaining_three*(remaining_three-1)
    elif count_three == 2:
        pro_cards *= remaining_three
    return pro_cards
def possible_hand_three(hand,occur,street):
    nums = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
    
    count_three = 0
    required_card = 3
    
    index_three = nums.index(hand[0])
    for i in range (4):

        if occur[i][index_three] == 1:
            count_three +=1

    if count_three > 3 :
        possible = False
        required_card = 3
    else:
        required_card-= (count_three)

    if street == "4th" and required_card > 4:
        possible = False
    elif street == "5th" and required_card > 3:
        possible = False
    elif street == "6th" and required_card > 2:
        possible = False
    elif street == "RIVER" and required_card > 1:
         possible = False
    elif (street == "SHOW" or street == "SUMMARY" ) and required_card == 0:
        possible = True
    elif street == "SHOW" or street == "SUMMARY" :
        possible = False
    else:
        return (True,required_card)
    return (possible,required_card)
def Avoid_Three(hand,occur):
    nums = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
    avoid_cards = [hand[0]]
    remaining_cards = []
    remaining_cards_with_occurence= []
    count_avoid = 1
    index_three = nums.index(hand[0])
    for i in range (4):
        if occur[i][index_three] == -1:
            count_avoid = 0
    for card in nums:
        if not(card in avoid_cards):
            remaining_cards.append(card)
    for card in remaining_cards:
        remaining_cards_with_occurence.append([card,count_cards([card],occur)])
    return (count_avoid,remaining_cards_with_occurence)

def Three_probability(hand,occur,street,list_numplayers):
    (possible,required_card)  = possible_hand_three(hand,occur,street)

    permutations = 0
    spare = 0
    probability = 0
    (avoid,remaining_cards_with_occur) =Avoid_Three(hand,occur)
    if required_card == 0 :
        return 1
    if street == "4th" and possible:
        spare = 4 - required_card
        num3 = list_numplayers[0]
        permutations = ((52-(2 + num3)))*((51-(2 + num3)))*((50-(2 + num3)))*((49-(2 + num3)))
        probability = factorial(4)*Spare(spare,avoid, count_remaining_cards(occur),remaining_cards_with_occur)*Required_three(hand,occur)/permutations
    elif street == "5th" and possible:
        spare = 3 - required_card
        num3 = list_numplayers[0]
        num4 = list_numplayers[1]
        permutations = ((52-(2 + num3+num4)))*((51-(2 + num3+num4)))*((50-(2 + num3+num4)))
        probability = factorial(3)*Spare(spare,avoid, count_remaining_cards(occur),remaining_cards_with_occur)*Required_three(hand,occur)/permutations
    elif street == "6th" and possible:
        spare = 2 - required_card
        num3 = list_numplayers[0]
        num4 = list_numplayers[1]
        num5 = list_numplayers[2]
        permutations = ((52-(2 + num3+num4+num5)))*((51-(2 + num3+num4+num5)))
        probability = factorial(2)*Spare(spare,avoid, count_remaining_cards(occur),remaining_cards_with_occur)*Required_three(hand,occur)/permutations
    elif street == "RIVER" and possible: 
        spare = 1 - required_card
        num3 = list_numplayers[0]
        num4 = list_numplayers[1]
        num5 = list_numplayers[2]
        num6 = list_numplayers[3]
        permutations = (52-(2+ num3+num4+num5+num6))
        probability = factorial(1)*Spare(spare,avoid,count_remaining_cards(occur),remaining_cards_with_occur)*Required_three(hand,occur)/permutations
    else:
        if possible:
            probability = 1

        else:
            return 0
    return probability



def generate_all_two():
    nums = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
    lst_full = []
    hand=[]
    for i in range (12):
        for j in range (i+1,13):
            hand = []
            hand.append(nums[i])
            hand.append(nums[i])
            hand.append(nums[j])
            hand.append(nums[j]) 
            lst_full.append(hand)
    return lst_full
lst_two = generate_all_two()
def Required_two(hand,occur):
    pro_cards = 1
    number_card=1
    have  = False
    nums = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
    remaining_pair1 = 0
    remaining_pair2 = 0
    count_pair2 = 0
    count_pair1 = 0
    index_pair1 = nums.index(hand[0])
    index_pair2 = nums.index(hand[2])
    for i in range (4):
        if occur[i][index_pair1] == 0: 
            remaining_pair1 +=1
        elif occur[i][index_pair1] == 1: 
            count_pair1 +=1
        if occur[i][index_pair2] == 0:
            remaining_pair2 +=1
        elif occur[i][index_pair2] == 1:
            count_pair2 +=1
    if count_pair1 == 0:
        pro_cards *=remaining_pair1*(remaining_pair1-1)
    elif count_pair1 == 1:
        pro_cards *=remaining_pair1
    if count_pair2 == 0:
        pro_cards *=remaining_pair2*(remaining_pair2-1)
    elif count_pair2 == 1:
        pro_cards *=remaining_pair2

    return pro_cards
def possible_hand_two(hand,occur,street):
    nums = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
    count_pair1 = 0
    count_pair2 = 0
    required_card = 4
    index_pair1 = nums.index(hand[0])
    index_pair2 = nums.index(hand[2])
    for i in range (4):
        if occur[i][index_pair1] == 1:
            count_pair1 +=1
        if occur[i][index_pair2] == 1:
            count_pair2 +=1

    if count_pair1> 2 or count_pair2 > 2:
        possible = False
        required_card = 4
    else:
        required_card-= (count_pair2 + count_pair1)

    if street == "4th" and required_card > 4:
        possible = False
    elif street == "5th" and required_card > 3:
        possible = False
    elif street == "6th" and required_card > 2:
        possible = False
    elif street == "RIVER" and required_card > 1:
         possible = False
    elif (street == "SHOW" or street == "SUMMARY" ) and required_card == 0:
        possible = True
    elif street == "SHOW" or street == "SUMMARY" :
        possible = False
    else:
        return (True,required_card)
    return (possible,required_card)
def Avoid_two(hand,occur):

    nums = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
    avoid_cards = [hand[0],hand[2]]
    remaining_cards = []
    remaining_cards_with_occurence= []
    for card in nums:
        if not(card in avoid_cards):
            remaining_cards.append(card)
    for card in remaining_cards:
        remaining_cards_with_occurence.append([card,count_cards([card],occur)])
    return (count_cards(avoid_cards,occur),remaining_cards_with_occurence)

def Two_probability(hand,occur,street,list_numplayers):
    (possible,required_card)  = possible_hand_two(hand,occur,street)
    
    permutations = 0
    spare = 0
    probability = 0
    (avoid,remaining_cards_with_occur) =Avoid_two(hand,occur)
    if required_card == 0 :
        return 1
    if street == "4th" and possible:
        spare = 4 - required_card
        num3 = list_numplayers[0]
        permutations = ((52-(2 + num3)))*((51-(2 + num3)))*((50-(2 + num3)))*((49-(2 + num3)))
        probability = factorial(4)*Spare(spare,avoid, count_remaining_cards(occur),remaining_cards_with_occur)*Required_two(hand,occur)/permutations
    elif street == "5th" and possible:
        spare = 3 - required_card
        num3 = list_numplayers[0]
        num4 = list_numplayers[1]
        permutations = ((52-(2 + num3+num4)))*((51-(2 + num3+num4)))*((50-(2 + num3+num4)))
        probability = factorial(3)*Spare(spare,avoid, count_remaining_cards(occur),remaining_cards_with_occur)*Required_two(hand,occur)/permutations
    elif street == "6th" and possible:
        spare = 2 - required_card
        num3 = list_numplayers[0]
        num4 = list_numplayers[1]
        num5 = list_numplayers[2]
        permutations = ((52-(2 + num3+num4+num5)))*((51-(2 + num3+num4+num5)))
        probability = factorial(2)*Spare(spare,avoid, count_remaining_cards(occur),remaining_cards_with_occur)*Required_two(hand,occur)/permutations
    elif street == "RIVER" and possible: 
        spare = 1 - required_card
        num3 = list_numplayers[0]
        num4 = list_numplayers[1]
        num5 = list_numplayers[2]
        num6 = list_numplayers[3]
        permutations = (52-(2+ num3+num4+num5+num6))
        probability = factorial(1)*Spare(spare,avoid,count_remaining_cards(occur),remaining_cards_with_occur)*Required_two(hand,occur)/permutations
    else:
        if possible:
            probability = 1
        elif required_card == -1:
            return -1
        else:
            return 0
    return probability 



def generate_all_pair():
    nums = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
    lst_full = []
    hand=[]
    for i in range (13):
        hand = []
        hand.append(nums[i])
        hand.append(nums[i])
        lst_full.append(hand)
    return lst_full
lst_pair = generate_all_pair()
def Required_pair(hand,occur):
    pro_cards = 1
    number_card=1
    have  = False
    nums = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
    remaining_pair1 = 0
    count_pair1 = 0
    index_pair1 = nums.index(hand[0])

    for i in range (4):
        if occur[i][index_pair1] == 0: 
            remaining_pair1 +=1
        elif occur[i][index_pair1] == 1: 
            count_pair1 +=1

    if count_pair1 == 0:
        pro_cards *=remaining_pair1*(remaining_pair1-1)
    elif count_pair1 == 1:
        pro_cards *=remaining_pair1


    return pro_cards
def possible_hand_pair(hand,occur,street):
    nums = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
    count_pair1 = 0

    required_card = 2
    index_pair1 = nums.index(hand[0])

    for i in range (4):
        if occur[i][index_pair1] == 1:
            count_pair1 +=1


    if count_pair1> 2:
        possible = False
        required_card = 2
    else:
        required_card-= ( count_pair1)

    if street == "4th" and required_card > 4:
        possible = False
    elif street == "5th" and required_card > 3:
        possible = False
    elif street == "6th" and required_card > 2:
        possible = False
    elif street == "RIVER" and required_card > 1:
         possible = False
    elif (street == "SHOW" or street == "SUMMARY" ) and required_card == 0:
        possible = True
    elif street == "SHOW" or street == "SUMMARY" :
        possible = False
    else:
        return (True,required_card)
    return (possible,required_card)
def Avoid_pair(hand,occur):
    nums = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
    avoid_cards = [hand[0]]
    remaining_cards = []
    remaining_cards_with_occurence= []
    for card in nums:
        if not(card in avoid_cards):
            remaining_cards.append(card)
    for card in remaining_cards:
        remaining_cards_with_occurence.append([card,count_cards([card],occur)])
    return (count_cards(avoid_cards,occur),remaining_cards_with_occurence)
def sum_occur(remaining_cards_with_occur,i):
    j = 0
    S = 0
    while j < len(remaining_cards_with_occur):
        if j != i:
            S+=remaining_cards_with_occur[j][1]
        j+=1
    return 0
def Spare_pair(spare,avoid, remaining_cards,remaining_cards_with_occur):
    
    if spare == 1:
        return remaining_cards - avoid
    elif spare == 2:
       ''' for i in range (0,len(remaining_cards_with_occur)):
            if remaining_cards_with_occur[i][1] == 2:
                avoid1 +=2
            elif remaining_cards_with_occur[i][1] == 3: 
                avoid1 +=6
            elif remaining_cards_with_occur[i][1] == 4: 
                avoid1 += 12'''
       return calculate_combinations(remaining_cards - avoid, 2,remaining_cards_with_occur) 
    elif spare == 3:
        '''for i in range (0,len(remaining_cards_with_occur)):
            if remaining_cards_with_occur[i][1] == 2:
                avoid1 +=2 * (remaining_cards - avoid - 2)
            elif remaining_cards_with_occur[i][1] == 3: 
                avoid1 +=6 +6*(remaining_cards - avoid - 3)
            elif remaining_cards_with_occur[i][1] == 4: 
                avoid1 +=  3*6 + 12 * (remaining_cards - avoid - 4)'''
        return calculate_combinations(remaining_cards - avoid, 3,remaining_cards_with_occur)
    elif spare == 4:
        
        return calculate_combinations(remaining_cards - avoid, 4,remaining_cards_with_occur)
    else:
        return 1
def Pair_probability(hand,occur,street,list_numplayers):
    (possible,required_card)  = possible_hand_pair(hand,occur,street)

    permutations = 0
    spare = 0
    probability = 0
    (avoid,remaining_cards_with_occur) =Avoid_pair(hand,occur)
    if required_card == 0 :
        return 1
    elif street == "4th" and possible:
        spare = 4 - required_card
        num3 = list_numplayers[0]
        permutations = ((52-(2 + num3)))*((51-(2 + num3)))*((50-(2 + num3)))*((49-(2 + num3)))
        probability = factorial(4)*Spare_pair(spare,avoid, count_remaining_cards(occur),remaining_cards_with_occur)*Required_pair(hand,occur)/permutations
    elif street == "5th" and possible:
        spare = 3 - required_card
        num3 = list_numplayers[0]
        num4 = list_numplayers[1]
        permutations = ((52-(2 + num3+num4)))*((51-(2 + num3+num4)))*((50-(2 + num3+num4)))
        probability = factorial(3)*Spare_pair(spare,avoid, count_remaining_cards(occur),remaining_cards_with_occur)*Required_pair(hand,occur)/permutations
    elif street == "6th" and possible:
        spare = 2 - required_card
        num3 = list_numplayers[0]
        num4 = list_numplayers[1]
        num5 = list_numplayers[2]
        permutations = ((52-(2 + num3+num4+num5)))*((51-(2 + num3+num4+num5)))
        probability = factorial(2)*Spare_pair(spare,avoid, count_remaining_cards(occur),remaining_cards_with_occur)*Required_pair(hand,occur)/permutations
    elif street == "RIVER" and possible: 
        spare = 1 - required_card
        num3 = list_numplayers[0]
        num4 = list_numplayers[1]
        num5 = list_numplayers[2]
        num6 = list_numplayers[3]
        permutations = (52-(2+ num3+num4+num5+num6))
        probability = factorial(1)*Spare_pair(spare,avoid,count_remaining_cards(occur),remaining_cards_with_occur)*Required_pair(hand,occur)/permutations
    else:
        if possible:
            probability = 1
        elif required_card == -1:
            return -1
        else:
            return 0
    return probability 
def high_hand_odd(occur,street,list_numplayers):
    nums = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
    odd = 0
    odd_royal_flush = 0
    rf_zero = 0
    odd_straight_flush = 0
    sf_zero = 0

    odd_four_of_Kind = 0
    fok_zero = 0
    odd_full_house = 0
    fh_zero = 0
    odd_flush = 0
    f_zero = 0
    odd_straight = 0
    s_zero = 0
    odd_three_of_kind = 0
    tok_zero = 0
    odd_two_pairs = 0
    tp_zero = 0
    odd_pair = 0
    p_zero = 0
    hc_zero = 0
    odd_high_card = 0
    odd=0
    for k in range (4):
        odd = straight_flush_probability(['T','J','Q','K','A'],k,occur,street,list_numplayers)
        odd_royal_flush += odd
        if odd == 1:
            return [['Royal Flush',1,1],['Straight Flush',odd_straight_flush,sf_zero],['Four of Kind',odd_four_of_Kind,fok_zero],['Full House',odd_full_house,fh_zero],['Flush',odd_flush,f_zero],['Straight',odd_straight,s_zero],['Three of Kind',odd_three_of_kind,tok_zero],['Two Pairs',odd_two_pairs,tp_zero],["Pair",odd_pair,p_zero]]
    if odd_royal_flush != 0:
        rf_zero = 1
    
    odd =0
    for hand in lst_straight:
        for k in range (4):
            odd = straight_flush_probability(hand,k,occur,street,list_numplayers)
            odd_straight_flush += odd
            if odd == 1:
                return [['Royal Flush',odd_royal_flush,rf_zero],['Straight Flush',1,1],['Four of Kind',odd_four_of_Kind,fok_zero],['Full House',odd_full_house,fh_zero],['Flush',odd_flush,f_zero],['Straight',odd_straight,s_zero],['Three of Kind',odd_three_of_kind,tok_zero],['Two Pairs',odd_two_pairs,tp_zero],["Pair",odd_pair,p_zero]]
    if odd_straight_flush !=0:
        sf_zero = 1
    odd = 0
    for hand in lst_four:
        odd = Four_probability(hand,occur,street,list_numplayers)
        odd_four_of_Kind += odd
        if odd == 1 :
            return [['Royal Flush',odd_royal_flush,rf_zero],['Straight Flush',odd_straight_flush,sf_zero],['Four of Kind',1,1],['Full House',odd_full_house,fh_zero],['Flush',odd_flush,f_zero],['Straight',odd_straight,s_zero],['Three of Kind',odd_three_of_kind,tok_zero],['Two Pairs',odd_two_pairs,tp_zero],["Pair",odd_pair,p_zero]]

        

    if odd_four_of_Kind != 0:
        fok_zero = 1
    
    odd = 0
    for hand in lst_full:
        odd = full_probability(hand,occur,street,list_numplayers)
        odd_full_house += odd 
        if odd == 1:
            return [['Royal Flush',odd_royal_flush,rf_zero],['Straight Flush',odd_straight_flush,sf_zero],['Four of Kind',odd_four_of_Kind,fok_zero],['Full House',1,1],['Flush',odd_flush,f_zero],['Straight',odd_straight,s_zero],['Three of Kind',odd_three_of_kind,tok_zero],['Two Pairs',odd_two_pairs,tp_zero],["Pair",odd_pair,p_zero]]
    if odd_full_house != 0:
        fh_zero = 1
    odd = 0
    for i in range (0,4):
        odd = flush_probability(occur,i,street,list_numplayers)
        odd_flush += odd
        if odd == 1 :
            return [['Royal Flush',odd_royal_flush,rf_zero],['Straight Flush',odd_straight_flush,sf_zero],['Four of Kind',odd_four_of_Kind,fok_zero],['Full House',odd_full_house,fh_zero],['Flush',1,1],['Straight',odd_straight,s_zero],['Three of Kind',odd_three_of_kind,tok_zero],['Two Pairs',odd_two_pairs,tp_zero],["Pair",odd_pair,p_zero]]
    if odd_flush != 0:
        f_zero = 1
    
    odd =0
    for hand in lst_straight:
        odd = straight_probability(hand,occur,street,list_numplayers)
        odd_straight += odd
        if odd == 1:
            return [['Royal Flush',odd_royal_flush,rf_zero],['Straight Flush',odd_straight_flush,sf_zero],['Four of Kind',odd_four_of_Kind,fok_zero],['Full House',odd_full_house,fh_zero],['Flush',odd_flush,f_zero],['Straight',1,1],['Three of Kind',odd_three_of_kind,tok_zero],['Two Pairs',odd_two_pairs,tp_zero],["Pair",odd_pair,p_zero]]
    if odd_straight != 0:
        s_zero = 1
   
    odd = 0
    for hand in lst_three:
         odd = Three_probability(hand,occur,street,list_numplayers)
         odd_three_of_kind += odd
         if odd == 1:
             return [['Royal Flush',odd_royal_flush,rf_zero],['Straight Flush',odd_straight_flush,sf_zero],['Four of Kind',odd_four_of_Kind,fok_zero],['Full House',odd_full_house,fh_zero],['Flush',odd_flush,f_zero],['Straight',odd_straight,s_zero],['Three of Kind',1,1],['Two Pairs',odd_two_pairs,tp_zero],["Pair",odd_pair,p_zero]]
    if odd_three_of_kind != 0:
        tok_zero = 1
    odd = 0
    for hand in lst_two:
        odd= Two_probability(hand,occur,street,list_numplayers)
        odd_two_pairs += odd 
        if odd == 1:
            return [['Royal Flush',odd_royal_flush,rf_zero],['Straight Flush',odd_straight_flush,sf_zero],['Four of Kind',odd_four_of_Kind,fok_zero],['Full House',odd_full_house,fh_zero],['Flush',odd_flush,f_zero],['Straight',odd_straight,s_zero],['Three of Kind',odd_three_of_kind,tok_zero],['Two Pairs',1,1],["Pair",odd_pair,p_zero]]
    if odd_two_pairs !=0:
        tp_zero = 1
    odd = 0
    for hand in lst_pair:
        odd = Pair_probability(hand,occur,street,list_numplayers)
        
        odd_pair += odd
        if odd == 1:
            return [['Royal Flush',odd_royal_flush,rf_zero],['Straight Flush',odd_straight_flush,sf_zero],['Four of Kind',odd_four_of_Kind,fok_zero],['Full House',odd_full_house,fh_zero],['Flush',odd_flush,f_zero],['Straight',odd_straight,s_zero],['Three of Kind',odd_three_of_kind,tok_zero],['Two Pairs',odd_two_pairs,tp_zero],["Pair",1,1]]

    if odd_two_pairs !=0:
        p_zero = 1
    
    return [['Royal Flush',odd_royal_flush,rf_zero],['Straight Flush',odd_straight_flush,sf_zero],['Four of Kind',odd_four_of_Kind,fok_zero],['Full House',odd_full_house,fh_zero],['Flush',odd_flush,f_zero],['Straight',odd_straight,s_zero],['Three of Kind',odd_three_of_kind,tok_zero],['Two Pairs',odd_two_pairs,tp_zero],["Pair",odd_pair,p_zero]]
