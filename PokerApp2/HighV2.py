
def find_current_hand(occur):
    suits = ['s','h','d','c']
    ranks = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
    current_hand = []
    for i in range (4):
        for j in range(13):
            if occur[i][j] == 1:
                current_hand.append(ranks[j] + suits[i])
    return current_hand
def Suitedness(current_hand):
    suited = [0,0,0,0]
    suits = ['s','h','d','c']
    for card in current_hand:
        suit = card[1:]
        suited[suits.index(suit)] = suited[suits.index(suit)] + 1
    number_of_suits = 0
    for nbre in suited:
        if nbre !=0:
            number_of_suits += 1
    if len(current_hand) == 3:
        if number_of_suits == 3:
            return "rainbow"
        elif number_of_suits == 2:
            return "2suited"
        else:
            return "mono"
    '''
    elif len(suit_hand) == 4:
        if number_of_suits == 4:
            return "rainbow"
        elif number_of_suits == 3:
            return "2suited"
        elif number_of_suits == 2:
            return "2suited"
        else:
            return "mono"
    elif len(suit_hand) == 5:
        if number_of_suits == 4:
            return "rainbow"
        elif number_of_suits == 3:
            return "2suited"
        elif number_of_suits == 2:
            return "2suited"
        else:
            return "mono"
    elif len(suit_hand) == 6:
        if number_of_suits == 4:
            return "rainbow"
        elif number_of_suits == 3:
            return "2suited"
        elif number_of_suits == 2:
            return "2suited"
        else:
            return "mono"'''

def count_cards_remaining_by_rank(occur):
    remaining_cards_ranks = []
    sum_cards=0
    for j in range (13):
        sum_cards = 0
        for i in range (4):
            if occur[i][j] ==0:
                sum_cards+=1
            remaining_cards_ranks.append(sum_cards)
    return remaining_cards_ranks
def count_cards_remaining_by_suit(occur):
    remaining_cards_suit = []
    sum_cards=0
    for i in range (4):
        sum_cards = 0
        for j in range (13):
            if occur[i][j] == 0:
                sum_cards+=1
            remaining_cards_suit.append(sum_cards)
    return remaining_cards_suit
def count_dead_cards_by_rank(occur):
    dead_cards_ranks = []
    sum_cards=0
    for j in range (13):
        sum_cards = 0
        for i in range (4):
            if occur[i][j] == -1:
                sum_cards+=1
            dead_cards_ranks.append(sum_cards)
    return dead_cards_ranks
def generate_all_remaining_hand(current_hand,remaining_cards_ranks):
    ranks = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
    all_possible_hand = []
    hand = []
    if len(current_hand) == 3:# 4 cards are remaining
        i=0
        j=0
        k=0
        l=0
        
        while i < 13:
            card1 = ranks[i]
            j=i
            while j < 13:
                card2 = ranks[j]
                k=j
                while k < 13:
                    card3 = ranks[k]
                    l=k
                    while l < 13:
                        card4 = ranks[l]
                        hand = [card1,card2,card3,card4]
                        count_rank_all_hand = [0,0,0,0,0,0,0,0,0,0,0,0,0]
                        count_rank_possible_hand = [0,0,0,0,0,0,0,0,0,0,0,0,0]
                        count_rank_current_hand = [0,0,0,0,0,0,0,0,0,0,0,0,0]
                        if hand.count(card1) <= remaining_cards_ranks[i] and hand.count(card2) <= remaining_cards_ranks[j] and hand.count(card3) <= remaining_cards_ranks[k] and hand.count(card4) <= remaining_cards_ranks[l]:
                            for card in current_hand:
                                count_rank_all_hand[ranks.index(card[:-1])] = count_rank_all_hand[ranks.index(card[:-1])] + 1
                                count_rank_current_hand[ranks.index(card[:-1])] = count_rank_current_hand[ranks.index(card[:-1])] + 1
                            for card in hand:
                                count_rank_possible_hand[ranks.index(card)] = count_rank_possible_hand[ranks.index(card)] + 1
                                count_rank_all_hand[ranks.index(card)] = count_rank_all_hand[ranks.index(card)] + 1
                            if card1 == card2 and card2 == card3 and card3 == card4  and card1 == card4:
                                all_possible_hand.append([hand,1,count_rank_current_hand,count_rank_possible_hand,count_rank_all_hand])
                            elif card1 != card2 and card1 != card3 and card2 != card3 and card1!=card4 and card2!=card4 and card3!=card4 :
                                all_possible_hand.append([hand,24,count_rank_current_hand,count_rank_possible_hand,count_rank_all_hand])
                            elif (card1 == card2 and card2 == card3 and card1 != card4) or (card1 == card2 and card2 == card4 and card1 != card3) or (card1 == card3 and card3 == card4 and card1 != card2)  or (card2 == card3 and card3 == card4 and card1 != card2):
                                all_possible_hand.append([hand,4,count_rank_current_hand,count_rank_possible_hand,count_rank_all_hand])
                            elif (card1 == card2 and card3 == card4) or (card1 == card3 and card2 == card4) or (card1 == card4 and card3 == card2):
                                all_possible_hand.append([hand,6,count_rank_current_hand,count_rank_possible_hand,count_rank_all_hand])   
                            else:
                                all_possible_hand.append([hand,12,count_rank_current_hand,count_rank_possible_hand,count_rank_all_hand])
                            
                        l+=1
                    k+=1
                j+=1
            i+=1
    elif len(current_hand) == 4:# 3 cards are remaining
        i=0
        j=0
        k=0
        while i < 13:
            card1 = ranks[i]
            j = i
            while j < 13:
                card2 = ranks[j]
                k = j
                while k < 13:
                    card3 = ranks[k]
                    hand = [card1,card2,card3]
                    count_rank_all_hand = [0,0,0,0,0,0,0,0,0,0,0,0,0]
                    count_rank_possible_hand = [0,0,0,0,0,0,0,0,0,0,0,0,0]
                    count_rank_current_hand = [0,0,0,0,0,0,0,0,0,0,0,0,0]
                    if hand.count(card1) <= remaining_cards_ranks[i] and hand.count(card2) <= remaining_cards_ranks[j] and hand.count(card3) <= remaining_cards_ranks[k]:
                        for card in current_hand:
                            count_rank_all_hand[ranks.index(card[:-1])] = count_rank_all_hand[ranks.index(card[:-1])] + 1
                            count_rank_current_hand[ranks.index(card[:-1])] = count_rank_current_hand[ranks.index(card[:-1])] + 1
                        for card in hand:
                            count_rank_possible_hand[ranks.index(card)] = count_rank_possible_hand[ranks.index(card)] + 1
                            count_rank_all_hand[ranks.index(card)] = count_rank_all_hand[ranks.index(card)] + 1
                        if card1 == card2 and card2 == card3:

                            all_possible_hand.append([hand,1,count_rank_current_hand,count_rank_possible_hand,count_rank_all_hand])
                        elif card1 != card2 and card1 != card3 and card2 != card3:
                            all_possible_hand.append([hand,6,count_rank_current_hand,count_rank_possible_hand,count_rank_all_hand])
                        else:
                            all_possible_hand.append([hand,3,count_rank_current_hand,count_rank_possible_hand,count_rank_all_hand])
                    k+=1
                j+=1
            i=1
    elif len(current_hand) == 5:# 2 cards are remaining
        i=0
        j=0
        while i < 13:
            card1 = ranks[i]
            j=i
            while j < 13:
                card2 = ranks[j]
                hand = [card1,card2]
                count_rank_all_hand = [0,0,0,0,0,0,0,0,0,0,0,0,0]
                count_rank_possible_hand = [0,0,0,0,0,0,0,0,0,0,0,0,0]
                count_rank_current_hand = [0,0,0,0,0,0,0,0,0,0,0,0,0]
                if hand.count(card1) <= remaining_cards_ranks[i] and hand.count(card2) <= remaining_cards_ranks[j]:
                    for card in current_hand:
                            count_rank_all_hand[ranks.index(card[:-1])] = count_rank_all_hand[ranks.index(card[:-1])] + 1
                            count_rank_current_hand[ranks.index(card[:-1])] = count_rank_current_hand[ranks.index(card[:-1])] + 1
                    for card in hand:
                        count_rank_possible_hand[ranks.index(card)] = count_rank_possible_hand[ranks.index(card)] + 1
                        count_rank_all_hand[ranks.index(card)] = count_rank_all_hand[ranks.index(card)] + 1
                    if card1 == card2:
                        all_possible_hand.append([hand,1,count_rank_current_hand,count_rank_possible_hand,count_rank_all_hand])
                    else:
                        all_possible_hand.append([hand,2,count_rank_current_hand,count_rank_possible_hand,count_rank_all_hand])
                j+=1
            i=1
    elif len(current_hand) == 6:# 1 card is remaining
        i=0
        while i < 13:
            card1 = ranks[i]
            hand = [card1]
            count_rank_all_hand = [0,0,0,0,0,0,0,0,0,0,0,0,0]
            count_rank_possible_hand = [0,0,0,0,0,0,0,0,0,0,0,0,0]
            count_rank_current_hand = [0,0,0,0,0,0,0,0,0,0,0,0,0]
            if hand.count(card1) <= remaining_cards_ranks[i]:
                for card in current_hand:
                    count_rank_all_hand[ranks.index(card[:-1])] = count_rank_all_hand[ranks.index(card[:-1])] + 1
                    count_rank_current_hand[ranks.index(card[:-1])] = count_rank_current_hand[ranks.index(card[:-1])] + 1
                for card in hand:
                    count_rank_possible_hand[ranks.index(card)] = count_rank_possible_hand[ranks.index(card)] + 1
                    count_rank_all_hand[ranks.index(card)] = count_rank_all_hand[ranks.index(card)] + 1
            all_possible_hand.append([hand,1,count_rank_current_hand,count_rank_possible_hand,count_rank_all_hand])
            i=1
    return all_possible_hand


def possible_flush(current_hand,all_possible_hand):
    lst = []
    for [hand,combinaisons,count_rank_current_hand,count_rank_possible_hand,count_rank_all_hand] in all_possible_hand:
        distinct_rank = 0
        distinct_rank_possible_hand = 0
        distinct_rank_current_hand = 0
        for i in range (13):
                if count_rank_possible_hand[i] !=0:
                    distinct_rank_possible_hand +=1
                    distinct_rank +=1
                if count_rank_possible_hand[i] !=0:
                    distinct_rank_current_hand +=1
                    distinct_rank +=1
        if Suitedness(current_hand) == "rainbow":
            
            if distinct_rank_possible_hand  == 4:
                lst.append([hand,combinaisons,count_rank_current_hand,count_rank_possible_hand,count_rank_all_hand,True])
            else:
                lst.append([hand,combinaisons,count_rank_current_hand,count_rank_possible_hand,count_rank_all_hand,False])
        elif Suitedness(current_hand) == "mono":
            if distinct_rank_possible_hand  > 2 and distinct_rank > 4:
                lst.append([hand,combinaisons,count_rank_current_hand,count_rank_possible_hand,count_rank_all_hand,True])
            else:
                lst.append([hand,combinaisons,count_rank_current_hand,count_rank_possible_hand,count_rank_all_hand,False])
        else:
            if (distinct_rank_current_hand >= 2 and distinct_rank > 4 and distinct_rank_possible_hand  > 2):
                lst.append([hand,combinaisons,count_rank_current_hand,count_rank_possible_hand,count_rank_all_hand,True])
            else:
                lst.append([hand,combinaisons,count_rank_current_hand,count_rank_possible_hand,count_rank_all_hand,False])
    return lst
