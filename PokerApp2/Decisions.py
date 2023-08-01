from Odds import odd_better_Flush ,odd_better_three_of_kind, odd_better_four_of_kind, odd_better_Straight, better_low_hand, odd_better_pair
from High import odd_full_house,odd_two_pairs
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
def add(tab_player,tab_prec_player):
    for i in range (0,len(tab_player)):
        for j in range(0,len(tab_prec_player)):
            if tab_player[i][0] == tab_prec_player[j][0]:
                tab_player[i][3] +=tab_prec_player[j][3]
def index_poss(name,tab_player):
    i = 0
    while i < len(tab_player) and tab_player[i][0] != name:
        i+=1
    return i
def sumarry_tab(tab_player):
    player_name = []
    i = 0
    new_tab_player = []
    while i< len(tab_player):
        if tab_player[i][0] in player_name:
            j = player_name.index(tab_player[i][0])
            new_tab_player[j][3] = tab_player[i][3]
        else:
            new_tab_player.append(tab_player[i])
            player_name.append(tab_player[i][0])
        i+=1
    return new_tab_player 
# 4th street

def pair_4th(hand,aggresive_prec,aggressive,occur,street,list_numplayers):
    result = False
    (odd,best_hand,odd_max,card_max ) = (0,[],0,'')
    num_cards = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
    if aggressive != -1 :
        if hand[0][:-1] == 'T' or hand[0][:-1] == 'J' or hand[0][:-1] == 'Q' or hand[0][:-1] == 'K' or hand[0][:-1] == 'A':
            if aggresive_prec >= 2:
                result = True
        if hand[1][:-1] == 'T' or hand[1][:-1] == 'J' or hand[1][:-1] == 'Q' or hand[1][:-1] == 'K' or hand[1][:-1] == 'A':
            if aggresive_prec >= 2:
                result = True
        if result:
            i1 = num_cards.index(hand[0][:-1])
            i2 = num_cards.index(hand[1][:-1])
            if i1 > i2 :
                card_max = hand[0]
                (odd,best_hand,odd_max) = better_pair(hand[0],occur,street,list_numplayers)
            else:
                card_max = hand[1]
                (odd,best_hand,odd_max) = better_pair(hand[1],occur,street,list_numplayers) 
    return (result,odd,best_hand,odd_max,card_max)

def Three_of_kind_4th(hand,aggressive_prec, aggressive,occur,street,list_numplayers):
    result = False
    num_cards = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
    (odd,best_hand,odd_max,card_max) = (0,[],0,'')
    if aggressive != -1 :
        if hand[0][:-1] == 'T' or hand[0][:-1] == 'J' or hand[0][:-1] == 'Q' or hand[0][:-1] == 'K' or hand[0][:-1] == 'A':
                if hand[0][:-1] == hand[1][:-1]:
                    if aggressive_prec < 2 and aggressive >= 2 :
                        (odd,best_hand,odd_max) = better_three_of_kind(hand[1],occur,street,list_numplayers)
                        card_max = hand[1]
                        result = True
    return (result,odd,best_hand,odd_max,card_max)
# I assume that the player might have the best high card possible if their are no card higher than a 8 
def comparaison_flush(card1,card2,occur):
    shape_card = ['s','h','d','c']
    num_cards = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
    shape_flush = shape_card.index(card1[1:])
    ind1 = num_cards.index(card1[:-1])
    ind2= num_cards.index(card2[:-1])
    if card1[:-1] == 'A' or card2[:-1] == 'A':
        return 'A' +card1[1:]
    elif ind1 >=7 or ind2 >= 7:
        if ind1 > ind2:
            return card1
        else:
            return card2
    for j in range (11):
        if occur[0]== 0 :
            return 'A' + card1[1:]
        elif occur[shape_flush][12-j] == -1:
            if card1[:-1] == num_cards[12-j] or card2[:-1] == num_cards[12-j]:
                return num_cards[12-j] + card1[1:]
        elif occur[shape_flush][12-j] == 0:
            return num_cards[12-j] + card1[1:]
