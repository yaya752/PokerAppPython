def Card_To_Html(hand):
    #Intialisation of the variable
    Html_Cards = []
    num_cards = ['A','2','3','4','5','6','7','8','9','T','J','C','Q','K']
    shape_card = ['s','h','d','c']
    for card in hand:
        i= num_cards.index(card[0])
        j= shape_card.index(card[1])
        #in html we can display graphical card by using a unicode value
        Html_Cards.append(["#1271" + str(i+16*j + 37)+";",j])
    return Html_Cards
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
            ['6','5','3','2','A'],
            ['6','5','4','2','A'],
            ['6','5','4','3','A'],
            ['6','5','4','3','2'],
            ['7','4','3','2','A'],
            ['7','5','3','2','A'],
            ['7','5','4','2','A'],
            ['7','5','4','3','A'],
            ['7','5','4','3','2'],
            ['7','6','3','2','A'],
            ['7','6','4','2','A'],
            ['7','6','4','3','A'],
            ['7','6','4','3','2'],
            ['7','6','5','2','A'],
            ['7','6','5','3','A'],
            ['7','6','5','3','2'],
            ['7','6','5','4','A'],
            ['7','6','5','4','2'],
            ['7','6','5','4','3'],
            ['8','4','3','2','A'],
            ['8','5','3','2','A'],
            ['8','5','4','2','A'],
            ['8','5','4','3','A'],
            ['8','5','4','3','2'],
            ['8','6','3','2','A'],
            ['8','6','4','2','A'],
            ['8','6','4','3','A'],
            ['8','6','4','3','2'],
            ['8','6','5','2','A'],
            ['8','6','5','3','A'],
            ['8','6','5','3','2'],
            ['8','6','5','4','A'],
            ['8','6','5','4','2'],
            ['8','6','5','4','3'],
            ['8','7','3','2','A'],
            ['8','7','4','2','A'],
            ['8','7','4','3','A'],
            ['8','7','4','3','2'],
            ['8','7','5','2','A'],
            ['8','7','5','3','A'],
            ['8','7','5','3','2'],
            ['8','7','5','4','A'],
            ['8','7','5','4','2'],
            ['8','7','5','4','3'],
            ['8','7','6','2','A'],
            ['8','7','6','3','A'],
            ['8','7','6','3','2'],
            ['8','7','6','4','A'],
            ['8','7','6','4','2'],
            ['8','7','6','4','3'],
            ['8','7','6','5','A'],
            ['8','7','6','5','2'],
            ['8','7','6','5','3'],
            ['8','7','6','5','4']]
def Best_hand(hand,occur):
    notFind = True
    nums = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
    shapes = ['s','h','d','c']
    result = []
    for card in hand:
        j = nums.index(card)
        for i in range (0,4):
            if occur[i][j]== 1 :
                notFind = False
                result.append(nums[j] + shapes[i])
        for i in range(0,4):
            if notFind:
                if occur[i][j] == 0:
                    result.append(nums[j] + shapes[i])
                    notFind = False
        notFind = True
    return Card_To_Html(result)

