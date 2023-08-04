from Odds import list_function,count_card,Card_To_Html, odd_Low_7cards
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
    
def high_hand_odd(occur,street,list_numplayers):
    nums = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
    odd_royal_flush = Royal_flush(occur,street,list_numplayers)
    rf_zero = 0
    if odd_royal_flush != 0:
        rf_zero = 1
    odd_straight_flush = 0
    sf_zero = 0
    '''
    for k in range(len(all_straight_flush_0)):
        odd_straight_flush+=odd_Straight_flush(all_straight_flush_0[0][k],occur,street,list_numplayers)
        odd_straight_flush+=odd_Straight_flush(all_straight_flush_1[0][k],occur,street,list_numplayers)
        odd_straight_flush+=odd_Straight_flush(all_straight_flush_2[0][k],occur,street,list_numplayers)
        odd_straight_flush+=odd_Straight_flush(all_straight_flush_3[0][k],occur,street,list_numplayers)
    for i in range(1,len(all_straight_flush_0)):
        if i%2 == 0 :
            for straight_flush in all_straight_flush_0[i]:
                
                odd_straight_flush+=straight_flush[1]*odd_Low_7cards(straight_flush[0],occur,street,list_numplayers)
        else:
            for straight_flush in all_straight_flush_0[i]:
                odd_straight_flush-=straight_flush[1]*odd_Low_7cards(straight_flush[0],occur,street,list_numplayers)
    for i in range(1,len(all_straight_flush_1)):
        if i%2 == 0 :
            for straight_flush in all_straight_flush_1[i]:
                
                odd_straight_flush+=straight_flush[1]*odd_Low_7cards(straight_flush[0],occur,street,list_numplayers)
        else:
            for straight_flush in all_straight_flush_1[i]:
                odd_flush-=straight_flush[1]*odd_Low_7cards(straight_flush[0],occur,street,list_numplayers)
    for i in range(1,len(all_straight_flush_2)):
        if i%2 == 0 :
            for straight_flush in all_straight_flush_2[i]:
                
                odd_straight_flush+=straight_flush[1]*odd_Low_7cards(straight_flush[0],occur,street,list_numplayers)
        else:
            for straight_flush in all_straight_flush_2[i]:
                odd_straight_flush-=straight[1]*odd_Low_7cards(straight_flush[0],occur,street,list_numplayers)
    for i in range(1,len(all_straight_flush_3)):
        if i%2 == 0 :
            for straight_flush in all_straight_flush_3[i]:
                
                odd_straight_flush+=straight_flush[1]*odd_Low_7cards(straight_flush[0],occur,street,list_numplayers)
        else:
            for straight_flush in all_straight_flush_3[i]:
                odd_flush-=straight_flush[1]*odd_Low_7cards(straight_flush[0],occur,street,list_numplayers)
    if odd_straight_flush != 0:
        sf_zero = 1
        '''
    odd_four_of_Kind = 0
    fok_zero = 0
    for i in range (0,13):
        odd_four_of_Kind += Four_Kind(occur,i,street,list_numplayers)
    if odd_four_of_Kind != 0:
        fok_zero = 1
    odd_full_house = 0
    fh_zero = 0
    odd_flush = 0
    f_zero = 0
    
    odd_three_of_kind = 0
    odd_straight = 0
    s_zero = 0
    i = 0
    
    for hand in all_straight[0]:
        odd_straight+=odd_Straight(hand,occur,street,list_numplayers)
    for i in range(1,len(all_straight)):
        if i%2 == 0 :
            for straight in all_straight[i]:
                
                odd_straight+=straight[1]*odd_Low_7cards(straight[0],occur,street,list_numplayers)
        else:
            for straight in all_straight[i]:
                odd_straight-=straight[1]*odd_Low_7cards(straight[0],occur,street,list_numplayers)
    
    if odd_straight != 0:
        s_zero = 1
    odd_three_of_kind = 0
    tok_zero = 0
    odd_two_pair = 0
    tp_zero = 0
    odd_pair = 0
    p_zero = 0
    odd_high_card = 0
    hc_zero = 0
    return [['Royal Flush',int(round(odd_royal_flush,2)*100),rf_zero],['Straight Flush',int(round(odd_straight_flush,2)*100),sf_zero],['Four of Kind',int(round(odd_four_of_Kind,2)*100),fok_zero],['Full House',int(round(odd_full_house,2)*100),fh_zero],['Flush',int(round(odd_flush,2)*100),f_zero],['Straight',odd_straight,s_zero],['Three of Kind',int(round(odd_three_of_kind,2)*100),tok_zero],['Two Pairs',int(round(odd_two_pair,2)*100),tp_zero],["Pair",int(round(odd_pair,2)*100),p_zero],['High Card',int(round(odd_high_card,2)*100),hc_zero]]