def flush_4th(hand,aggressive,occur,street,list_numplayers):
    result = False
    card_max = ''
    (odd,best_hand,odd_max) = (0,[],0)
    if aggressive != -1 :
        if hand[0][1:] == hand[1][1:]:
            result= True
            card_max = comparaison_flush(hand[0],hand[1],occur)

            (odd,best_hand,odd_max) = better_flush(card_max,occur,street,list_numplayers)
    return (result,odd,best_hand,odd_max,card_max)
#ok� 
def is_straight_flush(best_hand):
    num_cards = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
    royal_flush = ['A','T','J','C','Q','K']
    best_hand_sorted = []
    index = []
    result = False
    for card in best_hand:
        index.append(num_cards.index(card[:-1]))
    index.sort()
    for ind in index:
        best_hand_sorted.append(num_cards[ind])
    if best_hand_sorted == royal_flush:
        result = True
    #if I have a straight then the difference between the highest index and the lowest will be equal to 4
    elif index[0]-index[4] == 4:
        result = True
    return result
def better_flush(card_max_flush,occur,street,list_numplayers):
    card = card_max_flush
    (odd_full,odd_max_full,best_hand_full) = odd_full_house(occur)
    odd = odd_full
    odd_max = odd_max_full
    best_hand = best_hand_full 
    for i in range (4):
        (odd_max_flush,best_hand_flush,odd_flush) = odd_better_Flush(occur, i,street, list_numplayers,card)
        if odd_max_flush > odd_max:
            odd_max = odd_max_flush
            best_hand = best_hand_flush
        odd+=odd_flush
    (odd_four,best_hand_four,odd_max_four) =  odd_better_four_of_kind(occur)
    odd+=odd_four
    if odd_max_four > odd_max:
       best_hand =best_hand_four
       odd_max = odd_max_four
    
    return (odd,best_hand,odd_max)
#look
def better_three_of_kind(card_max_three,occur,street,list_numplayers):
    (odd_full,odd_max_full,best_hand_full) = odd_full_house(occur)
    odd = odd_full
    odd_max = odd_max_full
    best_hand = best_hand_full 
    for i in range (4):
        (odd_max_flush,best_hand_flush,odd_flush) = odd_better_Flush(occur, i,street, list_numplayers,'2s')#we look for all flush because even with a 7 for the higest card it will be the higest hand 
        if odd_max_flush > odd_max:
            odd_max = odd_max_flush
            best_hand = best_hand_flush
        odd+=odd_flush
    (odd_straight,best_hand_straight,odd_max_straight) = odd_better_Straight(occur,street,list_numplayers) 
    odd+=odd_straight
    if odd_max_straight > odd_max:
       best_hand =best_hand_straight
       odd_max = odd_max_straight
    (odd_four,best_hand_four,odd_max_four) =  odd_better_four_of_kind(occur)
    odd+=odd_four
    if odd_max_four > odd_max:
       best_hand =best_hand_four
       odd_max = odd_max_four
    (odd_three,best_hand_three,odd_max_three) =  odd_better_three_of_kind(occur,card_max_three)
    odd+=odd_three
    if odd_max_three > odd_max:
       best_hand =best_hand_three
       odd_max = odd_max_three
    return (odd,best_hand,odd_max)

def better_pair(card,occur,street,list_numplayers):
    (odd_full,odd_max_full,best_hand_full) = odd_full_house(occur)
    odd = odd_full
    odd_max = odd_max_full
    best_hand = best_hand_full
    (odd_four,best_hand_four,odd_max_four) =  odd_better_four_of_kind(occur)
    odd+=odd_four
    if odd_max_four > odd_max:
       best_hand =best_hand_four
       odd_max = odd_max_four
    for i in range (4):
        (odd_max_flush,best_hand_flush,odd_flush) = odd_better_Flush(occur, i,street, list_numplayers,'2s')#we look for all flush because even with a 7 for the higest card it will be the higest hand 
        if odd_max_flush > odd_max:
            odd_max = odd_max_flush
            best_hand = best_hand_flush
        odd+=odd_flush
    (odd_have_two_pairs,best_hand_two_pairs,odd_max_two_pairs) = odd_two_pairs(occur)
    odd+=odd_have_two_pairs
    if odd_max_two_pairs > odd_max:
        best_hand =best_hand_two_pairs
        odd_max = odd_max_two_pairs
    (odd_pair,best_hand_pair,odd_max_pair) =  odd_better_pair(occur,card)
    odd+=odd_pair
    if odd_max_pair > odd_max:
       best_hand =best_hand_pair
       odd_max = odd_max_pair
    (odd_three,best_hand_three,odd_max_three) =  odd_better_three_of_kind(occur,'')
    odd+=odd_three
    if odd_max_three > odd_max:
       best_hand =best_hand_three
       odd_max = odd_max_three
    (odd_straight,best_hand_straight,odd_max_straight) = odd_better_Straight(occur,street,list_numplayers) 
    odd+=odd_straight
    if odd_max_straight > odd_max:
       best_hand =best_hand_straight
       odd_max = odd_max_straight
    return (odd,best_hand,odd_max)