def low_hand_odd(occur,street,list_numplayers):
    i = 0
    odd = 0
    odd_5low = 0.
    odd_6low = 0.
    odd_7low = 0.
    odd_8low = 0.
    odd_5low_max = 0.
    odd_6low_max= 0.
    odd_7low_max = 0.
    odd_8low_max = 0.
    best_5low = []
    best_6low = []
    best_7low = []
    best_8low = []
    hand = []
    low_hand_odds = []
    Odds = []
    for hand in low_hand :
        low_hand_odds.append([hand,odd_Low(hand,occur,street,list_numplayers)/len(low_hand)])
    while (low_hand_odds[i][0][0] == '5'):
        hand = low_hand_odds[i][0]
        odd = low_hand_odds[i][1]
        odd_5low += odd
        if odd > odd_5low_max:
            odd_5low_max = odd
           
            best_5low = Best_hand(hand,occur)
        if odd_5low_max == 1:
            odd_5low = 1
        i+=1
    Odds.append(["5-Low",best_5low,round(odd_5low_max*100,3)])
    while (low_hand_odds[i][0][0] == '6'):
        hand = low_hand_odds[i][0]
        odd = low_hand_odds[i][1]
        odd_6low += odd
        if odd > odd_6low_max:
            odd_6low_max = odd
            best_6low = Best_hand(hand,occur)
        if odd_6low_max == 1:
            odd_6low = 1
        i+=1
    Odds.append(["6-Low",best_6low,round(odd_6low_max*100,3)])
    while (low_hand_odds[i][0][0] == '7'):
        hand = low_hand_odds[i][0]
        odd = low_hand_odds[i][1]
        odd_7low += odd
        if odd > odd_7low_max:
            odd_7low_max = odd 
            best_7low = Best_hand(hand,occur)
        if odd_7low_max == 1:
            odd_7low = 1
        i+=1
    Odds.append(["7-Low",best_7low,round(odd_7low_max*100,3)])
    while (i < len(low_hand_odds) and low_hand_odds[i][0][0] == '8'):
        hand = low_hand_odds[i][0]
        odd = low_hand_odds[i][1]
        odd_8low += odd
        if odd > odd_8low_max:
            odd_8low_max= odd
            best_8low = Best_hand(hand,occur)
        if odd_8low_max == 1:
            odd_8low =1 
        i+=1
    Odds.append(["8-Low",best_8low,round(odd_8low_max*100,3)])
    return Odds

    
def odd_Low(low,occur,street,list_numplayers):
    nums = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
    suits = ['s','h','d','c']
    odd = 0.
    hand = 0
    remaining = []
    count = []
    for k in range (len(low)):
        pres = 0
        j = nums.index(low[k])
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
def better_low_hand(low_hand_odds,occur,hand):
    nums = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
    shape = ['s','h','d','c']
    index_hand = []
    lowest_cards = []
    index_low = []
    i_low = 13
    (odd,lowest_hand,odd_max,i_low) = (0,[],0,13)
    for card in hand:
        index_low.append(nums.index(card[:-1]))
    index_low.sort()  
    for i in index_low:
        if i > 5 and i <8:
            if i < i_low:
                i_low = i
    if  i_low == 13 : 
        i_low = 7
    j = 0
    while j < len(low_hand_odds) and int(low_hand_odds[j][0][0]) < i_low:
        odd_low = low_hand_odds[j][1]
        odd+=odd_low
        if odd_low > odd_max:
            lowest_cards = low_hand_odds[j][0]
            odd_max=odd_low
        j+=1
    if lowest_cards != []:
        for card in lowest_cards:
            index_card = nums.index(card)
            find = False
            for i in range (0,4):
                if occur[i][index_card] == 1 : 
                    find = True
                    lowest_hand.append(nums[index_card] + shape[i])
            if not(find):
                i = 0
                while i < 4 and occur[i][index_card] != 0:
                    i+=1
                if i != 4:
                    lowest_hand.append(nums[index_card] + shape[i])
    return (odd,lowest_hand,odd_max,i_low)