def all_prob(occur,street,list_numplayers):
        prob_royal_flush,rf_zero =0,1
        prob_straight_flush,sf_zero=0,1
        prob_four_of_Kind,fok_zero=0,1
        prob_full_house,fh_zero = 0,1
        prob_flush,f_zero=0,1
        prob_straight,s_zero = 0,1
        prob_three_of_kind,tok_zero = 0,1
        prob_two_pairs,tp_zero = 0,1
        prob_pair,p_zero = 0,1
        prob_high_card,h_zero = 0,1
        all_comb = 0
        if street == '4th':
            current_hand = find_current_hand(occur)
            lst_all_possibilities = possible_flush(current_hand,generate_all_remaining_hand(current_hand,count_cards_remaining_by_rank(occur)))
            for possibility in lst_all_possibilities: #[hand,combinaisons,count_rank_current_hand,count_rank_possible_hand,count_rank_all_hand,Bool]
                comb = possibility[1]
                all_comb+= comb
                prob_Royal_flush_hand = 0
                if prob_Royal_flush_hand ==0:
                    prob_straight_flush_hand = 0
                    if prob_straight_flush_hand == 0:
                        lst_rank = possibility[4]
                        prob_4kind_hand = probability_4Kind(lst_rank)
                        if prob_4kind_hand == 0:
                            prob_full_house_hand = probability_Full_House(lst_rank)
                            if prob_full_house_hand == 0:
                                prob_flush_hand = probability_flush_given_hand(current_hand,possibility,occur,count_cards_remaining_by_rank(occur),list_numplayers)/comb
                                prob_flush_given_hand = prob_flush_hand 
                                lst_straight = have_straigth(lst_rank)
                                prob_straight_hand = probability_straight(lst_straight,prob_flush_given_hand)
                                if prob_straight_hand == 0:
                                    prob_3kind_hand = probability_3KIND(lst_rank,prob_flush_given_hand)
                                    if prob_3kind_hand == 0:
                                        prob_2pairs_hand = probability_2PAIRS(lst_rank,prob_flush_given_hand)
                                        if prob_2pairs_hand == 0:
                                            prob_pair_hand = probability_PAIR(lst_rank,prob_flush_given_hand)
                                            if prob_pair_hand == 0:
                                                prob_high_card_hand = probability_high_card(lst_rank,prob_flush_given_hand)
                                                prob_high_card +=prob_high_card_hand * comb
                                                prob_flush += prob_flush_hand * comb
                                            else:
                                                prob_pair +=prob_pair_hand * comb
                                                prob_flush += prob_flush_hand *comb
                                        else:
                                            prob_two_pairs +=prob_2pairs_hand * comb
                                            prob_flush += prob_flush_hand * comb
                                    else:
                                        prob_three_of_kind += prob_3kind_hand * comb
                                        prob_flush += prob_flush_hand * comb
                                else:
                                    prob_straight +=prob_straight_hand * comb 
                                    prob_flush += prob_flush_hand * comb
                                    
                            else:
                                prob_full_house += prob_full_house_hand * comb 
                        else:
                            prob_four_of_Kind += comb  * prob_4kind_hand
                    else:
                        prob_straight_flush += comb  * prob_straight_flush_hand
                else:
                    prob_royal_flush += comb  * prob_Royal_flush_hand
            prob_royal_flush/=all_comb 
            prob_straight_flush/=all_comb       
            prob_four_of_Kind/=all_comb    
            prob_full_house/=all_comb
            prob_flush/=all_comb
            prob_straight/=all_comb
            prob_three_of_kind/=all_comb
            prob_two_pairs/=all_comb
            prob_pair/=all_comb
            prob_high_card/=all_comb
        return [['Royal Flush',prob_royal_flush,rf_zero],
                ['Straight Flush',prob_straight_flush,sf_zero],
                ['Four of Kind',prob_four_of_Kind,fok_zero],
                ['Full House',prob_full_house,fh_zero],
                ['Flush',prob_flush,f_zero],
                ['Straight',prob_straight,s_zero],
                ['Three of Kind',prob_three_of_kind,tok_zero],
                ['Two Pairs',prob_two_pairs,tp_zero],
                ["Pair",prob_pair,p_zero],
                ["High_card",prob_high_card,h_zero],
                ["Total",prob_royal_flush+prob_straight_flush+prob_four_of_Kind+prob_full_house+prob_high_card+prob_flush+prob_straight+prob_three_of_kind+prob_two_pairs+prob_pair,1]]


def have_straigth(lst_rank):
    lst_straight = [0 for i in range (13)]
    if lst_rank[0]*lst_rank[9]*lst_rank[10]*lst_rank[11]*lst_rank[12] !=0:
       lst_straight[0] = 1
    for i in range (8,-1,-1):
        if lst_rank[i]*lst_rank[i+1]*lst_rank[i+2]*lst_rank[i+3]*lst_rank[i+4] !=0:
            lst_straight[i+4] = 1

    return lst_straight
def probability_straight(lst_straight,prob_flush):
    for have_str in lst_straight:
        if have_str == 1 :
            return 1 - prob_flush
    return 0
def probability_4Kind(lst_rank):
    for nber_rank in lst_rank:
        if nber_rank  ==  4:
            return 1
    return 0

    
def probability_Full_House(lst_rank):
    index_3KIND =-1
    for i in range (13):
        if lst_rank[i]  ==  3:
            if index_3KIND != -1:
                return 1
            else:
                index_3KIND = i
    if index_3KIND == -1:
                return 0
    else:    
        for j in range (13):
            if (lst_rank[j]  ==  2 or lst_rank[j]  ==  3) and j != index_3KIND:
                if index_3KIND != -1:
                    return 1
        return 0
'''print(possible_flush(['Ac','2c','Kc'],generate_all_remaining_hand(['Ac','2c','Kc'],[3,3,4,4,4,4,4,4,4,4,4,4,3])))'''
def probability_3KIND(lst_rank,prob_flush):
    for i in range (13):
        if lst_rank[i]  ==  3:
                return 1-prob_flush
    return 0
def probability_2PAIRS(lst_rank,prob_flush):
    index_first_pair =-1
    for i in range (13):
        if lst_rank[i]  ==  2:
            if index_first_pair != -1:
                return 1 - prob_flush
            else:
                index_first_pair = i
    return 0
def probability_PAIR(lst_rank,prob_flush):
    for i in range (13):
        if lst_rank[i]  ==  2:
            return 1 - prob_flush
    return 0
def probability_high_card(lst_rank,prob_flush):
    lst_str = have_straigth(lst_rank)
    Sum_straight  = 0
    Distinct_rank = 0
    for str in lst_str:
        Sum_straight += str
    for nber_rank in lst_rank:
        if nber_rank != 0 :
            Distinct_rank +=1
    if Sum_straight == 0 and Distinct_rank == 7:
        return 1 - prob_flush
    return 0

def probability_flush_given_hand(current_hand,possible_hand,occur,remaining_cards_ranks,list_numplayers):
    suits = ['s','h','d','c']
    ranks = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
    probability = 1
    count_card = 0
    list_remaining_card =[]
    lst_remaining_card = count_cards_remaining_by_rank(occur)
    if len(current_hand) == 3 :
        if possible_hand[5]:
            if Suitedness(current_hand) == 'rainbow':
                for card in possible_hand[0]:
                    count_card = 0
                    for i in range(4):
                        if occur[i][ranks.index(card)] == 0:
                            count_card+=1
                        list_remaining_card.append(count_card)
                suit1 = current_hand[0][1:]
                suit2 = current_hand[1][1:]
                suit3 = current_hand[2][1:]
                card_needed = 4
                probability_possible_hand = probability_4cards(current_hand,possible_hand,occur,remaining_cards_ranks,list_numplayers)
                probability_possible_hand_suit1= probability_4cards_flush(suit1,card_needed,current_hand,possible_hand,occur,remaining_cards_ranks,list_numplayers)
                probability_possible_hand_suit2= probability_4cards_flush(suit2,card_needed,current_hand,possible_hand,occur,remaining_cards_ranks,list_numplayers)
                probability_possible_hand_suit3= probability_4cards_flush(suit3,card_needed,current_hand,possible_hand,occur,remaining_cards_ranks,list_numplayers)
                if probability_possible_hand == 0:
                    return 0
                else:
                    probability = (probability_possible_hand_suit1+probability_possible_hand_suit2+probability_possible_hand_suit3)/(probability_possible_hand)
                    return probability 
            elif Suitedness(current_hand) == 'mono':
                for card in possible_hand[0]:
                    count_card = 0
                    for i in range(4):
                        if occur[i][ranks.index(card)] == 0:
                            count_card+=1
                        list_remaining_card.append(count_card)
                suit = current_hand[0][1:]
                card_needed = 2
                probability_possible_hand = probability_4cards(current_hand,possible_hand,occur,remaining_cards_ranks,list_numplayers)
                probability_possible_hand_suit= probability_4cards_flush(suit,card_needed,current_hand,possible_hand,occur,remaining_cards_ranks,list_numplayers)
    
                if probability_possible_hand == 0:
                    return 0
                else:
                    probability = (probability_possible_hand_suit)/(probability_possible_hand)
                    return probability 
            else:
                
                for card in possible_hand[0]:
                    count_card = 0
                    for i in range(4):
                        if occur[i][ranks.index(card)] == 0:
                            count_card+=1
                        list_remaining_card.append(count_card)
                suit1 = current_hand[0][1:]
                if suit1 == current_hand[1][1:]:
                    
                    suit2 = current_hand[2][1:]
                    card_needed_suit1 = 3
                    card_needed_suit2 = 4
                else:
                   
                    suit2 = current_hand[1][1:]
                    if  current_hand[2][1:] == suit2 :
                        card_needed_suit1 = 4
                        card_needed_suit2 = 3
                    else:
                        card_needed_suit1 = 3
                        card_needed_suit2 = 4
                probability_possible_hand = probability_4cards(current_hand,possible_hand,occur,remaining_cards_ranks,list_numplayers)
                print(current_hand,probability_possible_hand)
                probability_possible_hand_suit1= probability_4cards_flush(suit1,card_needed_suit1,current_hand,possible_hand,occur,remaining_cards_ranks,list_numplayers)
                probability_possible_hand_suit2= probability_4cards_flush(suit2,card_needed_suit2,current_hand,possible_hand,occur,remaining_cards_ranks,list_numplayers)
                print(suit2,probability_possible_hand_suit2)
                print(suit1,probability_possible_hand_suit1)
                if probability_possible_hand == 0:
                    return 0
                else:
                    probability = (probability_possible_hand_suit1+probability_possible_hand_suit2)/(probability_possible_hand)
                    return probability
        else:
            return 0
    else:
        return 0
                