# To do: je dois transformer les r�sultats en une probabilit� d'avoir mieux ( ie; flush -> meilleur flush idem low)
def quiz_4th(tab_player,tab_prec_player,main_player,occur, street, list_numplayers, low_hand_odds):
    player_name = []
    player_possibilities =[]
    possibilities = []
    round2 = 0
    odd = 0.
    best_hand = []
    odd_max = 0.

    odd_low = 0.
    lowest_hand = []
    odd_max_low = 0.
    i_lowest = 13

    num_cards = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
    card_max = ''
    best_opponent_hand = -1
    for player in tab_player:
        aggressive = player[3]
        j = index_poss(player[0],tab_prec_player)
        aggressive_prec = tab_prec_player[j][3]
        if player[0] != main_player:
            if player[0] in player_name:
                '''hand = player[1]
                if round2 == 0:
                    decision.append(player_possibilities)
                    possibilities.append([[odd,best_hand,odd_max],[odd_low,lowest_hand,odd_max_low]])
                    
                    player_possibilities = []
                    odd_low = 0.
                    lowest_hand = []
                    odd_max_low = 0.
                    odd = 0.
                    best_hand = []
                    odd_max = 0.
                    card_max = ''
                    best_opponent_hand = -1
                    round2 +=1
                (result_flush,odd_flush,best_hand_flush,odd_max_flush,card_max_flush)  = flush_4th(hand,aggressive,occur,street,list_numplayers)
                (result_three,odd_three,best_hand_three,odd_max_three,card_max_three) = Three_of_kind_4th(hand,aggressive_prec, aggressive,occur,street,list_numplayers)
                (result_pair,odd_pair,best_hand_pair,odd_max_pair,card_max_pair) = pair_4th(hand,aggressive_prec,aggressive,occur,street,list_numplayers)
                if result_flush:
                    
                    if best_opponent_hand == 4:
                        if num_cards.index(card_max_flush[:-1]) > num_cards.index(card_max[:-1]):
                            (odd,best_hand,odd_max,card_max)=(odd_flush,best_hand_flush,odd_max_flush,card_max_flush)
                    elif best_opponent_hand < 4:
                        best_opponent_hand = 4
                        (odd,best_hand,odd_max,card_max)=(odd_flush,best_hand_flush,odd_max_flush,card_max_flush)
                elif result_three:
                    
                    if best_opponent_hand == 3:
                        if num_cards.index(card_max_three[:-1]) > num_cards.index(card_max[:-1]):
                            (odd,best_hand,odd_max,card_max)=(odd_three,best_hand_three,odd_max_three,card_max_three)
                    elif best_opponent_hand < 3 :
                        best_opponent_hand == 3
                        (odd,best_hand,odd_max,card_max)=(odd_three,best_hand_three,odd_max_three,card_max_three)
                elif result_pair:
                     if best_opponent_hand == 2:
                        if num_cards.index(card_max_pair[:-1]) > num_cards.index(card_max[:-1]):
                            (odd,best_hand,odd_max,card_max)=(odd_three,best_hand_three,odd_max_three,card_max_three)
                     elif best_opponent_hand < 2 :
                        best_opponent_hand == 2
                        (odd,best_hand,odd_max,card_max)=(odd_pair,best_hand_pair,odd_max_pair,card_max_pair)
                else:
                    
                    (odd_low1,lowest_hand1,odd_max1,i_low1) = better_low_hand(low_hand_odds,occur,hand)
                    if i_low1 < i_lowest:
                        odd_low = odd_low1
                        lowest_hand = lowest_hand1
                        odd_max_low = odd_max1'''
            else:
                player_name.append(player[0])
                hand = player[1]
                (result_flush,odd_flush,best_hand_flush,odd_max_flush,card_max_flush)  = flush_4th(hand,aggressive,occur,street,list_numplayers)
                (result_three,odd_three,best_hand_three,odd_max_three,card_max_three) = Three_of_kind_4th(hand,aggressive_prec, aggressive,occur,street,list_numplayers)
                (result_pair,odd_pair,best_hand_pair,odd_max_pair,card_max_pair) = pair_4th(hand,aggressive_prec,aggressive,occur,street,list_numplayers)
                
                if result_flush:
                    
                    if best_opponent_hand == 4:
                        if num_cards.index(card_max_flush[:-1]) > num_cards.index(card_max[:-1]):
                            (odd,best_hand,odd_max,card_max)=(odd_flush,best_hand_flush,odd_max_flush,card_max_flush)
                    elif best_opponent_hand < 4:
                        best_opponent_hand = 4
                        (odd,best_hand,odd_max,card_max)=(odd_flush,best_hand_flush,odd_max_flush,card_max_flush)
                elif result_three:
                    
                    if best_opponent_hand == 3:
                        if num_cards.index(card_max_three[:-1]) > num_cards.index(card_max[:-1]):
                            (odd,best_hand,odd_max,card_max)=(odd_three,best_hand_three,odd_max_three,card_max_three)
                    elif best_opponent_hand < 3 :
                        best_opponent_hand == 3
                        (odd,best_hand,odd_max,card_max)=(odd_three,best_hand_three,odd_max_three,card_max_three)
                elif result_pair:
                    
                    if best_opponent_hand == 2:
                        if num_cards.index(card_max_pair[:-1]) > num_cards.index(card_max[:-1]):
                            (odd,best_hand,odd_max,card_max)=(odd_three,best_hand_three,odd_max_three,card_max_three)
                        elif best_opponent_hand < 2 :
                            best_opponent_hand == 2
                            (odd,best_hand,odd_max,card_max)=(odd_pair,best_hand_pair,odd_max_pair,card_max_pair)
                else:
                    (odd_low1,lowest_hand1,odd_max1,i_low1) = better_low_hand(low_hand_odds,occur,hand)
                    if i_low1 < i_lowest:
                        odd_low = odd_low1
                        lowest_hand = lowest_hand1
                        odd_max_low = odd_max1
    return ([[odd,Card_To_Html(best_hand),odd_max],[odd_low,Card_To_Html(lowest_hand),odd_max_low]])