def odd_better_Straight(occur,street,list_numplayers):
    odd = 0.
    odd_straight = 0
    odd_max = 0
    best_hand = []
    poss = list_Straight()
    for straight in poss :
        odd_straight=odd_Straight(straight,occur,street,list_numplayers)
        odd+=odd_straight
        if odd_Straight(straight,occur,street,list_numplayers) == 1:
            return (1.,straight,1)
        elif odd_straight > odd_max:
            odd_max = odd_straight
            best_hand = straight
    return (odd,best_hand,odd_max)
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
def odd_better_pair(occur,card):
    num = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
    shape = ['s','h','d','c']
    
    odd = 0
    odd_max = 0
    best_hand = []
    odd_pair = 0
    count = 0
    l = 0
    index_card_max = num.index(card[:-1])
    if index_card_max!=0:
        odd_max = occur[4][0]
        if odd_max != 0:
            for i in range (len(occur)-3):
                if occur[i][0] == 1:
                    best_hand.append(num[0] + shape[i])
                    count += 1
            while count !=2 and l < 4:
                if occur[l][0] == 0:
                    best_hand.append(num[0] + shape[i])
                    count1+= 1
                l+=1
        for j in range (index_card_max +1,len(occur[0])-3):
            odd_pair = occur[4][j]
            odd += odd_pair
            if odd_pair > odd_max:
                odd_max =odd_pair
                for i in range (len(occur)-3):
                    if occur[i][j] == 1:
                        best_hand.append(num[j] + shape[i])
                        count += 1
                while count !=2 and l < 4:
                    if occur[l][j] == 0:
                        best_hand.append(num[j] + shape[i])
                        count+= 1
                    l+=1
    return(odd,best_hand,odd_max)

def odd_better_three_of_kind(occur,card):
    num = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
    shape = ['s','h','d','c']
    odd = 0
    odd_max = 0
    best_hand = []
    odd_three = 0
    count = 0
    l = 0
    if card =='':
        for j in range (len(occur[0])-3):
            odd_three = occur[5][j]
            odd += odd_three
            if odd_three > odd_max:
                odd_max =odd_three
                for i in range (len(occur)-3):
                    if occur[i][j] == 1:
                        best_hand.append(num[j] + shape[i])
                        count += 1
                while count !=3 and l < 4:
                    if occur[l][j] == 0:
                        best_hand.append(num[j] + shape[i])
                        count+= 1
                    l+=1
    else:
        index_card_max = num.index(card[:-1])
        if index_card_max!=0:
            odd_max = occur[4][0]
            if odd_max != 0:
                for i in range (len(occur)-3):
                    if occur[i][0] == 1:
                        best_hand.append(num[0] + shape[i])
                        count += 1
                while count !=2 and l < 4:
                    if occur[l][0] == 0:
                        best_hand.append(num[0] + shape[i])
                        count1+= 1
                    l+=1
            for j in range (index_card_max +1,len(occur[0])-3):
                odd_three = occur[5][j]
                odd += odd_three
                if odd_three > odd_max:
                    odd_max =odd_three
                    for i in range (len(occur)-3):
                        if occur[i][j] == 1:
                            best_hand.append(num[j] + shape[i])
                            count += 1
                    while count !=3 and l < 4:
                        if occur[l][j] == 0:
                            best_hand.append(num[j] + shape[i])
                            count+= 1
                        l+=1

    return(odd,best_hand,odd_max)
def odd_better_four_of_kind(occur):
    num = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
    shape = ['s','h','d','c']
    odd = 0
    odd_max = 0
    best_hand = []
    odd_four = 0
    count = 0
    l = 0
    for j in range (len(occur[0])-3):
        odd_four = occur[6][j]
        odd += odd_four
        if odd_four > odd_max:
            odd_max =odd_four
            for i in range (len(occur)-3):
                if occur[i][j] == 1:
                    best_hand.append(num[j] + shape[i])
                    count += 1
            while count !=3 and l < 4:
                if occur[l][j] == 0:
                    best_hand.append(num[j] + shape[i])
                    count+= 1
                l+=1
    return(odd,best_hand,odd_max)
