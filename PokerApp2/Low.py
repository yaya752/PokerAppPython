from Odds import Card_To_Html, count_card, odd_Low_7cards ,list_function, Best_hand
from math import *
low5 = [['5','4','3','2','A']]

   
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


low6 = [['6','4','3','2','A'],
    ['6','5','3','2','A'],
    ['6','5','4','2','A'],
    ['6','5','4','3','A'],
    ['6','5','4','3','2']]



low5 =[['5','4','3','2','A']]

def Avoid(hand,occur):
    nums = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
    avoid_cards = []
    remaining_cards = []
    remaining_cards_with_occurence= []
    if hand[0] == '8':
        all_avoid_card = ['A','2','3','4','5','6','7']
        for card in all_avoid_card:
            if not(card in hand):
                avoid_cards.append(card)
    elif hand[0] == '7':
        all_avoid_card = ['A','2','3','4','5','6']
        for card in all_avoid_card:
            if not(card in hand):
                avoid_cards.append(card)
    elif hand[0] == '6':
        all_avoid_card = ['A','2','3','4','5']
        for card in all_avoid_card:
            if not(card in hand):
                avoid_cards.append(card)
    for card in nums:
        if not(card in avoid_cards):
            remaining_cards.append(card)
    for card in remaining_cards:
        remaining_cards_with_occurence.append([card,count_cards([card],occur)])
    return (count_cards(avoid_cards,occur),remaining_cards_with_occurence)
def count_cards(lst,occur):
    sum_cards = 0
    nums = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
    for card in lst:
        k = nums.index(card)
        for i in range (4):
            if occur[i][k] == 0:
                sum_cards+=1
    return sum_cards

def calculate_combinations(n, r,remaining_cards_with_occur):
    if n < r:
        return 0
    all_comb = factorial(n) // (factorial(r) * factorial(n - r))
    for [card,count_card] in remaining_cards_with_occur:
        if count_card >= 2:
            all_comb-=1
        
    return all_comb
def new_probability(hand,occur,street,list_numplayers):
    (possible,required_card)  = possible_hand_low(hand,occur,street)
    print(street,hand,(possible,required_card))
    permutations = 0
    spare = 0
    probability = 0
    (avoid,remaining_cards_with_occur) =Avoid(hand,occur)
    #=SI(AD11=1,L$6-AF11,SI(AD11=2,COMBIN(L$6-AF11,2),1))
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
        return 0
    
    return probability
def Required(hand,occur):
    pro_cards = 1
    number_card=1
    have  = False
    nums = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
    for card in hand:
        k = nums.index(card)
        have  = False
        number_card=0
        for i in range (4):
            if occur[i][k] == 1:
                have  = True
        if not(have):
            for i in range (4):
                if occur[i][k] == 0:
                    number_card+=1
            pro_cards*=number_card
    return pro_cards

def count_remaining_cards(occur):
    S = 0
    for i in range (4):
        for j in range(13):
            if occur[i][j]==0:
                S+=1
    return S
def Spare(spare,avoid, remaining_cards,remaining_cards_with_occur):
    print(spare)
    if spare == 1:
        return remaining_cards - avoid
    elif spare == 2:
        return calculate_combinations(remaining_cards - avoid, 2,remaining_cards_with_occur)
    else:
        return 1
def possible_hand_low(hand,occur,street):
    nums = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
    avoid_cards = []
    if hand[0] == '8':
        all_avoid_card = ['A','2','3','4','5','6','7']
        for card in all_avoid_card:
            if not(card in hand):
                avoid_cards.append(card)
    elif hand[0] == '7':
        all_avoid_card = ['A','2','3','4','5','6']
        for card in all_avoid_card:
            if not(card in hand):
                avoid_cards.append(card)
    elif hand[0] == '6':
        all_avoid_card = ['A','2','3','4','5']
        for card in all_avoid_card:
            if not(card in hand):
                avoid_cards.append(card)

    for card in avoid_cards:
        k = nums.index(card)
        for i in range (4):
            if occur[i][k] == 1:
                return (False,5)
    required_card = 5
    for card in hand:
        k = nums.index(card)
        i = 0
        while i < 4 and occur[i][k] != 1:
            i+=1
        if i !=4:
            required_card -= 1
    
    if street == "4th" and required_card > 4:
        possible = False
    elif street == "5th" and required_card > 3:
        possible = False
    elif street == "6th" and required_card > 2:
        possible = False
    elif street == "RIVER" and required_card > 1:
         possible = False
    elif street == "SHOW" or street == "SUMMARY":
        possible = False
    else:
        return (True,required_card)
    return (possible,required_card)


def low_hand_odd(occur,street,list_numplayers):
    i = 0
    odd = 0
    odd_5low = 0.
    odd_6low = 0.
    odd_7low = 0.
    odd_8low = 0.
    have_5low = 1
    have_6low = 1
    have_7low = 1
    have_8low = 1
    hand = []
    low_hand_odds = []
    odd_have_it = 0
    Odds = []   
    low_hand =  low5 + low6 + low7 + low8
    
    for hand in low_hand :
        
        low_hand_odds.append([hand,new_probability(hand,occur,street,list_numplayers)])
    
    while (low_hand_odds[i][0][0] == '5'):
        hand = low_hand_odds[i][0]
        odd = low_hand_odds[i][1]
        odd_5low += odd
        i+=1
    if odd_5low == 0:
        have_5low = 0
    Odds.append(["5-Low",odd_5low,have_5low])
    while (low_hand_odds[i][0][0] == '6'):
        hand = low_hand_odds[i][0]
        odd = low_hand_odds[i][1]
        odd_6low += odd
        i+=1
    if odd_6low == 0:
        have_6low = 0
    Odds.append(["6-Low",odd_6low,have_6low])
    while (low_hand_odds[i][0][0] == '7'):
        hand = low_hand_odds[i][0]
        odd = low_hand_odds[i][1]
        odd_7low += odd
        i+=1
    if odd_7low == 0:
        have_7low = 0
    Odds.append(["7-Low",odd_7low,have_7low])
    while (i < len(low_hand_odds) and low_hand_odds[i][0][0] == '8'):
        if street == '4th' and low_hand_odds[i][1] != 0 :
            print(low_hand_odds[i])
        hand = low_hand_odds[i][0]
        odd = low_hand_odds[i][1]
        odd_8low += odd
        i+=1
    if odd_8low == 0:
        have_8low = 0
    Odds.append(["8-Low",odd_8low,have_8low])

    return Odds