# 5th Street
def pair_5th(hand,aggresive_prec,aggressive,occur,street,list_numplayers):
    (result,odd,best_hand,odd_max,card_max) = (False,0,[],0,'')
    num_cards = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
    if aggressive != -1 :
        if hand[0][:-1] == 'T' or hand[0][:-1] == 'J' or hand[0][:-1] == 'Q' or hand[0][:-1] == 'K' or hand[0][:-1] == 'A':
            if aggresive_prec >= 2:
                result = True
        elif hand[1][:-1] == 'T' or hand[1][:-1] == 'J' or hand[1][:-1] == 'Q' or hand[1][:-1] == 'K' or hand[1][:-1] == 'A':
            if aggresive_prec >= 2:
                result = True
        elif hand[2][:-1] == 'T' or hand[2][:-1] == 'J' or hand[2][:-1] == 'Q' or hand[2][:-1] == 'K' or hand[2][:-1] == 'A':
            if aggresive_prec >= 2:
                result = True
        if result:
            i1 = num_cards.index(hand[0][:-1])
            i2 = num_cards.index(hand[1][:-1])
            i3 = num_cards.index(hand[2][:-1])
            if i1 > i2 and i1> i3 :
                card_max = hand[0]
                (odd,best_hand,odd_max) = better_pair(hand[0],occur,street,list_numplayers)
            elif i2 > i3 and i2 > i1:
                card_max = hand[1]
                (odd,best_hand,odd_max) = better_pair(hand[1],occur,street,list_numplayers)
            else:
                card_max = hand[2]
                (odd,best_hand,odd_max) = better_pair(hand[2],occur,street,list_numplayers)
    return (result,odd,best_hand,odd_max,card_max)