def odd_better_Flush(occur, row,street, list_numplayers,card_max):
    num = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
    index = num.index(card_max[:-1])
    suit = ['s','h','d','c']
    odd = 0.
    odd_max = 0.
    hand = 0
    hand_cards = []
    best_hand = []
    remaining = []
    other = 0
    count = 0
    better = False
    other = 0
    count = 0
    odd_4 = 0
    odd_3 = 0 
    odd_2 = 0 
    odd_1 = 0 
    for j in range(len(occur[0])-3):
        if occur[row][j] == 1:
            hand += 1
            hand_cards.append(num[j] + suit[row])
            if j>index or j == 0 or index == 1 :
                better = True
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
                    index1 = num.index(card1[:-1])
                    for j in range (i+1,len(remaining)-2):
                        card2 = remaining[j]
                        index2 = num.index(card2[:-1])
                        for k in range (j+1,len(remaining)-1):
                            card3 = remaining[k]
                            index3 = num.index(card3[:-1])
                            for l in range (k+1,len(remaining)):
                                card4 = remaining[l]
                                index4 = num.index(card4[:-1])
                                if not(better) or (index1<=index and index2<=index and index3<=index and index4<=index) or (index1!=0 and index2!=0 and index3!=0 and index4!=0) :
                                    odd += 0
                                else:
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
                                                    odd_4= (odd1*odd6*odd11*odd16+
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
                                                    if odd_4 > odd_max:
                                                        best_hand = []
                                                        odd_max = odd_4
                                                        best_hand.append(card1)
                                                        best_hand.append(card2)
                                                        best_hand.append(card3)
                                                        best_hand.append(card4)
                                                    odd+= odd_4
            elif hand == 2:
               for i in range (0,len(remaining)-2):
                    card1 = remaining[i]
                    index1 = num.index(card1[:-1])
                    for j in range (i+1,len(remaining)-1):
                        card2 = remaining[j]
                        index2 = num.index(card2[:-1])
                        for k in range (j+1,len(remaining)):
                            card3 = remaining[k]
                            index3 = num.index(card3[:-1])
                            if not(better) or (index1<=index and index2<=index and index3<=index) or (index1!=0 and index2!=0 and index3!=0) :
                                    odd += 0
                            else:
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
                                            if odd_3 > odd_max:
                                                best_hand = []
                                                odd_max = odd_3
                                                best_hand.append(card1)
                                                best_hand.append(card2)
                                                best_hand.append(card3)
                                                best_hand += hand_cards
                                            odd+=odd_3 
            elif hand == 3:
                for i in range (0,len(remaining)-1):
                    card1 = remaining[i]
                    index1 = num.index(card1[:-1])
                    for j in range (i+1,len(remaining)):
                        card2 = remaining[j]
                        index2 = num.index(card2[:-1])
                        if not(better) or (index1<=index and index2<=index) or (index1!=0 and index2!=0) :
                                    odd += 0
                        else:
                            for m in range (0,len(list_function)-1):
                                odd1 = list_function[m](card1,occur,street,list_numplayers)
                                odd2 = list_function[m](card2,occur,street,list_numplayers)
                                for n in range (m+1,len(list_function)):
                                    odd5 = list_function[n](card1,occur,street,list_numplayers)
                                    odd6 = list_function[n](card2,occur,street,list_numplayers)
                                    odd_2 = (odd1*odd6 + odd2*odd5)
                                    if odd_2 > odd_max:
                                        best_hand = []
                                        odd_max = odd_2
                                        best_hand.append(card1)
                                        best_hand.append(card2)
                                        best_hand += hand_cards
                                    odd+=odd_2
            elif hand == 4:
                for i in range (0,len(remaining)):
                    card1 = remaining[i]
                    index1 = num.index(card1[:-1])
                    if not(better) or (index1<=index) or (index1!=0) :
                                    odd += 0
                    else:
                        for m in range (0,len(list_function)):
                            odd += list_function[m](card1,occur,street,list_numplayers)
                            odd_1 = (odd1*odd6 + odd2*odd5)
                            if odd_1 > odd_max:
                                best_hand = []
                                odd_max = odd_1
                                best_hand.append(card1)
                                best_hand.append(card2)
                                best_hand += hand_cards
                            odd+=odd_1
        else:
            odd = 0
    return (odd_max,best_hand,odd)
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
    nums = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
    shapes = ['s','h','d','c']
    occur = []
    for i in range(0,len(shapes)+3):
        row = []
        for j in range(0,len(nums)+3):
            row.append(0)
        occur.append(row)
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
    occur1 = Table()
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