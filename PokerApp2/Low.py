from Odds import Card_To_Html, count_card, odd_Low_7cards ,list_function, Best_hand
low5 = [['5','4','3','2','A']]

nums_possible_8 = ['9','T','J','Q','K']
   
low8 =[['8','4','3','2','A'],
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
all_low8 = []
hand_all = []
for hand in low8:
    hand_all = nums_possible_8 + hand 
    for i in range (len(hand_all)):
        for k in range (i,len(hand_all)):
            new_hand = []
            for card in hand:
                new_hand.append(card)
            new_hand.append(hand_all[i])
            new_hand.append(hand_all[k])
            all_low8.append(new_hand)


nums_possible_7 = ['8','9','T','J','Q','K']

low7 = [['7','4','3','2','A'],
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
            ['7','6','5','4','3']]
all_low7 = []
hand_all = []
for hand in low7:
    hand_all = nums_possible_7 +hand
    for i in range (len(hand_all)):
        for k in range (i,len(hand_all)):
            new_hand = []
            for card in hand:
                new_hand.append(card)
            new_hand.append(hand_all[i])
            new_hand.append(hand_all[k])
            all_low7.append(new_hand)

low6 = [['6','4','3','2','A'],
    ['6','5','3','2','A'],
    ['6','5','4','2','A'],
    ['6','5','4','3','A'],
    ['6','5','4','3','2']]
nums_possible_6 = ['7','8','9','T','J','Q','K']
all_low6 = []
hand_all = []
for hand in low6:
    hand_all = nums_possible_6 + hand
    for i in range (len(hand_all)):
        for k in range (i,len(hand_all)):
            new_hand = []
            for card in hand:
                new_hand.append(card)
            new_hand.append(hand_all[i])
            new_hand.append(hand_all[k])
            all_low6.append(new_hand)

low5 =[['5','4','3','2','A']]
nums_possible_5 = ['6','7','8','9','T','J','Q','K']
all_low5 = []
hand_all = []
for hand in low5:
    hand_all = nums_possible_5 +hand
    for i in range (len(hand_all)):
        for k in range (i,len(hand_all)):
            new_hand = []
            for card in hand:
                new_hand.append(card)
            new_hand.append(hand_all[i])
            new_hand.append(hand_all[k])
            all_low5.append(new_hand)



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
    have_hand=[]
    best_8low = []
    hand = []
    low_hand_odds = []
    odd_have_it = 0
    Odds = []   
    low_hand =  all_low5 + all_low6 + all_low7 + all_low8
    for hand in low_hand :
        low_hand_odds.append([hand,odd_Low_7cards(hand,occur,street,list_numplayers)])

    while (low_hand_odds[i][0][0] == '5'):
        hand = low_hand_odds[i][0]
        odd = low_hand_odds[i][1]
        odd_5low += odd
        if odd > odd_5low_max:
            odd_5low_max = odd
            best_5low = Best_hand(hand,occur)
            odd_have_it = odd_Low(hand[:-2],occur,street,list_numplayers)
        i+=1
    if odd_have_it == 1:
        best_5low = Best_hand(hand[:-2],occur)
        return(["5-Low",best_5low,1,int(round(odd_5low,2)*100)])
        
    Odds.append(["5-Low",best_5low,int(round(odd_5low_max,2)),int(round(odd_5low,2)*100)])
    while (low_hand_odds[i][0][0] == '6'):
        hand = low_hand_odds[i][0]
        odd = low_hand_odds[i][1]
        odd_6low += odd
        if odd > odd_6low_max:
            odd_6low_max = odd
            best_6low = Best_hand(hand,occur)
            odd_have_it = odd_Low(hand[:-2],occur,street,list_numplayers)
            if odd_Low(hand[:-2],occur,street,list_numplayers) == 1:
                odd_have_it = 1
                have_hand = Best_hand(hand[:-2],occur)
        
        i+=1
    if odd_have_it == 1:
            best_6low = have_hand
            Odds.append(["6-Low",best_6low,100,int(round(odd_6low,2)*100)])
            return Odds
    Odds.append(["6-Low",best_6low,int(round(odd_6low_max,2)*100),int(round(odd_6low,2)*100)])
    while (low_hand_odds[i][0][0] == '7'):
        hand = low_hand_odds[i][0]
        odd = low_hand_odds[i][1]
        odd_7low += odd
        
        if odd > odd_7low_max:
            odd_7low_max = odd 
            best_7low = Best_hand(hand,occur)
            if odd_Low(hand[:-2],occur,street,list_numplayers) == 1:
                odd_have_it = 1
                have_hand = Best_hand(hand[:-2],occur)
        i+=1
    if odd_have_it == 1:
        best_7low = have_hand
        Odds.append(["7-Low",best_7low,100,int(round(odd_7low,2)*100)])
        return Odds
    Odds.append(["7-Low",best_7low,int(round(odd_7low_max,2)*100),int(round(odd_7low,2)*100)])
    while (i < len(low_hand_odds) and low_hand_odds[i][0][0] == '8'):
        hand = low_hand_odds[i][0]
        odd = low_hand_odds[i][1]
        odd_8low += odd
        if odd > odd_8low_max:
            odd_8low_max= odd
            best_8low = Best_hand(hand,occur)
            
            if odd_Low(hand[:-2],occur,street,list_numplayers) == 1:
                odd_have_it = 1
                have_hand = Best_hand(hand[:-2],occur)
        
            
        i+=1
    print(street,["8-Low",best_8low,int(round(odd_8low_max,2)*100),int(round(odd_8low,2)*100)])   
    Odds.append(["8-Low",best_8low,int(round(odd_8low_max,2)*100),int(round(odd_8low,2)*100)])

    return Odds