def Three_of_kind_5th(hand,aggressive_prec, aggressive,occur,street,list_numplayers):
    (result,odd,best_hand,odd_max,card_max) = (False,0,[],0,'')
    if aggressive != -1 :
        if hand[0][:-1] == 'T' or hand[0][:-1] == 'J' or hand[0][:-1] == 'Q' or hand[0][:-1] == 'K' or hand[0][:-1] == 'A':
                if hand[0][:-1] == hand[1][:-1] or hand[0][:-1] == hand[2][:-1] :
                    if aggressive_prec < 2 and aggressive >= 2 :
                        result = True
                        card_max =hand[0]
                        (odd,best_hand,odd_max) = better_three_of_kind(hand[0],occur,street,list_numplayers)
                        return (result,odd,best_hand,odd_max,card_max)
        elif hand[1][:-1] == 'T' or hand[1][:-1] == 'J' or hand[1][:-1] == 'Q' or hand[1][:-1] == 'K' or hand[1][:-1] == 'A':
                if hand[1][:-1] == hand[0][:-1] or hand[1][:-1] == hand[2][:-1]:
                    if aggressive_prec < 2 and aggressive >= 2 :
                        result = True
                        (odd,best_hand,odd_max) = better_three_of_kind(hand[1],occur,street,list_numplayers)
                        card_max = hand[1]
                        return (result,odd,best_hand,odd_max,card_max)
                        
    return (result,odd,best_hand,odd_max,card_max)

def flush_5th(hand,aggressive,occur,street,list_numplayers):
    (result,odd,best_hand,odd_max,card_max) = (False,0,[],0,'')
    if aggressive != -1 :
        if hand[0][1:] == hand[1][1] or hand[0][1] == hand[2][1] or hand[1][1] == hand[2][1:] :
            result = True
            if hand[0][1:] == hand[1][1:]:
                card_max = comparaison_flush(hand[0],hand[1],occur)
                (odd,best_hand,odd_max) = better_flush(card_max,occur,street,list_numplayers)
            elif  hand[0][1:] == hand[2][1:]:
                card_max = comparaison_flush(hand[0],hand[2],occur)
                (odd,best_hand,odd_max) = better_flush(card_max,occur,street,list_numplayers)
            else:
                card_max = comparaison_flush(hand[1],hand[2],occur) 
                (odd,best_hand,odd_max) = better_flush(card_max,occur,street,list_numplayers)
    return (result,odd,best_hand,odd_max,card_max)