def probability_4cards(current_hand,possible_hand,occur,remaining_cards_ranks,list_numplayers):
    ranks = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
    num3 = list_numplayers[0]
    distinct_rank = 0
    permutations = ((52-(2 + num3)))*((51-(2 + num3)))*((50-(2 + num3)))*((49-(2 + num3)))
    permutations_cards = 0
    remaining_card1 = 0
    remaining_card2= 0
    remaining_card3= 0
    remaining_card4= 0
    for count_rank in possible_hand[3]:
        if count_rank != 0:
            distinct_rank += 1
    if distinct_rank == 4:
        remaining_card1 = remaining_cards_ranks[ranks.index(possible_hand[0][0])]
        remaining_card2= remaining_cards_ranks[ranks.index(possible_hand[0][1])]
        remaining_card3= remaining_cards_ranks[ranks.index(possible_hand[0][2])]
        remaining_card4= remaining_cards_ranks[ranks.index(possible_hand[0][3])]
        if remaining_card4==0 or remaining_card3 == 0 or remaining_card2==0 or remaining_card1 == 0:
            permutations_cards += 0
        else:
            permutations_cards = (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
        return permutations_cards/permutations
    elif distinct_rank == 3:
        if possible_hand[0][0] == possible_hand[0][1] :
            remaining_card1 = remaining_cards_ranks[ranks.index(possible_hand[0][0])]
            remaining_card2= remaining_card1-1
            remaining_card3= remaining_cards_ranks[ranks.index(possible_hand[0][2])]
            remaining_card4= remaining_cards_ranks[ranks.index(possible_hand[0][3])]
            if remaining_card4==0 or remaining_card3 == 0 or remaining_card2==0 or remaining_card1 == 0:
                permutations_cards += 0
            else:
                permutations_cards = (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
        
        elif possible_hand[0][0] == possible_hand[0][2] :
            remaining_card1 = remaining_cards_ranks[ranks.index(possible_hand[0][0])]
            remaining_card2= remaining_cards_ranks[ranks.index(possible_hand[0][1])]
            remaining_card3= remaining_card1-1
            remaining_card4= remaining_cards_ranks[ranks.index(possible_hand[0][3])]
            if remaining_card4==0 or remaining_card3 == 0 or remaining_card2==0 or remaining_card1 == 0:
                permutations_cards += 0
            else:
                permutations_cards = (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
        
        elif possible_hand[0][0] == possible_hand[0][3] :
            remaining_card1 = remaining_cards_ranks[ranks.index(possible_hand[0][0])]
            remaining_card2 = remaining_cards_ranks[ranks.index(possible_hand[0][1])]
            remaining_card3 = remaining_cards_ranks[ranks.index(possible_hand[0][2])]
            remaining_card4 = remaining_card1 - 1
            if remaining_card4==0 or remaining_card3 == 0 or remaining_card2==0 or remaining_card1 == 0:
                permutations_cards += 0
            else:
                permutations_cards = (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
        
        elif possible_hand[0][1] == possible_hand[0][2] :
            remaining_card1 = remaining_cards_ranks[ranks.index(possible_hand[0][0])]
            remaining_card2 = remaining_cards_ranks[ranks.index(possible_hand[0][1])]
            remaining_card3 = remaining_card2 -1
            remaining_card4 = remaining_cards_ranks[ranks.index(possible_hand[0][3])]
            if remaining_card4==0 or remaining_card3 == 0 or remaining_card2==0 or remaining_card1 == 0:
                permutations_cards += 0
            else:
                permutations_cards = (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
        
        elif possible_hand[0][1] == possible_hand[0][3] :
            remaining_card1 = remaining_cards_ranks[ranks.index(possible_hand[0][0])]
            remaining_card2 = remaining_cards_ranks[ranks.index(possible_hand[0][1])]
            remaining_card3 = remaining_cards_ranks[ranks.index(possible_hand[0][2])]
            remaining_card4 = remaining_card2 -1
            if remaining_card4==0 or remaining_card3 == 0 or remaining_card2==0 or remaining_card1 == 0:
                permutations_cards += 0
            else:
                permutations_cards = (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
        
        elif possible_hand[0][2] == possible_hand[0][3] :
            remaining_card1 = remaining_cards_ranks[ranks.index(possible_hand[0][0])]
            remaining_card2 = remaining_cards_ranks[ranks.index(possible_hand[0][1])]
            remaining_card3 = remaining_cards_ranks[ranks.index(possible_hand[0][2])]
            remaining_card4 = remaining_card3 -1
            if remaining_card4==0 or remaining_card3 == 0 or remaining_card2==0 or remaining_card1 == 0:
                permutations_cards += 0
            else:
                permutations_cards = (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
        return permutations_cards/permutations
    elif distinct_rank == 2:
        if possible_hand[0][0] == possible_hand[0][1] and possible_hand[0][2] == possible_hand[0][3] :
            remaining_card1 = remaining_cards_ranks[ranks.index(possible_hand[0][0])]
            remaining_card2= remaining_card1-1
            remaining_card3= remaining_cards_ranks[ranks.index(possible_hand[0][2])]
            remaining_card4= remaining_card3 -1
            if remaining_card4==0 or remaining_card3 == 0 or remaining_card2==0 or remaining_card1 == 0:
                permutations_cards = 0
            else:
                permutations_cards = (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
        
        elif possible_hand[0][0] == possible_hand[0][2] and possible_hand[0][1] == possible_hand[0][3] :
            remaining_card1 = remaining_cards_ranks[ranks.index(possible_hand[0][0])]
            remaining_card2= remaining_cards_ranks[ranks.index(possible_hand[0][1])]
            remaining_card3= remaining_card1-1
            remaining_card4= remaining_card2 -1
            if remaining_card4==0 or remaining_card3 == 0 or remaining_card2==0 or remaining_card1 == 0:
                permutations_cards = 0
            else:
                permutations_cards = (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
        
        elif possible_hand[0][0] == possible_hand[0][1] and possible_hand[0][1] == possible_hand[0][2] :
            remaining_card1 = remaining_cards_ranks[ranks.index(possible_hand[0][0])]
            remaining_card2 = remaining_card1 - 1
            remaining_card3 = remaining_card1 - 2
            remaining_card4 =  remaining_cards_ranks[ranks.index(possible_hand[0][3])]
            if remaining_card4==0 or remaining_card3 == 0 or remaining_card2==0 or remaining_card1 == 0:
                permutations_cards = 0
            else:
                permutations_cards = (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
        
        elif possible_hand[0][0] == possible_hand[0][1] and possible_hand[0][1] == possible_hand[0][3] :
            remaining_card1 = remaining_cards_ranks[ranks.index(possible_hand[0][0])]
            remaining_card2 = remaining_card1-1
            remaining_card3 = remaining_cards_ranks[ranks.index(possible_hand[0][2])]
            remaining_card4 = remaining_card1-2
            if remaining_card4==0 or remaining_card3 == 0 or remaining_card2==0 or remaining_card1 == 0:
                permutations_cards = 0
            else:
                permutations_cards = (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
        
        elif possible_hand[0][0] == possible_hand[0][2] and possible_hand[0][2] == possible_hand[0][3]  :
            remaining_card1 = remaining_cards_ranks[ranks.index(possible_hand[0][0])]
            remaining_card2 = remaining_cards_ranks[ranks.index(possible_hand[0][1])]
            remaining_card3 = remaining_card1 - 1
            remaining_card4 = remaining_card1 - 2
            if remaining_card4==0 or remaining_card3 == 0 or remaining_card2==0 or remaining_card1 == 0:
                permutations_cards = 0
            else:
                permutations_cards = (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
        
        elif possible_hand[0][1] == possible_hand[0][2] and possible_hand[0][2] == possible_hand[0][3]   :
            remaining_card1 = remaining_cards_ranks[ranks.index(possible_hand[0][0])]
            remaining_card2 = remaining_cards_ranks[ranks.index(possible_hand[0][1])]
            remaining_card3 = remaining_card2 - 1
            remaining_card4 = remaining_card2 - 2
            if remaining_card4==0 or remaining_card3 == 0 or remaining_card2==0 or remaining_card1 == 0:
                permutations_cards = 0
            else:
                permutations_cards = (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
        return permutations_cards/permutations
    elif distinct_rank == 1:
        if  remaining_cards_ranks[ranks.index(possible_hand[0][0])] < 4:
            return 0
        else:
            remaining_card1 = remaining_cards_ranks[ranks.index(possible_hand[0][0])]
            remaining_card2 = remaining_card1 -1
            remaining_card3 = remaining_card1 - 2
            remaining_card4 = remaining_card1 - 3
            permutations_cards = (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
        return permutations_cards/permutations
    else:
        return 0

def probability_4cards_flush(suit,card_needed,current_hand,possible_hand,occur,remaining_cards_ranks,list_numplayers):
    ranks = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
    suits = ['s','h','d','c']
    num3 = list_numplayers[0]
    distinct_rank = 0
    permutations = ((52-(2 + num3)))*((51-(2 + num3)))*((50-(2 + num3)))*((49-(2 + num3)))
    permutations_cards = 0
    remaining_card1 = 0
    remaining_card2= 0
    remaining_card3= 0
    remaining_card4= 0
    for count_rank in possible_hand[3]:
        if count_rank != 0:
            distinct_rank += 1
    if card_needed == 4:
        if distinct_rank == 4:
            if occur[suits.index(suit)][ranks.index(possible_hand[0][0])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][0])] == -1:
                return 0
            if occur[suits.index(suit)][ranks.index(possible_hand[0][1])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][1])] == -1:
                return 0          
            if occur[suits.index(suit)][ranks.index(possible_hand[0][2])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][2])] == -1:
                return 0          
            if occur[suits.index(suit)][ranks.index(possible_hand[0][3])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][3])] == -1:
                return 0                                                                                                     
            remaining_card1 = 1
            remaining_card2= 1
            remaining_card3= 1
            remaining_card4= 1
            permutations_cards = (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
            return permutations_cards/permutations
        else:
            return 0
    if card_needed == 3:
        if distinct_rank == 4:
            if occur[suits.index(suit)][ranks.index(possible_hand[0][1])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][1])] == -1:
                permutations_cards +=0        
            elif occur[suits.index(suit)][ranks.index(possible_hand[0][2])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][2])] == -1:
                permutations_cards +=0            
            elif occur[suits.index(suit)][ranks.index(possible_hand[0][3])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][3])] == -1:
                permutations_cards +=0                                                                                                        
            else:
                if occur[suits.index(suit)][ranks.index(possible_hand[0][0])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][0])] == -1:
                
                    remaining_card1 = remaining_cards_ranks[ranks.index(possible_hand[0][0])]
                    remaining_card2= 1
                    remaining_card3= 1
                    remaining_card4= 1
                    permutations_cards += (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
                else:
                    remaining_card1 = remaining_cards_ranks[ranks.index(possible_hand[0][0])]-1
                    remaining_card2= 1
                    remaining_card3= 1
                    remaining_card4= 1
                    permutations_cards += (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
                
            if occur[suits.index(suit)][ranks.index(possible_hand[0][0])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][0])] == -1:
                permutations_cards +=0   
                    
            elif occur[suits.index(suit)][ranks.index(possible_hand[0][2])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][2])] == -1:
                permutations_cards +=0             
            elif occur[suits.index(suit)][ranks.index(possible_hand[0][3])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][3])] == -1:
                permutations_cards +=0                                                                                                        
            else:
                if occur[suits.index(suit)][ranks.index(possible_hand[0][1])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][1])] == -1:
                
                    remaining_card1 = 1
                    remaining_card2= remaining_cards_ranks[ranks.index(possible_hand[0][1])]
                    remaining_card3= 1
                    remaining_card4= 1
                    permutations_cards += (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
                else:
                    remaining_card1 = 1
                    remaining_card2= remaining_cards_ranks[ranks.index(possible_hand[0][1])]-1
                    remaining_card3= 1
                    remaining_card4= 1
                    permutations_cards += (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
            if occur[suits.index(suit)][ranks.index(possible_hand[0][0])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][0])] == -1:
                permutations_cards +=0  
            elif occur[suits.index(suit)][ranks.index(possible_hand[0][1])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][1])] == -1:
                permutations_cards +=0        
                        
            elif occur[suits.index(suit)][ranks.index(possible_hand[0][3])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][3])] == -1:
                permutations_cards +=0                                                                                                        
            else:
                if occur[suits.index(suit)][ranks.index(possible_hand[0][2])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][2])] == -1:
                    remaining_card1 = 1
                    remaining_card2 = 1
                    remaining_card3 = remaining_cards_ranks[ranks.index(possible_hand[0][2])]
                    remaining_card4 = 1
                    permutations_cards += (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
                else:
                    remaining_card1 = 1
                    remaining_card2= 1
                    remaining_card3= remaining_cards_ranks[ranks.index(possible_hand[0][2])]-1
                    remaining_card4= 1
                    permutations_cards += (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
                
            if occur[suits.index(suit)][ranks.index(possible_hand[0][0])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][0])] == -1:
                permutations_cards +=0
            elif occur[suits.index(suit)][ranks.index(possible_hand[0][1])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][1])] == -1:
                permutations_cards +=0        
            elif occur[suits.index(suit)][ranks.index(possible_hand[0][2])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][2])] == -1:
                permutations_cards +=0            
                                                                                                               
            else:
                if occur[suits.index(suit)][ranks.index(possible_hand[0][3])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][3])] == -1:
                    remaining_card1 = 1
                    remaining_card2= 1
                    remaining_card3= 1
                    remaining_card4= remaining_cards_ranks[ranks.index(possible_hand[0][3])]
                    permutations_cards += (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
                else:
                    remaining_card1 = 1
                    remaining_card2= 1
                    remaining_card3= 1
                    remaining_card4= remaining_cards_ranks[ranks.index(possible_hand[0][3])]-1
                    permutations_cards += (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
                    
            if occur[suits.index(suit)][ranks.index(possible_hand[0][0])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][0])] == -1:
                permutations_cards +=0
            elif occur[suits.index(suit)][ranks.index(possible_hand[0][1])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][1])] == -1:
                permutations_cards +=0        
            elif occur[suits.index(suit)][ranks.index(possible_hand[0][2])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][2])] == -1:
                permutations_cards +=0            
            elif occur[suits.index(suit)][ranks.index(possible_hand[0][3])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][3])] == -1:
                permutations_cards +=0                                                                                            
            else:
                remaining_card1 = 1
                remaining_card2= 1
                remaining_card3= 1
                remaining_card4= 1
                permutations_cards += (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
                    
            return permutations_cards/permutations
        elif distinct_rank == 3:
            if possible_hand[0][0] == possible_hand[0][1] :
                if occur[suits.index(suit)][ranks.index(possible_hand[0][0])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][0])] == -1:
                    permutations_cards = 0
                elif occur[suits.index(suit)][ranks.index(possible_hand[0][1])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][1])] == -1:
                    permutations_cards = 0
                elif occur[suits.index(suit)][ranks.index(possible_hand[0][2])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][2])] == -1:
                    permutations_cards = 0
                elif occur[suits.index(suit)][ranks.index(possible_hand[0][3])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][3])] == -1:
                    permutations_cards = 0
                else:
                    if remaining_cards_ranks[ranks.index(possible_hand[0][0])] == 0 or remaining_cards_ranks[ranks.index(possible_hand[0][0])] == 1:
                        permutations_cards = 0
                    else:
                        remaining_card1 = 1
                        remaining_card2= remaining_cards_ranks[ranks.index(possible_hand[0][0])]-1
                        remaining_card3= 1
                        remaining_card4= 1
                        permutations_cards += (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
                return permutations_cards/permutations   
                
            elif possible_hand[0][0] == possible_hand[0][2] :
                if occur[suits.index(suit)][ranks.index(possible_hand[0][0])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][0])] == -1:
                    permutations_cards = 0
                elif occur[suits.index(suit)][ranks.index(possible_hand[0][1])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][1])] == -1:
                    permutations_cards = 0
                elif occur[suits.index(suit)][ranks.index(possible_hand[0][2])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][2])] == -1:
                    permutations_cards = 0
                elif occur[suits.index(suit)][ranks.index(possible_hand[0][3])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][3])] == -1:
                    permutations_cards = 0
                else:
                    if remaining_cards_ranks[ranks.index(possible_hand[0][0])] == 0 or remaining_cards_ranks[ranks.index(possible_hand[0][0])] == 1:
                        permutations_cards = 0
                    else:
                        remaining_card1 = 1
                        remaining_card2= 1
                        remaining_card3= remaining_cards_ranks[ranks.index(possible_hand[0][0])]-1
                        remaining_card4= 1
                        permutations_cards += (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
                return permutations_cards/permutations
            elif possible_hand[0][0] == possible_hand[0][3] :
                if occur[suits.index(suit)][ranks.index(possible_hand[0][0])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][0])] == -1:
                    permutations_cards = 0
                elif occur[suits.index(suit)][ranks.index(possible_hand[0][1])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][1])] == -1:
                    permutations_cards = 0
                elif occur[suits.index(suit)][ranks.index(possible_hand[0][2])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][2])] == -1:
                    permutations_cards = 0
                elif occur[suits.index(suit)][ranks.index(possible_hand[0][3])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][3])] == -1:
                    permutations_cards = 0
                else:
                    if remaining_cards_ranks[ranks.index(possible_hand[0][0])] == 0 or remaining_cards_ranks[ranks.index(possible_hand[0][0])] == 1 :
                        permutations_cards = 0
                    else:
                        remaining_card1 = 1
                        remaining_card2= 1
                        remaining_card3= 1
                        remaining_card4= remaining_cards_ranks[ranks.index(possible_hand[0][0])]-1
                        permutations_cards += (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
                return permutations_cards/permutations
            elif possible_hand[0][1] == possible_hand[0][2] :
                if occur[suits.index(suit)][ranks.index(possible_hand[0][0])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][0])] == -1:
                    permutations_cards = 0
                elif occur[suits.index(suit)][ranks.index(possible_hand[0][1])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][1])] == -1:
                    permutations_cards = 0
                elif occur[suits.index(suit)][ranks.index(possible_hand[0][2])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][2])] == -1:
                    permutations_cards = 0
                elif occur[suits.index(suit)][ranks.index(possible_hand[0][3])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][3])] == -1:
                    permutations_cards = 0
                else:
                    if remaining_cards_ranks[ranks.index(possible_hand[0][1])] == 0 or remaining_cards_ranks[ranks.index(possible_hand[0][1])] == 1 :
                        permutations_cards = 0
                    else:
                        remaining_card1 = 1
                        remaining_card2= 1
                        remaining_card3= remaining_cards_ranks[ranks.index(possible_hand[0][1])]-1
                        remaining_card4= 1
                        permutations_cards += (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
                return permutations_cards/permutations
            elif possible_hand[0][1] == possible_hand[0][3] :
                if occur[suits.index(suit)][ranks.index(possible_hand[0][0])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][0])] == -1:
                    permutations_cards = 0
                elif occur[suits.index(suit)][ranks.index(possible_hand[0][1])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][1])] == -1:
                    permutations_cards = 0
                elif occur[suits.index(suit)][ranks.index(possible_hand[0][2])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][2])] == -1:
                    permutations_cards = 0
                elif occur[suits.index(suit)][ranks.index(possible_hand[0][3])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][3])] == -1:
                    permutations_cards = 0
                else:
                    if remaining_cards_ranks[ranks.index(possible_hand[0][1])] == 0 or remaining_cards_ranks[ranks.index(possible_hand[0][1])] == 1 :
                        permutations_cards += 0
                    else:
                        remaining_card1 = 1
                        remaining_card2= 1
                        remaining_card3= 1
                        remaining_card4= remaining_cards_ranks[ranks.index(possible_hand[0][1])]-1
                        permutations_cards += (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
                return permutations_cards/permutations
            elif possible_hand[0][2] == possible_hand[0][3] :
                if occur[suits.index(suit)][ranks.index(possible_hand[0][0])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][0])] == -1:
                    permutations_cards = 0
                elif occur[suits.index(suit)][ranks.index(possible_hand[0][1])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][1])] == -1:
                    permutations_cards = 0
                elif occur[suits.index(suit)][ranks.index(possible_hand[0][2])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][2])] == -1:
                    permutations_cards = 0
                elif occur[suits.index(suit)][ranks.index(possible_hand[0][3])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][3])] == -1:
                    permutations_cards = 0
                else:
                    if remaining_cards_ranks[ranks.index(possible_hand[0][2])] == 0 or remaining_cards_ranks[ranks.index(possible_hand[0][2])] == 1 :
                        permutations_cards = 0
                    else:
                        remaining_card1 = 1
                        remaining_card2= 1
                        remaining_card3= 1
                        remaining_card4= remaining_cards_ranks[ranks.index(possible_hand[0][2])]-1
                        permutations_cards += (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
                return permutations_cards/permutations
        else:
            return 0
    if card_needed == 2:
        if distinct_rank == 2:
            if possible_hand[0][0] == possible_hand[0][1] and possible_hand[0][2] == possible_hand[0][3] :
                if occur[suits.index(suit)][ranks.index(possible_hand[0][0])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][0])] == -1:
                    permutations_cards = 0
                elif occur[suits.index(suit)][ranks.index(possible_hand[0][2])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][2])] == -1:
                    permutations_cards = 0
                else:
                    remaining_card1 = remaining_cards_ranks[ranks.index(possible_hand[0][0])] -1
                    remaining_card2= 1
                    remaining_card3= remaining_cards_ranks[ranks.index(possible_hand[0][2])] -1
                    remaining_card4= 1
                    if remaining_card4==0 or remaining_card3 == 0 or remaining_card2==0 or remaining_card1 == 0:
                        permutations_cards += 0
                    else:
                        permutations_cards += (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
        
            elif possible_hand[0][0] == possible_hand[0][2] and possible_hand[0][1] == possible_hand[0][3] :
                if occur[suits.index(suit)][ranks.index(possible_hand[0][0])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][0])] == -1:
                    permutations_cards = 0
                elif occur[suits.index(suit)][ranks.index(possible_hand[0][1])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][1])] == -1:
                    permutations_cards = 0
                
                else:
                    remaining_card1 = remaining_cards_ranks[ranks.index(possible_hand[0][0])]-1
                    remaining_card2= remaining_cards_ranks[ranks.index(possible_hand[0][1])]-1
                    remaining_card3= 1
                    remaining_card4= 1
                    if remaining_card4==0 or remaining_card3 == 0 or remaining_card2==0 or remaining_card1 == 0:
                        permutations_cards += 0
                    else:
                        permutations_cards += (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
            elif possible_hand[0][0] == possible_hand[0][3] and possible_hand[0][1] == possible_hand[0][2] :
                if occur[suits.index(suit)][ranks.index(possible_hand[0][0])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][0])] == -1:
                    permutations_cards = 0
                elif occur[suits.index(suit)][ranks.index(possible_hand[0][1])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][1])] == -1:
                    permutations_cards = 0
                else:
                    remaining_card1 = remaining_cards_ranks[ranks.index(possible_hand[0][0])]-1
                    remaining_card2= remaining_cards_ranks[ranks.index(possible_hand[0][1])]-1
                    remaining_card3= 1
                    remaining_card4= 1
                    if remaining_card4==0 or remaining_card3 == 0 or remaining_card2==0 or remaining_card1 == 0:
                        permutations_cards += 0
                    else:
                        permutations_cards += (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
                
            elif possible_hand[0][0] == possible_hand[0][1] and possible_hand[0][1] == possible_hand[0][2] :
                if occur[suits.index(suit)][ranks.index(possible_hand[0][0])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][0])] == -1:
                    permutations_cards = 0
                elif occur[suits.index(suit)][ranks.index(possible_hand[0][3])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][3])] == -1:
                    permutations_cards = 0
                else:
                    remaining_card1 = remaining_cards_ranks[ranks.index(possible_hand[0][0])]-1
                    remaining_card2 = remaining_card1 - 1
                    remaining_card3 = 1
                    remaining_card4 =  1
                    if remaining_card4==0 or remaining_card3 == 0 or remaining_card2==0 or remaining_card1 == 0:
                        permutations_cards += 0
                    else:
                        permutations_cards += (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
            
            elif possible_hand[0][0] == possible_hand[0][1] and possible_hand[0][1] == possible_hand[0][3] :
                if occur[suits.index(suit)][ranks.index(possible_hand[0][0])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][0])] == -1:
                    permutations_cards = 0
                
                elif occur[suits.index(suit)][ranks.index(possible_hand[0][2])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][2])] == -1:
                    permutations_cards = 0
                
                else:
                    remaining_card1 = remaining_cards_ranks[ranks.index(possible_hand[0][0])]-1
                    remaining_card2 = 1
                    remaining_card3 = 1
                    remaining_card4 = remaining_card1-1
                    if remaining_card4==0 or remaining_card3 == 0 or remaining_card2==0 or remaining_card1 == 0:
                        permutations_cards += 0
                    else:
                        permutations_cards += (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
            
            elif possible_hand[0][0] == possible_hand[0][2] and possible_hand[0][2] == possible_hand[0][3]  :
                if occur[suits.index(suit)][ranks.index(possible_hand[0][0])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][0])] == -1:
                    permutations_cards = 0
                elif occur[suits.index(suit)][ranks.index(possible_hand[0][1])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][1])] == -1:
                    permutations_cards = 0
                
                else:
                    remaining_card1 = remaining_cards_ranks[ranks.index(possible_hand[0][0])]-1
                    remaining_card2 = 1
                    remaining_card3 = remaining_card1 - 1
                    remaining_card4 = 1
                    if remaining_card4==0 or remaining_card3 == 0 or remaining_card2==0 or remaining_card1 == 0:
                        permutations_cards += 0
                    else:
                        permutations_cards += (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
            
            elif possible_hand[0][1] == possible_hand[0][2] and possible_hand[0][2] == possible_hand[0][3]:
                if occur[suits.index(suit)][ranks.index(possible_hand[0][0])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][0])] == -1:
                    permutations_cards = 0
                elif occur[suits.index(suit)][ranks.index(possible_hand[0][3])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][3])] == -1:
                    permutations_cards = 0
                else:
                    remaining_card1 = 1
                    remaining_card2 = remaining_cards_ranks[ranks.index(possible_hand[0][1])]-1
                    remaining_card3 = remaining_card2 - 1
                    remaining_card4 = 1
                    if remaining_card4==0 or remaining_card3 == 0 or remaining_card2==0 or remaining_card1 == 0:
                        permutations_cards += 0
                    else:
                        permutations_cards += (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
            return permutations_cards/permutations
            
        elif distinct_rank == 3:
            if possible_hand[0][0] == possible_hand[0][1] :
                if remaining_cards_ranks[ranks.index(possible_hand[0][0])] > 1:
                    if occur[suits.index(suit)][ranks.index(possible_hand[0][0])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][0])] == -1:
                        permutations_cards += 0
                    else:
                        if occur[suits.index(suit)][ranks.index(possible_hand[0][0])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][0])] == -1:
                            permutations_cards += 0
                        elif occur[suits.index(suit)][ranks.index(possible_hand[0][2])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][2])] == -1:
                            permutations_cards += 0
                        else:
                            remaining_card1 = remaining_cards_ranks[ranks.index(possible_hand[0][0])]-1
                            remaining_card2 = 1
                            remaining_card3 = 1
                            remaining_card4 = remaining_cards_ranks[ranks.index(possible_hand[0][3])]-1
                            if remaining_card4<=0 or remaining_card3 == 0 or remaining_card2==0 or remaining_card1 == 0:
                                permutations_cards += 0
                            else:
                                permutations_cards += (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
                        if occur[suits.index(suit)][ranks.index(possible_hand[0][1])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][1])] == -1:
                            permutations_cards += 0
                        elif occur[suits.index(suit)][ranks.index(possible_hand[0][3])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][3])] == -1:
                            permutations_cards += 0
                        else:
                            remaining_card1 = remaining_cards_ranks[ranks.index(possible_hand[0][0])]-1
                            remaining_card2 = 1
                            remaining_card3 = remaining_cards_ranks[ranks.index(possible_hand[0][2])]-1
                            remaining_card4 = 1
                            if remaining_card4==0 or remaining_card3 <= 0 or remaining_card2==0 or remaining_card1 == 0:
                                permutations_cards += 0
                            else:
                                permutations_cards += (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
                        if occur[suits.index(suit)][ranks.index(possible_hand[0][1])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][1])] == -1:
                            permutations_cards += 0
                        elif occur[suits.index(suit)][ranks.index(possible_hand[0][3])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][3])] == -1:
                            permutations_cards += 0
                        elif occur[suits.index(suit)][ranks.index(possible_hand[0][2])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][2])] == -1:
                            permutations_cards += 0
                        else:
                            remaining_card1 = remaining_cards_ranks[ranks.index(possible_hand[0][0])]-1
                            remaining_card2 = 1
                            remaining_card3 = 1
                            remaining_card4 = 1
                            if remaining_card4==0 or remaining_card3 <= 0 or remaining_card2==0 or remaining_card1 == 0:
                                permutations_cards += 0
                            else:
                                permutations_cards += (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
                    if occur[suits.index(suit)][ranks.index(possible_hand[0][2])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][2])] == -1:
                            permutations_cards += 0
                    elif occur[suits.index(suit)][ranks.index(possible_hand[0][3])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][3])] == -1:
                        permutations_cards += 0
                    else:
                        if occur[suits.index(suit)][ranks.index(possible_hand[0][0])] == 0:
                            remaining_card1 = remaining_cards_ranks[ranks.index(possible_hand[0][0])]-1
                            remaining_card2 = remaining_cards_ranks[ranks.index(possible_hand[0][0])] -2
                            remaining_card3 = 1
                            remaining_card4 = 1
                            if remaining_card4==0 or remaining_card3 == 0 or remaining_card2==0 or remaining_card1 == 0:
                                permutations_cards += 0
                            else:
                                permutations_cards += (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
                        else:
                            remaining_card1 = remaining_cards_ranks[ranks.index(possible_hand[0][0])]
                            remaining_card2 = remaining_cards_ranks[ranks.index(possible_hand[0][0])] -1
                            remaining_card3 = 1
                            remaining_card4 = 1
                            if remaining_card4==0 or remaining_card3 == 0 or remaining_card2==0 or remaining_card1 == 0:
                                permutations_cards += 0
                            else:
                                permutations_cards += (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
                        

                else: 
                    permutations_cards += 0
            elif possible_hand[0][0] == possible_hand[0][2] :
                if remaining_cards_ranks[ranks.index(possible_hand[0][0])] > 1:
                    if occur[suits.index(suit)][ranks.index(possible_hand[0][0])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][0])] == -1:
                        permutations_cards += 0
                    else:
                        if occur[suits.index(suit)][ranks.index(possible_hand[0][0])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][0])] == -1:
                            permutations_cards += 0
                        elif occur[suits.index(suit)][ranks.index(possible_hand[0][1])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][1])] == -1:
                            permutations_cards += 0
                        else:
                            remaining_card1 = remaining_cards_ranks[ranks.index(possible_hand[0][0])]-1
                            remaining_card2 = 1
                            remaining_card3 = 1
                            remaining_card4 = remaining_cards_ranks[ranks.index(possible_hand[0][3])]-1
                            if remaining_card4<=0 or remaining_card3 == 0 or remaining_card2==0 or remaining_card1 == 0:
                                permutations_cards += 0
                            else:
                                permutations_cards += (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
                        if occur[suits.index(suit)][ranks.index(possible_hand[0][2])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][3])] == -1:
                            permutations_cards += 0
                        elif occur[suits.index(suit)][ranks.index(possible_hand[0][3])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][3])] == -1:
                            permutations_cards += 0
                        else:
                            remaining_card1 = remaining_cards_ranks[ranks.index(possible_hand[0][0])]-1
                            remaining_card2 = remaining_cards_ranks[ranks.index(possible_hand[0][1])]-1
                            remaining_card3 = 1
                            remaining_card4 = 1
                            if remaining_card4==0 or remaining_card3 == 0 or remaining_card2<=0 or remaining_card1 == 0:
                                permutations_cards += 0
                            else:
                                permutations_cards += (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
                        if occur[suits.index(suit)][ranks.index(possible_hand[0][1])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][1])] == -1:
                            permutations_cards += 0
                        elif occur[suits.index(suit)][ranks.index(possible_hand[0][3])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][3])] == -1:
                            permutations_cards += 0
                        elif occur[suits.index(suit)][ranks.index(possible_hand[0][2])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][2])] == -1:
                            permutations_cards += 0
                        else:
                            remaining_card1 = remaining_cards_ranks[ranks.index(possible_hand[0][0])]-1
                            remaining_card2 = 1
                            remaining_card3 = 1
                            remaining_card4 = 1
                            if remaining_card4==0 or remaining_card3 <= 0 or remaining_card2==0 or remaining_card1 == 0:
                                permutations_cards += 0
                            else:
                                permutations_cards += (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
                    if occur[suits.index(suit)][ranks.index(possible_hand[0][1])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][1])] == -1:
                            permutations_cards += 0
                    elif occur[suits.index(suit)][ranks.index(possible_hand[0][3])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][3])] == -1:
                        permutations_cards += 0
                    else:
                        if occur[suits.index(suit)][ranks.index(possible_hand[0][0])] == 0:
                            remaining_card1 = remaining_cards_ranks[ranks.index(possible_hand[0][0])]-1
                            remaining_card2 = 1
                            remaining_card3 = remaining_cards_ranks[ranks.index(possible_hand[0][0])] -2
                            remaining_card4 = 1
                            if remaining_card4==0 or remaining_card3 == 0 or remaining_card2==0 or remaining_card1 == 0:
                                permutations_cards += 0
                            else:
                                permutations_cards += (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
                        else:
                            remaining_card1 = remaining_cards_ranks[ranks.index(possible_hand[0][0])]
                            remaining_card2 = 1
                            remaining_card3 = remaining_cards_ranks[ranks.index(possible_hand[0][0])] - 1
                            remaining_card4 = 1
                            if remaining_card4==0 or remaining_card3 == 0 or remaining_card2==0 or remaining_card1 == 0:
                                permutations_cards += 0
                            else:
                                permutations_cards += (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
                
                else: 
                    permutations_cards += 0
            elif possible_hand[0][0] == possible_hand[0][3] :
                if remaining_cards_ranks[ranks.index(possible_hand[0][0])] > 1:
                    if occur[suits.index(suit)][ranks.index(possible_hand[0][0])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][0])] == -1:
                        permutations_cards += 0
                    else:
                        if occur[suits.index(suit)][ranks.index(possible_hand[0][1])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][1])] == -1:
                            permutations_cards += 0
                        elif occur[suits.index(suit)][ranks.index(possible_hand[0][3])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][3])] == -1:
                            permutations_cards += 0
                        else:
                            remaining_card1 = remaining_cards_ranks[ranks.index(possible_hand[0][0])]-1
                            remaining_card2 = 1
                            remaining_card3 = remaining_cards_ranks[ranks.index(possible_hand[0][2])]-1
                            remaining_card4 = 1
                            if remaining_card4==0 or remaining_card3 <= 0 or remaining_card2==0 or remaining_card1 == 0:
                                permutations_cards += 0
                            else:
                                permutations_cards += (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
                        if occur[suits.index(suit)][ranks.index(possible_hand[0][2])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][3])] == -1:
                            permutations_cards += 0
                        elif occur[suits.index(suit)][ranks.index(possible_hand[0][3])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][3])] == -1:
                            permutations_cards += 0
                        else:
                            remaining_card1 = remaining_cards_ranks[ranks.index(possible_hand[0][0])]-1
                            remaining_card2 = remaining_cards_ranks[ranks.index(possible_hand[0][1])] -1
                            remaining_card3 = 1
                            remaining_card4 = 1
                            if remaining_card4==0 or remaining_card3 == 0 or remaining_card2<=0 or remaining_card1 == 0:
                                permutations_cards += 0
                            else:
                                permutations_cards += (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
                        if occur[suits.index(suit)][ranks.index(possible_hand[0][1])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][1])] == -1:
                            permutations_cards += 0
                        elif occur[suits.index(suit)][ranks.index(possible_hand[0][3])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][3])] == -1:
                            permutations_cards += 0
                        elif occur[suits.index(suit)][ranks.index(possible_hand[0][2])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][2])] == -1:
                            permutations_cards += 0
                        else:
                            remaining_card1 = remaining_cards_ranks[ranks.index(possible_hand[0][0])]-1
                            remaining_card2 = 1
                            remaining_card3 = 1
                            remaining_card4 = 1
                            if remaining_card4==0 or remaining_card3 <= 0 or remaining_card2==0 or remaining_card1 == 0:
                                permutations_cards += 0
                            else:
                                permutations_cards += (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
                    if occur[suits.index(suit)][ranks.index(possible_hand[0][1])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][1])] == -1:
                            permutations_cards += 0
                    elif occur[suits.index(suit)][ranks.index(possible_hand[0][2])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][2])] == -1:
                        permutations_cards += 0
                    else:
                        if occur[suits.index(suit)][ranks.index(possible_hand[0][0])] == 0:
                            remaining_card1 = remaining_cards_ranks[ranks.index(possible_hand[0][0])] - 1
                            remaining_card2 = 1
                            remaining_card3 = 1
                            remaining_card4 = remaining_cards_ranks[ranks.index(possible_hand[0][0])] - 2
                            if remaining_card4==0 or remaining_card3 == 0 or remaining_card2==0 or remaining_card1 == 0:
                                permutations_cards += 0
                            else:
                                permutations_cards += (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
                        else:
                            remaining_card1 = remaining_cards_ranks[ranks.index(possible_hand[0][0])] 
                            remaining_card2 = 1
                            remaining_card3 = 1
                            remaining_card4 = remaining_cards_ranks[ranks.index(possible_hand[0][0])] - 1
                            if remaining_card4==0 or remaining_card3 == 0 or remaining_card2==0 or remaining_card1 == 0:
                                permutations_cards += 0
                            else:
                                permutations_cards += (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
                        
                else: 
                    permutations_cards += 0
            elif possible_hand[0][1] == possible_hand[0][2] :
                if remaining_cards_ranks[ranks.index(possible_hand[0][1])] > 1:
                    if occur[suits.index(suit)][ranks.index(possible_hand[0][1])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][1])] == -1:
                        permutations_cards += 0
                    else:
                        if occur[suits.index(suit)][ranks.index(possible_hand[0][1])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][1])] == -1:
                            permutations_cards += 0
                        elif occur[suits.index(suit)][ranks.index(possible_hand[0][3])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][3])] == -1:
                            permutations_cards += 0
                        else:
                            remaining_card1 = remaining_cards_ranks[ranks.index(possible_hand[0][0])]-1
                            remaining_card2 = remaining_cards_ranks[ranks.index(possible_hand[0][1])]-1
                            remaining_card3 = 1
                            remaining_card4 = 1
                            if remaining_card4<=0 or remaining_card3 == 0 or remaining_card2==0 or remaining_card1 <= 0:
                                permutations_cards += 0
                            else:
                                permutations_cards += (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
                        if occur[suits.index(suit)][ranks.index(possible_hand[0][0])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][0])] == -1:
                            permutations_cards += 0
                        elif occur[suits.index(suit)][ranks.index(possible_hand[0][2])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][2])] == -1:
                            permutations_cards += 0
                        else:
                            remaining_card1 = 1
                            remaining_card2 = remaining_cards_ranks[ranks.index(possible_hand[0][1])]-1
                            remaining_card3 = 1
                            remaining_card4 = remaining_cards_ranks[ranks.index(possible_hand[0][3])]-1
                            if remaining_card4<=0 or remaining_card3 == 0 or remaining_card2==0 or remaining_card1 <= 0:
                                permutations_cards += 0
                            else:
                                permutations_cards += (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
                        if occur[suits.index(suit)][ranks.index(possible_hand[0][0])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][0])] == -1:
                            permutations_cards += 0
                        elif occur[suits.index(suit)][ranks.index(possible_hand[0][3])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][3])] == -1:
                            permutations_cards += 0
                        elif occur[suits.index(suit)][ranks.index(possible_hand[0][2])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][2])] == -1:
                            permutations_cards += 0
                        else:
                            remaining_card1 = 1 
                            remaining_card2 = remaining_cards_ranks[ranks.index(possible_hand[0][1])]-1
                            remaining_card3 = 1
                            remaining_card4 = 1
                            if remaining_card4==0 or remaining_card3 <= 0 or remaining_card2==0 or remaining_card1 == 0:
                                permutations_cards += 0
                            else:
                                permutations_cards += (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
                    
                    if occur[suits.index(suit)][ranks.index(possible_hand[0][0])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][1])] == -1:
                            permutations_cards += 0
                    elif occur[suits.index(suit)][ranks.index(possible_hand[0][3])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][2])] == -1:
                        permutations_cards += 0
                    else:
                        if occur[suits.index(suit)][ranks.index(possible_hand[0][1])] == 0:
                            
                            remaining_card1 = 1
                            remaining_card2 = remaining_cards_ranks[ranks.index(possible_hand[0][1])] - 1
                            remaining_card3 = remaining_cards_ranks[ranks.index(possible_hand[0][1])] - 2
                            remaining_card4 = 1
                            if remaining_card4==0 or remaining_card3 == 0 or remaining_card2==0 or remaining_card1 == 0:
                                permutations_cards += 0
                            else:
                                permutations_cards += (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
                        else:
                            
                            remaining_card1 = 1
                            remaining_card2 = remaining_cards_ranks[ranks.index(possible_hand[0][1])]
                            remaining_card3 = remaining_cards_ranks[ranks.index(possible_hand[0][1])] - 1
                            remaining_card4 = 1
                            if remaining_card4==0 or remaining_card3 == 0 or remaining_card2==0 or remaining_card1 == 0:
                                permutations_cards += 0
                            else:
                                permutations_cards += (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1      
                else: 
                    permutations_cards += 0
            elif possible_hand[0][1] == possible_hand[0][3] :
                if remaining_cards_ranks[ranks.index(possible_hand[0][1])] > 1:
                    if occur[suits.index(suit)][ranks.index(possible_hand[0][1])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][1])] == -1:
                        permutations_cards += 0
                    else:
                        if occur[suits.index(suit)][ranks.index(possible_hand[0][1])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][1])] == -1:
                            permutations_cards += 0
                        elif occur[suits.index(suit)][ranks.index(possible_hand[0][2])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][2])] == -1:
                            permutations_cards += 0
                        else:
                            remaining_card1 = remaining_cards_ranks[ranks.index(possible_hand[0][0])]-1
                            remaining_card2 = remaining_cards_ranks[ranks.index(possible_hand[0][1])]-1
                            remaining_card3 = 1
                            remaining_card4 = 1
                            if remaining_card4==0 or remaining_card3 == 0 or remaining_card2==0 or remaining_card1 == 0:
                                permutations_cards += 0
                            else:
                                permutations_cards += (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
                        if occur[suits.index(suit)][ranks.index(possible_hand[0][2])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][3])] == -1:
                            permutations_cards += 0
                        elif occur[suits.index(suit)][ranks.index(possible_hand[0][3])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][3])] == -1:
                            permutations_cards += 0
                        else:
                            remaining_card1 = remaining_cards_ranks[ranks.index(possible_hand[0][0])]-1
                            remaining_card2 = remaining_cards_ranks[ranks.index(possible_hand[0][1])]-1
                            remaining_card3 = 1
                            remaining_card4 = 1
                            if remaining_card4==0 or remaining_card3 == 0 or remaining_card2==0 or remaining_card1 <= 0:
                                permutations_cards += 0
                            else:
                                permutations_cards += (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
                        if occur[suits.index(suit)][ranks.index(possible_hand[0][0])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][0])] == -1:
                            permutations_cards += 0
                        elif occur[suits.index(suit)][ranks.index(possible_hand[0][3])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][3])] == -1:
                            permutations_cards += 0
                        elif occur[suits.index(suit)][ranks.index(possible_hand[0][2])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][2])] == -1:
                            permutations_cards += 0
                        else:
                            remaining_card1 = 1 
                            remaining_card2 = remaining_cards_ranks[ranks.index(possible_hand[0][1])]-1
                            remaining_card3 = 1
                            remaining_card4 = 1
                            if remaining_card4==0 or remaining_card3 <= 0 or remaining_card2==0 or remaining_card1 == 0:
                                permutations_cards += 0
                            else:
                                permutations_cards += (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
                    
                    if occur[suits.index(suit)][ranks.index(possible_hand[0][0])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][0])] == -1:
                            permutations_cards += 0
                    elif occur[suits.index(suit)][ranks.index(possible_hand[0][2])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][2])] == -1:
                        permutations_cards += 0
                    else:
                        if occur[suits.index(suit)][ranks.index(possible_hand[0][1])] == 0:
                            remaining_card1 = 1
                            remaining_card2 = remaining_cards_ranks[ranks.index(possible_hand[0][1])] - 1
                            remaining_card3 = 1
                            remaining_card4 = remaining_cards_ranks[ranks.index(possible_hand[0][1])] - 2
                            if remaining_card4==0 or remaining_card3 == 0 or remaining_card2==0 or remaining_card1 == 0:
                                permutations_cards += 0
                            else:
                                permutations_cards += (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
                        else:
                            remaining_card1 = 1
                            remaining_card2 = remaining_cards_ranks[ranks.index(possible_hand[0][1])] 
                            remaining_card3 = 1
                            remaining_card4 = remaining_cards_ranks[ranks.index(possible_hand[0][1])] - 1
                            if remaining_card4==0 or remaining_card3 == 0 or remaining_card2==0 or remaining_card1 == 0:
                                permutations_cards += 0
                            else:
                                permutations_cards += (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
                else: 
                    permutations_cards += 0

            elif possible_hand[0][2] == possible_hand[0][3] :
                if remaining_cards_ranks[ranks.index(possible_hand[0][2])] > 1:
                    if occur[suits.index(suit)][ranks.index(possible_hand[0][2])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][2])] == -1:
                        permutations_cards += 0
                    else:
                        if occur[suits.index(suit)][ranks.index(possible_hand[0][0])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][0])] == -1:
                            permutations_cards += 0
                        elif occur[suits.index(suit)][ranks.index(possible_hand[0][2])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][2])] == -1:
                            permutations_cards += 0
                        else:
                            remaining_card1 = 1
                            remaining_card2 = remaining_cards_ranks[ranks.index(possible_hand[0][1])]-1
                            remaining_card3 = 1
                            remaining_card4 = remaining_cards_ranks[ranks.index(possible_hand[0][3])]-1
                            if remaining_card4==0 or remaining_card3 == 0 or remaining_card2<=0 or remaining_card1 == 0:
                                permutations_cards += 0
                            else:
                                permutations_cards += (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
                        if occur[suits.index(suit)][ranks.index(possible_hand[0][1])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][1])] == -1:
                            permutations_cards += 0
                        elif occur[suits.index(suit)][ranks.index(possible_hand[0][2])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][2])] == -1:
                            permutations_cards += 0
                        else:
                            remaining_card1 = remaining_cards_ranks[ranks.index(possible_hand[0][0])]-1
                            remaining_card2 = 1
                            remaining_card3 = 1
                            remaining_card4 = remaining_cards_ranks[ranks.index(possible_hand[0][3])]-1
                            if remaining_card4==0 or remaining_card3 == 0 or remaining_card2==0 or remaining_card1 <= 0:
                                permutations_cards += 0
                            else:
                                permutations_cards += (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
                        if occur[suits.index(suit)][ranks.index(possible_hand[0][0])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][0])] == -1:
                            permutations_cards += 0
                        elif occur[suits.index(suit)][ranks.index(possible_hand[0][1])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][1])] == -1:
                            permutations_cards += 0
                        elif occur[suits.index(suit)][ranks.index(possible_hand[0][2])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][2])] == -1:
                            permutations_cards += 0
                        else:
                            remaining_card1 = 1 
                            remaining_card2 = 1
                            remaining_card3 = 1
                            remaining_card4 = remaining_cards_ranks[ranks.index(possible_hand[0][3])]-1
                            if remaining_card4==0 or remaining_card3 <= 0 or remaining_card2==0 or remaining_card1 == 0:
                                permutations_cards += 0
                            else:
                                permutations_cards += (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
                    
                    if occur[suits.index(suit)][ranks.index(possible_hand[0][0])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][0])] == -1:
                            permutations_cards += 0
                    elif occur[suits.index(suit)][ranks.index(possible_hand[0][1])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][1])] == -1:
                        permutations_cards += 0
                    else:
                        if occur[suits.index(suit)][ranks.index(possible_hand[0][3])] == 0:
                            remaining_card1 = 1
                            remaining_card2 = 1
                            remaining_card3 = remaining_cards_ranks[ranks.index(possible_hand[0][3])] - 1
                            remaining_card4 = remaining_cards_ranks[ranks.index(possible_hand[0][3])] - 2
                            if remaining_card4<=0 or remaining_card3 <= 0 or remaining_card2<=0 or remaining_card1 <= 0:
                                permutations_cards += 0
                            else:
                                permutations_cards += (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
                        else:
                            remaining_card1 = 1
                            remaining_card2 = 1 
                            remaining_card3 = remaining_cards_ranks[ranks.index(possible_hand[0][3])]
                            remaining_card4 = remaining_cards_ranks[ranks.index(possible_hand[0][3])] - 1
                            if remaining_card4==0 or remaining_card3 == 0 or remaining_card2==0 or remaining_card1 == 0:
                                permutations_cards += 0
                            else:
                                permutations_cards += (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1

                else: 
                    permutations_cards += 0
            else: 
                permutations_cards += 0
            return permutations_cards/permutations
        elif distinct_rank == 4:
            if occur[suits.index(suit)][ranks.index(possible_hand[0][0])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][0])] == -1:
                permutations_cards += 0
            elif occur[suits.index(suit)][ranks.index(possible_hand[0][1])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][1])] == -1:
                permutations_cards += 0
            elif occur[suits.index(suit)][ranks.index(possible_hand[0][2])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][2])] == -1:
                permutations_cards += 0
            elif occur[suits.index(suit)][ranks.index(possible_hand[0][3])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][3])] == -1:
                permutations_cards += 0
            else:
                remaining_card1 = 1
                remaining_card2 = 1 
                remaining_card3 = 1
                remaining_card4 = 1
                permutations_cards += (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1

            if occur[suits.index(suit)][ranks.index(possible_hand[0][0])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][0])] == -1:
                permutations_cards += 0
            elif occur[suits.index(suit)][ranks.index(possible_hand[0][1])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][1])] == -1:
                permutations_cards += 0
            elif occur[suits.index(suit)][ranks.index(possible_hand[0][2])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][2])] == -1:
                permutations_cards += 0
            else:
                if occur[suits.index(suit)][ranks.index(possible_hand[0][3])] == 0:
                    remaining_card1 = 1
                    remaining_card2 = 1
                    remaining_card3 = 1
                    remaining_card4 = remaining_cards_ranks[ranks.index(possible_hand[0][3])] - 1
                    if remaining_card4<=0 or remaining_card3 <= 0 or remaining_card2<=0 or remaining_card1 <= 0:
                        permutations_cards += 0
                    else:
                        permutations_cards += (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
                else:
                    remaining_card1 = 1
                    remaining_card2 = 1
                    remaining_card3 = 1
                    remaining_card4 = remaining_cards_ranks[ranks.index(possible_hand[0][3])]
                    if remaining_card4==0 or remaining_card3 == 0 or remaining_card2==0 or remaining_card1 == 0:
                        permutations_cards += 0
                    else:
                        permutations_cards += (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1

            if occur[suits.index(suit)][ranks.index(possible_hand[0][0])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][0])] == -1:
                permutations_cards += 0
            elif occur[suits.index(suit)][ranks.index(possible_hand[0][1])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][1])] == -1:
                permutations_cards += 0
            elif occur[suits.index(suit)][ranks.index(possible_hand[0][3])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][3])] == -1:
                permutations_cards += 0
            else:
                if occur[suits.index(suit)][ranks.index(possible_hand[0][2])] == 0:
                    remaining_card1 = 1
                    remaining_card2 = 1
                    remaining_card3 = remaining_cards_ranks[ranks.index(possible_hand[0][2])] - 1
                    remaining_card4 = 1
                    if remaining_card4<=0 or remaining_card3 <= 0 or remaining_card2<=0 or remaining_card1 <= 0:
                        permutations_cards += 0
                    else:
                        permutations_cards += (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
                else:
                    remaining_card1 = 1
                    remaining_card2 = 1
                    remaining_card3 = remaining_cards_ranks[ranks.index(possible_hand[0][2])]
                    remaining_card4 = 1
                    if remaining_card4==0 or remaining_card3 == 0 or remaining_card2==0 or remaining_card1 == 0:
                        permutations_cards += 0
                    else:
                        permutations_cards += (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
            
            if occur[suits.index(suit)][ranks.index(possible_hand[0][0])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][0])] == -1:
                permutations_cards += 0
            elif occur[suits.index(suit)][ranks.index(possible_hand[0][2])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][2])] == -1:
                permutations_cards += 0
            elif occur[suits.index(suit)][ranks.index(possible_hand[0][3])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][3])] == -1:
                permutations_cards += 0
            else:
                if occur[suits.index(suit)][ranks.index(possible_hand[0][1])] == 0:
                    remaining_card1 = 1
                    remaining_card2 = remaining_cards_ranks[ranks.index(possible_hand[0][1])] - 1
                    remaining_card3 = 1
                    remaining_card4 = 1
                    if remaining_card4<=0 or remaining_card3 <= 0 or remaining_card2<=0 or remaining_card1 <= 0:
                        permutations_cards += 0
                    else:
                        permutations_cards += (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
                else:
                    remaining_card1 = 1
                    remaining_card2 = remaining_cards_ranks[ranks.index(possible_hand[0][1])]
                    remaining_card3 = 1
                    remaining_card4 = 1
                    if remaining_card4==0 or remaining_card3 == 0 or remaining_card2==0 or remaining_card1 == 0:
                        permutations_cards += 0
                    else:
                        permutations_cards += (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1

            if occur[suits.index(suit)][ranks.index(possible_hand[0][1])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][1])] == -1:
                permutations_cards += 0
            elif occur[suits.index(suit)][ranks.index(possible_hand[0][2])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][2])] == -1:
                permutations_cards += 0
            elif occur[suits.index(suit)][ranks.index(possible_hand[0][3])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][3])] == -1:
                permutations_cards += 0
            else:
                if occur[suits.index(suit)][ranks.index(possible_hand[0][0])] == 0:
                    remaining_card1 = remaining_cards_ranks[ranks.index(possible_hand[0][0])] - 1
                    remaining_card2 = 1
                    remaining_card3 = 1
                    remaining_card4 = 1
                    if remaining_card4<=0 or remaining_card3 <= 0 or remaining_card2<=0 or remaining_card1 <= 0:
                        permutations_cards += 0
                    else:
                        permutations_cards += (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
                else:
                    remaining_card1 = remaining_cards_ranks[ranks.index(possible_hand[0][0])] - 1
                    remaining_card2 = 1
                    remaining_card3 = 1
                    remaining_card4 = 1
                    if remaining_card4==0 or remaining_card3 == 0 or remaining_card2==0 or remaining_card1 == 0:
                        permutations_cards += 0
                    else:
                        permutations_cards += (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1

            if occur[suits.index(suit)][ranks.index(possible_hand[0][0])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][0])] == -1:
                            permutations_cards += 0
            elif occur[suits.index(suit)][ranks.index(possible_hand[0][1])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][1])] == -1:
                permutations_cards += 0
            else:
                if occur[suits.index(suit)][ranks.index(possible_hand[0][2])] == 0 and occur[suits.index(suit)][ranks.index(possible_hand[0][3])] == 0:
                    remaining_card1 = 1
                    remaining_card2 = 1
                    remaining_card3 = remaining_cards_ranks[ranks.index(possible_hand[0][2])] - 1
                    remaining_card4 = remaining_cards_ranks[ranks.index(possible_hand[0][3])] - 1
                    if remaining_card4<=0 or remaining_card3 <= 0 or remaining_card2<=0 or remaining_card1 <= 0:
                        permutations_cards += 0
                    else:
                        permutations_cards += (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
                elif occur[suits.index(suit)][ranks.index(possible_hand[0][2])] == 0 and occur[suits.index(suit)][ranks.index(possible_hand[0][3])] != 0:
                    remaining_card1 = 1
                    remaining_card2 = 1
                    remaining_card3 = remaining_cards_ranks[ranks.index(possible_hand[0][2])] - 1
                    remaining_card4 = remaining_cards_ranks[ranks.index(possible_hand[0][3])]
                    if remaining_card4<=0 or remaining_card3 <= 0 or remaining_card2<=0 or remaining_card1 <= 0:
                        permutations_cards += 0
                    else:
                        permutations_cards += (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
                elif occur[suits.index(suit)][ranks.index(possible_hand[0][2])] != 0 and occur[suits.index(suit)][ranks.index(possible_hand[0][3])] == 0:
                    remaining_card1 = 1
                    remaining_card2 = 1
                    remaining_card3 = remaining_cards_ranks[ranks.index(possible_hand[0][2])] 
                    remaining_card4 = remaining_cards_ranks[ranks.index(possible_hand[0][3])] -1
                    if remaining_card4<=0 or remaining_card3 <= 0 or remaining_card2<=0 or remaining_card1 <= 0:
                        permutations_cards += 0
                    else:
                        permutations_cards += (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
                
                else:
                    remaining_card1 = 1
                    remaining_card2 = 1
                    remaining_card3 = remaining_cards_ranks[ranks.index(possible_hand[0][2])] 
                    remaining_card4 = remaining_cards_ranks[ranks.index(possible_hand[0][3])] 
                    if remaining_card4==0 or remaining_card3 == 0 or remaining_card2==0 or remaining_card1 == 0:
                        permutations_cards += 0
                    else:
                        permutations_cards += (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1

            if occur[suits.index(suit)][ranks.index(possible_hand[0][0])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][0])] == -1:
                permutations_cards += 0
            elif occur[suits.index(suit)][ranks.index(possible_hand[0][3])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][3])] == -1:
                permutations_cards += 0
            else:
                if occur[suits.index(suit)][ranks.index(possible_hand[0][1])] == 0 and occur[suits.index(suit)][ranks.index(possible_hand[0][2])] == 0:
                    remaining_card1 = 1
                    remaining_card2 =  remaining_cards_ranks[ranks.index(possible_hand[0][1])] - 1
                    remaining_card3 = remaining_cards_ranks[ranks.index(possible_hand[0][2])] - 1
                    remaining_card4 = 1
                    if remaining_card4<=0 or remaining_card3 <= 0 or remaining_card2<=0 or remaining_card1 <= 0:
                        permutations_cards += 0
                    else:
                        permutations_cards += (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
                elif occur[suits.index(suit)][ranks.index(possible_hand[0][1])] == 0 and occur[suits.index(suit)][ranks.index(possible_hand[0][2])] != 0:
                    remaining_card1 = 1
                    remaining_card2 =  remaining_cards_ranks[ranks.index(possible_hand[0][1])] - 1
                    remaining_card3 = remaining_cards_ranks[ranks.index(possible_hand[0][2])] 
                    remaining_card4 = 1
                    if remaining_card4<=0 or remaining_card3 <= 0 or remaining_card2<=0 or remaining_card1 <= 0:
                        permutations_cards += 0
                    else:
                        permutations_cards += (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
                elif occur[suits.index(suit)][ranks.index(possible_hand[0][1])] != 0 and occur[suits.index(suit)][ranks.index(possible_hand[0][2])] == 0:
                    remaining_card1 = 1
                    remaining_card2 =  remaining_cards_ranks[ranks.index(possible_hand[0][1])] - 1
                    remaining_card3 = remaining_cards_ranks[ranks.index(possible_hand[0][2])] 
                    remaining_card4 = 1
                    if remaining_card4<=0 or remaining_card3 <= 0 or remaining_card2<=0 or remaining_card1 <= 0:
                        permutations_cards += 0
                    else:
                        permutations_cards += (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
                
                else:
                    remaining_card1 = 1
                    remaining_card2 =  remaining_cards_ranks[ranks.index(possible_hand[0][1])] 
                    remaining_card3 = remaining_cards_ranks[ranks.index(possible_hand[0][2])] 
                    remaining_card4 = 1 
                    if remaining_card4==0 or remaining_card3 == 0 or remaining_card2==0 or remaining_card1 == 0:
                        permutations_cards += 0
                    else:
                        permutations_cards += (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
                
            if occur[suits.index(suit)][ranks.index(possible_hand[0][2])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][2])] == -1:
                permutations_cards += 0
            elif occur[suits.index(suit)][ranks.index(possible_hand[0][3])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][3])] == -1:
                permutations_cards += 0
            else:
                if occur[suits.index(suit)][ranks.index(possible_hand[0][0])] == 0 and occur[suits.index(suit)][ranks.index(possible_hand[0][1])] == 0:
                    remaining_card1 =  remaining_cards_ranks[ranks.index(possible_hand[0][0])] - 1
                    remaining_card2 =  remaining_cards_ranks[ranks.index(possible_hand[0][1])] - 1
                    remaining_card3 =1
                    remaining_card4 = 1
                    if remaining_card4<=0 or remaining_card3 <= 0 or remaining_card2<=0 or remaining_card1 <= 0:
                        permutations_cards += 0
                    else:
                        permutations_cards += (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
                elif occur[suits.index(suit)][ranks.index(possible_hand[0][0])] == 0 and occur[suits.index(suit)][ranks.index(possible_hand[0][1])] != 0:
                    remaining_card1 =  remaining_cards_ranks[ranks.index(possible_hand[0][0])] - 1
                    remaining_card2 =  remaining_cards_ranks[ranks.index(possible_hand[0][1])] 
                    remaining_card3 =1
                    remaining_card4 = 1
                    if remaining_card4<=0 or remaining_card3 <= 0 or remaining_card2<=0 or remaining_card1 <= 0:
                        permutations_cards += 0
                    else:
                        permutations_cards += (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
                elif occur[suits.index(suit)][ranks.index(possible_hand[0][0])] != 0 and occur[suits.index(suit)][ranks.index(possible_hand[0][1])] == 0:
                    remaining_card1 =  remaining_cards_ranks[ranks.index(possible_hand[0][0])] 
                    remaining_card2 =  remaining_cards_ranks[ranks.index(possible_hand[0][1])] - 1 
                    remaining_card3 = 1
                    remaining_card4 = 1
                    if remaining_card4<=0 or remaining_card3 <= 0 or remaining_card2<=0 or remaining_card1 <= 0:
                        permutations_cards += 0
                    else:
                        permutations_cards += (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
                
                else:
                    remaining_card1 =  remaining_cards_ranks[ranks.index(possible_hand[0][0])] 
                    remaining_card2 =  remaining_cards_ranks[ranks.index(possible_hand[0][1])]
                    remaining_card3 = 1
                    remaining_card4 = 1
                    if remaining_card4==0 or remaining_card3 == 0 or remaining_card2==0 or remaining_card1 == 0:
                        permutations_cards += 0
                    else:
                        permutations_cards += (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1

            if occur[suits.index(suit)][ranks.index(possible_hand[0][0])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][0])] == -1:
                permutations_cards += 0
            elif occur[suits.index(suit)][ranks.index(possible_hand[0][2])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][2])] == -1:
                permutations_cards += 0
            else:
                if occur[suits.index(suit)][ranks.index(possible_hand[0][1])] == 0 and occur[suits.index(suit)][ranks.index(possible_hand[0][3])] == 0:
                    remaining_card1 =  1
                    remaining_card2 =  remaining_cards_ranks[ranks.index(possible_hand[0][1])] - 1
                    remaining_card3 =1
                    remaining_card4 = remaining_cards_ranks[ranks.index(possible_hand[0][3])] - 1
                    if remaining_card4<=0 or remaining_card3 <= 0 or remaining_card2<=0 or remaining_card1 <= 0:
                        permutations_cards += 0
                    else:
                        permutations_cards += (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
                elif occur[suits.index(suit)][ranks.index(possible_hand[0][1])] == 0 and occur[suits.index(suit)][ranks.index(possible_hand[0][3])] != 0:
                    remaining_card1 =  1
                    remaining_card2 =  remaining_cards_ranks[ranks.index(possible_hand[0][1])] - 1
                    remaining_card3 =1
                    remaining_card4 = remaining_cards_ranks[ranks.index(possible_hand[0][3])] 
                    if remaining_card4<=0 or remaining_card3 <= 0 or remaining_card2<=0 or remaining_card1 <= 0:
                        permutations_cards += 0
                    else:
                        permutations_cards += (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
                elif occur[suits.index(suit)][ranks.index(possible_hand[0][1])] != 0 and occur[suits.index(suit)][ranks.index(possible_hand[0][3])] == 0:
                    remaining_card1 =  1
                    remaining_card2 =  remaining_cards_ranks[ranks.index(possible_hand[0][1])]
                    remaining_card3 =1
                    remaining_card4 = remaining_cards_ranks[ranks.index(possible_hand[0][3])] - 1
                    if remaining_card4<=0 or remaining_card3 <= 0 or remaining_card2<=0 or remaining_card1 <= 0:
                        permutations_cards += 0
                    else:
                        permutations_cards += (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
                
                else:
                    remaining_card1 =  1
                    remaining_card2 =  remaining_cards_ranks[ranks.index(possible_hand[0][1])]
                    remaining_card3 =1
                    remaining_card4 = remaining_cards_ranks[ranks.index(possible_hand[0][3])] 
                    if remaining_card4==0 or remaining_card3 == 0 or remaining_card2==0 or remaining_card1 == 0:
                        permutations_cards += 0
                    else:
                        permutations_cards += (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1

            if occur[suits.index(suit)][ranks.index(possible_hand[0][1])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][1])] == -1:
                permutations_cards += 0
            elif occur[suits.index(suit)][ranks.index(possible_hand[0][3])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][3])] == -1:
                permutations_cards += 0
            else:
                if occur[suits.index(suit)][ranks.index(possible_hand[0][0])] == 0 and occur[suits.index(suit)][ranks.index(possible_hand[0][2])] == 0:
                    remaining_card1 =  remaining_cards_ranks[ranks.index(possible_hand[0][0])] - 1
                    remaining_card2 =  1
                    remaining_card3 =remaining_cards_ranks[ranks.index(possible_hand[0][2])] -1
                    remaining_card4 = 1
                    if remaining_card4<=0 or remaining_card3 <= 0 or remaining_card2<=0 or remaining_card1 <= 0:
                        permutations_cards += 0
                    else:
                        permutations_cards += (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
                elif occur[suits.index(suit)][ranks.index(possible_hand[0][0])] == 0 and occur[suits.index(suit)][ranks.index(possible_hand[0][2])] != 0:
                    remaining_card1 =  remaining_cards_ranks[ranks.index(possible_hand[0][0])] - 1
                    remaining_card2 =  1
                    remaining_card3 =remaining_cards_ranks[ranks.index(possible_hand[0][2])] 
                    remaining_card4 = 1
                    if remaining_card4<=0 or remaining_card3 <= 0 or remaining_card2<=0 or remaining_card1 <= 0:
                        permutations_cards += 0
                    else:
                        permutations_cards += (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
                elif occur[suits.index(suit)][ranks.index(possible_hand[0][0])] != 0 and occur[suits.index(suit)][ranks.index(possible_hand[0][2])] == 0:
                    remaining_card1 =  remaining_cards_ranks[ranks.index(possible_hand[0][0])] 
                    remaining_card2 =  1
                    remaining_card3 =remaining_cards_ranks[ranks.index(possible_hand[0][2])] -1
                    remaining_card4 = 1
                    if remaining_card4<=0 or remaining_card3 <= 0 or remaining_card2<=0 or remaining_card1 <= 0:
                        permutations_cards += 0
                    else:
                        permutations_cards += (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
                
                else:
                    remaining_card1 =  remaining_cards_ranks[ranks.index(possible_hand[0][0])] 
                    remaining_card2 =  1
                    remaining_card3 =remaining_cards_ranks[ranks.index(possible_hand[0][2])]
                    remaining_card4 = 1
                    if remaining_card4==0 or remaining_card3 == 0 or remaining_card2==0 or remaining_card1 == 0:
                        permutations_cards += 0
                    else:
                        permutations_cards += (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1

            if occur[suits.index(suit)][ranks.index(possible_hand[0][1])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][1])] == -1:
                permutations_cards += 0
            elif occur[suits.index(suit)][ranks.index(possible_hand[0][2])] == 1 or occur[suits.index(suit)][ranks.index(possible_hand[0][2])] == -1:
                permutations_cards += 0
            else:
                if occur[suits.index(suit)][ranks.index(possible_hand[0][0])] == 0 and occur[suits.index(suit)][ranks.index(possible_hand[0][3])] == 0:
                    remaining_card1 =  remaining_cards_ranks[ranks.index(possible_hand[0][0])] - 1
                    remaining_card2 =  1
                    remaining_card3 =1
                    remaining_card4 = remaining_cards_ranks[ranks.index(possible_hand[0][3])] -1
                    if remaining_card4<=0 or remaining_card3 <= 0 or remaining_card2<=0 or remaining_card1 <= 0:
                        permutations_cards += 0
                    else:
                        permutations_cards += (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
                elif occur[suits.index(suit)][ranks.index(possible_hand[0][0])] == 0 and occur[suits.index(suit)][ranks.index(possible_hand[0][3])] != 0:
                    remaining_card1 =  remaining_cards_ranks[ranks.index(possible_hand[0][0])] - 1
                    remaining_card2 =  1
                    remaining_card3 =1
                    remaining_card4 = remaining_cards_ranks[ranks.index(possible_hand[0][3])]
                    if remaining_card4<=0 or remaining_card3 <= 0 or remaining_card2<=0 or remaining_card1 <= 0:
                        permutations_cards += 0
                    else:
                        permutations_cards += (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
                elif occur[suits.index(suit)][ranks.index(possible_hand[0][0])] != 0 and occur[suits.index(suit)][ranks.index(possible_hand[0][3])] == 0:
                    remaining_card1 =  remaining_cards_ranks[ranks.index(possible_hand[0][0])] 
                    remaining_card2 =  1
                    remaining_card3 =1
                    remaining_card4 = remaining_cards_ranks[ranks.index(possible_hand[0][3])] -1 
                    if remaining_card4<=0 or remaining_card3 <= 0 or remaining_card2<=0 or remaining_card1 <= 0:
                        permutations_cards += 0
                    else:
                        permutations_cards += (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
                
                else:
                    remaining_card1 =  remaining_cards_ranks[ranks.index(possible_hand[0][0])]
                    remaining_card2 =  1
                    remaining_card3 =1
                    remaining_card4 = remaining_cards_ranks[ranks.index(possible_hand[0][3])]
                    if remaining_card4==0 or remaining_card3 == 0 or remaining_card2==0 or remaining_card1 == 0:
                        permutations_cards += 0
                    else:
                        permutations_cards += (remaining_card1+remaining_card2+remaining_card3+remaining_card4)*(remaining_card1+remaining_card2+remaining_card3)*(remaining_card1+remaining_card2)*remaining_card1
            return permutations_cards/permutations
        else:
            return 0
    else:
        return 0