def quiz_5th(occur,tab_player,tab_prec_player,main_player,street,list_numplayers ,low_hand_odds):
    player_name = []
    player_possibilities =[]
    possibilities = []
    round2 = 0
    odd = 0.
    best_hand = []
    odd_max = 0.

    odd_low = 0.
    lowest_hand = []
    odd_max_low = 0.
    i_lowest = 13

    num_cards = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
    card_max = ''
    best_opponent_hand = -1
    for player in tab_player:
        aggressive = player[3]
        j = index_poss(player[0],tab_prec_player)
        aggressive_prec = tab_prec_player[j][3]
        if player[0] != main_player:
            if player[0] in player_name:
                '''hand = player[1]
                if round2 == 0:
                    decision.append(player_possibilities)
                    player_possibilities = []
                    possibilities.append((odd,Card_To_Html(best_hand),odd_max))
                    odd = 0.
                    best_hand = []
                    odd_max = 0.
                    odd_low = 0.
                    lowest_hand = []
                    odd_max_low = 0.
                    odd = 0.
                    card_max = ''
                    best_opponent_hand = -1
                    round2 +=1
                (result_flush,odd_flush,best_hand_flush,odd_max_flush,card_max_flush)  = flush_5th(hand,aggressive,occur,street,list_numplayers)
                (result_three,odd_three,best_hand_three,odd_max_three,card_max_three) = Three_of_kind_5th(hand,aggressive_prec, aggressive,occur,street,list_numplayers)
                (result_pair,odd_pair,best_hand_pair,odd_max_pair,card_max_pair) = pair_5th(hand,aggressive_prec,aggressive,occur,street,list_numplayers)
                if result_flush:
                    if best_opponent_hand == 4:
                        if num_cards.index(card_max_flush[:-1]) > num_cards.index(card_max[:-1]):
                            (odd,best_hand,odd_max,card_max)=(odd_flush,best_hand_flush,odd_max_flush,card_max_flush)
                    elif best_opponent_hand < 4:
                        best_opponent_hand = 4
                        (odd,best_hand,odd_max,card_max)=(odd_flush,best_hand_flush,odd_max_flush,card_max_flush)
                elif result_three:
                    if best_opponent_hand == 3:
                        if num_cards.index(card_max_three[:-1]) > num_cards.index(card_max[:-1]):
                            (odd,best_hand,odd_max,card_max)=(odd_three,best_hand_three,odd_max_three,card_max_three)
                    elif best_opponent_hand < 3 :
                        best_opponent_hand == 3
                        (odd,best_hand,odd_max,card_max)=(odd_three,best_hand_three,odd_max_three,card_max_three)
                elif result_pair:
                     if best_opponent_hand == 2:
                        if num_cards.index(card_max_pair[:-1]) > num_cards.index(card_max[:-1]):
                            (odd,best_hand,odd_max,card_max)=(odd_three,best_hand_three,odd_max_three,card_max_three)
                     elif best_opponent_hand < 2 :
                        best_opponent_hand == 2
                        (odd,best_hand,odd_max,card_max)=(odd_pair,best_hand_pair,odd_max_pair,card_max_pair)
                else:
                    (odd_low1,lowest_hand1,odd_max1,i_low1) = better_low_hand(low_hand_odds,occur,hand)
                    if i_low1 < i_lowest:
                        odd_low = odd_low1
                        lowest_hand = lowest_hand1
                        odd_max_low = odd_max1'''
            else:
                player_name.append(player[0])
                hand = player[1]
                (result_flush,odd_flush,best_hand_flush,odd_max_flush,card_max_flush)  = flush_5th(hand,aggressive,occur,street,list_numplayers)
                (result_three,odd_three,best_hand_three,odd_max_three,card_max_three) = Three_of_kind_5th(hand,aggressive_prec, aggressive,occur,street,list_numplayers)
                (result_pair,odd_pair,best_hand_pair,odd_max_pair,card_max_pair) = pair_5th(hand,aggressive_prec,aggressive,occur,street,list_numplayers)
                if result_flush:
                    if best_opponent_hand == 4:
                        if num_cards.index(card_max_flush[:-1]) > num_cards.index(card_max[:-1]):
                            (odd,best_hand,odd_max,card_max)=(odd_flush,best_hand_flush,odd_max_flush,card_max_flush)
                    elif best_opponent_hand < 4:
                        best_opponent_hand = 4
                        (odd,best_hand,odd_max,card_max)=(odd_flush,best_hand_flush,odd_max_flush,card_max_flush)
                elif result_three:
                    if best_opponent_hand == 3:
                        if num_cards.index(card_max_three[:-1]) > num_cards.index(card_max[:-1]):
                            (odd,best_hand,odd_max,card_max)=(odd_three,best_hand_three,odd_max_three,card_max_three)
                    elif best_opponent_hand < 3 :
                        best_opponent_hand == 3
                        (odd,best_hand,odd_max,card_max)=(odd_three,best_hand_three,odd_max_three,card_max_three)
                elif result_pair:
                     if best_opponent_hand == 2:
                        if num_cards.index(card_max_pair[:-1]) > num_cards.index(card_max[:-1]):
                            (odd,best_hand,odd_max,card_max)=(odd_three,best_hand_three,odd_max_three,card_max_three)
                     elif best_opponent_hand < 2 :
                        best_opponent_hand == 2
                        (odd,best_hand,odd_max,card_max)=(odd_pair,best_hand_pair,odd_max_pair,card_max_pair)
                else:
                    (odd_low1,lowest_hand1,odd_max1,i_low1) = better_low_hand(low_hand_odds,occur,hand)
                    if i_low1 < i_lowest:
                        odd_low = odd_low1
                        lowest_hand = lowest_hand1
                        odd_max_low = odd_max1
    return ([[odd,Card_To_Html(best_hand),odd_max],[odd_low,Card_To_Html(lowest_hand),odd_max_low]])


def odds_better_hand(occur):
    odd = 0
    row = -1
    column = -1
    row1 = -1
    column1= -1
    for i in range (0,3):
        for j in range(13,16):
            if occur[i][j] == 1:
                row1 = i
                column1 = j
    for i in range (4,7):
        for j in range(0,13):
            if occur[i][j] == 1:
                row = i
                column = j
    # The player don't have any high hand
    if row == -1 and row1 == -1 and column == -1 and column1 == -1:
        count = 0
        for i in range (0,3):
            for j in range(14,16):
                odd += occur[i][j]
                count +=1
        for i in range (4,7):
            for j in range(0,12):
                odd += occur[i][j]
                count +=1
        odd += occur[13][0]
        count +=1
        odd/=count
    # The player have a pair a three of kind or a four of kind
    elif row != -1  and column != -1 and row1 == -1 and column1 == -1:
        #has a pair
        if row  == 4:
            count = 0
            for j in range(0,13):
                if j!=column:
                    odd += occur[4][j]
                    count +=1
            for i in range (0,3):
                for j in range(14,16):
                    odd += occur[i][j]
                    count +=1
            for i in range (5,7):
                for j in range(0,12):
                    odd += occur[i][j]
                    count +=1
            odd += occur[13][0]
            count +=1
            odd/=count
        #has a three of kind 
        elif row == 5:
            count = 0
            for j in range(column,13):
                odd += occur[5][j]
                count +=1
            for i in range (0,3):
                for j in range(14,16):
                    odd += occur[i][j]
                    count +=1
            for j in range(0,12):
                odd += occur[6][j]
                count +=1
            odd += occur[13][0]
            count +=1
            odd/=count
        #has a four of kind
        else:
            odd = 0
    elif row1 != -1 and column1 != -1:
        #has a straight
        if column1  == 13:
            #if he has a straight the only hand that is higher is a straight flush or a better straight (not done )
            odd = occur[0][15]+occur[1][15]+occur[2][15]+occur[3][15]
            odd/=4
        #has a flush 
        
        elif row == 5:
            #if he has a flush the only hand that is higher is a straight flush or a better flush(higher card) (not done )
            odd = occur[0][15]+occur[1][15]+occur[2][15]+occur[3][15]
            odd/=4
        #has a straight flush
        else:
            odd = 0
    return odd


 
# 3rd Street
def hand(occur):
    x = 0
    y = -1
    index_low = 0
    index_high = -1
    for j in range(0,len(occur[0])-3):
        for i in range(0,len(occur)-3):
            if occur[i][j] == 1 and index_low < j:
                index_low = j
            if occur[i][j] == -1 and (index_high == -1 or index_high !=0):
                index_high = j
    for i in range(0,len(occur)-3):
        for j in range(0,8):
            if occur[i][j] == -1 and index_low > j:
                x = -1
    for j in range(0,len(occur[0])-3):
        if occur[4][j] == 1 and j>8 and (index_high <= j or index_high != 0) :
            y = 0
        if occur[5][j] == 1 and (index_high <= j or index_high != 0) :
            y = 0
    return [x,y]
def pair_suited_ace(occur):
    result = False
    j = 0
    while j < 13 and not(result):
        if occur[4][j] == 1:
            if (occur[3][j]== 1 and occur[3][0]) or (occur[2][j]== 1 and occur[2][0]) or (occur[1][j]== 1 and occur[1][0]) or (occur[0][j]== 1 and occur[0][0]):
                result = True
        j+=1
def good_hand(occur):
    action = ""
    z=0
    for i in range(0,4):
        if (occur[i][13]>0.11 or occur[i][14] > 0.2) or pair_suited_ace(occur):
            action = 0
        else:
            action = -1 
    return action
def third_street_decision(occur):
    [x,y] = hand(occur)
    if x == 0:
        return 0
    elif y == 0:
        return 0
    elif x == -1 and y == -1:
        return good_hand(occur)
        