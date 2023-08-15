
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
def count_cards_having_by_ranks(hand):
    count_rank_all_hand = [0,0,0,0,0,0,0,0,0,0,0,0,0]
    ranks = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
    for card in hand:
        count_rank_all_hand[ranks.index(card[:-1])] = count_rank_all_hand[ranks.index(card[:-1])] + 1
    return count_rank_all_hand
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
                                all_possible_hand.append([hand,1*(remaining_cards_ranks[i]*(remaining_cards_ranks[i]-1)*(remaining_cards_ranks[i]-2)*(remaining_cards_ranks[i]-3)),count_rank_current_hand,count_rank_possible_hand,count_rank_all_hand])


                            elif card1 != card2 and card1 != card3 and card2 != card3 and card1!=card4 and card2!=card4 and card3!=card4 :
                                all_possible_hand.append([hand,24*(remaining_cards_ranks[i]*remaining_cards_ranks[j]*remaining_cards_ranks[k]*remaining_cards_ranks[l]),count_rank_current_hand,count_rank_possible_hand,count_rank_all_hand])

                            elif (card1 == card2 and card2 == card3 and card1 != card4) or (card1 == card2 and card2 == card4 and card1 != card3) or (card1 == card3 and card3 == card4 and card1 != card2)  or (card2 == card3 and card3 == card4 and card1 != card2):
                                if (card1 == card2 and card2 == card3 and card1 != card4):
                                    all_possible_hand.append([hand,4*remaining_cards_ranks[i]*(remaining_cards_ranks[i]-1)*(remaining_cards_ranks[i]-2)*remaining_cards_ranks[l],count_rank_current_hand,count_rank_possible_hand,count_rank_all_hand])
                                elif (card1 == card2 and card2 == card4 and card1 != card3):
                                    all_possible_hand.append([hand,4*remaining_cards_ranks[i]*(remaining_cards_ranks[i]-1)*(remaining_cards_ranks[i]-2)*remaining_cards_ranks[k],count_rank_current_hand,count_rank_possible_hand,count_rank_all_hand])
                                elif (card1 == card3 and card3 == card4 and card1 != card2):
                                    all_possible_hand.append([hand,4*remaining_cards_ranks[i]*(remaining_cards_ranks[i]-1)*(remaining_cards_ranks[i]-2)*remaining_cards_ranks[j],count_rank_current_hand,count_rank_possible_hand,count_rank_all_hand])
                                else: #(card2 == card3 and card3 == card4 and card1 != card2):
                                    all_possible_hand.append([hand,4*remaining_cards_ranks[i]*(remaining_cards_ranks[l]-1)*(remaining_cards_ranks[l]-2)*remaining_cards_ranks[l],count_rank_current_hand,count_rank_possible_hand,count_rank_all_hand])


                            elif (card1 == card2 and card3 == card4) or (card1 == card3 and card2 == card4) or (card1 == card4 and card3 == card2):
                                if (card1 == card2 and card3 == card4):
                                    all_possible_hand.append([hand,6*remaining_cards_ranks[i]*(remaining_cards_ranks[i]-1)*remaining_cards_ranks[k]*(remaining_cards_ranks[k]-1),count_rank_current_hand,count_rank_possible_hand,count_rank_all_hand])
                                elif (card1 == card3 and card2 == card4):
                                    all_possible_hand.append([hand,6*remaining_cards_ranks[i]*(remaining_cards_ranks[i]-1)*remaining_cards_ranks[j]*(remaining_cards_ranks[j]-1),count_rank_current_hand,count_rank_possible_hand,count_rank_all_hand])
                                else:#(card1 == card4 and card3 == card2)
                                    all_possible_hand.append([hand,6*remaining_cards_ranks[i]*(remaining_cards_ranks[i]-1)*remaining_cards_ranks[j]*(remaining_cards_ranks[j]-1),count_rank_current_hand,count_rank_possible_hand,count_rank_all_hand])

                            else:
                                if (card1 == card2 ):
                                    all_possible_hand.append([hand,12*remaining_cards_ranks[i]*(remaining_cards_ranks[i]-1)*remaining_cards_ranks[k]*remaining_cards_ranks[l],count_rank_current_hand,count_rank_possible_hand,count_rank_all_hand])
                                elif (card1 == card3 ):
                                    all_possible_hand.append([hand,12*remaining_cards_ranks[i]*(remaining_cards_ranks[i]-1)*remaining_cards_ranks[j]*remaining_cards_ranks[l],count_rank_current_hand,count_rank_possible_hand,count_rank_all_hand])
                                elif (card1 == card4):
                                    all_possible_hand.append([hand,12*remaining_cards_ranks[i]*(remaining_cards_ranks[i]-1)*remaining_cards_ranks[k]*remaining_cards_ranks[j],count_rank_current_hand,count_rank_possible_hand,count_rank_all_hand])
                                elif (card2 == card3):
                                    all_possible_hand.append([hand,12*remaining_cards_ranks[j]*(remaining_cards_ranks[j]-1)*remaining_cards_ranks[i]*remaining_cards_ranks[l],count_rank_current_hand,count_rank_possible_hand,count_rank_all_hand])
                                elif (card2 == card4):
                                    all_possible_hand.append([hand,12*remaining_cards_ranks[j]*(remaining_cards_ranks[j]-1)*remaining_cards_ranks[i]*remaining_cards_ranks[k],count_rank_current_hand,count_rank_possible_hand,count_rank_all_hand])
                                else:#(card3 == card4)
                                    all_possible_hand.append([hand,12*remaining_cards_ranks[k]*(remaining_cards_ranks[k]-1)*remaining_cards_ranks[i]*remaining_cards_ranks[j],count_rank_current_hand,count_rank_possible_hand,count_rank_all_hand])
                                
                            
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
                        if card1 == card2 and card2 == card3 and card3==card1:

                            all_possible_hand.append([hand,1*(remaining_cards_ranks[i])*(remaining_cards_ranks[i]-1)*(remaining_cards_ranks[i]-2),count_rank_current_hand,count_rank_possible_hand,count_rank_all_hand])
                        elif card1 != card2 and card1 != card3 and card2 != card3:
                            all_possible_hand.append([hand,6*(remaining_cards_ranks[i])*(remaining_cards_ranks[j])*(remaining_cards_ranks[k]),count_rank_current_hand,count_rank_possible_hand,count_rank_all_hand])
                        else:
                            if card1 == card2 :
                                all_possible_hand.append([hand,3*(remaining_cards_ranks[i])*(remaining_cards_ranks[i]-1)*(remaining_cards_ranks[k]),count_rank_current_hand,count_rank_possible_hand,count_rank_all_hand])
                            elif card2 == card3:
                                all_possible_hand.append([hand,3*(remaining_cards_ranks[j])*(remaining_cards_ranks[j]-1)*(remaining_cards_ranks[i]),count_rank_current_hand,count_rank_possible_hand,count_rank_all_hand])
                            else:#card3==card1:
                                all_possible_hand.append([hand,3*(remaining_cards_ranks[k])*(remaining_cards_ranks[k]-1)*(remaining_cards_ranks[j]),count_rank_current_hand,count_rank_possible_hand,count_rank_all_hand])
                    k+=1
                j+=1
            i+=1
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
                        all_possible_hand.append([hand,1*remaining_cards_ranks[i]*(remaining_cards_ranks[j]-1),count_rank_current_hand,count_rank_possible_hand,count_rank_all_hand])
                    else:
                        all_possible_hand.append([hand,2*remaining_cards_ranks[i]*remaining_cards_ranks[j],count_rank_current_hand,count_rank_possible_hand,count_rank_all_hand])
                j+=1
            i+=1
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
                all_possible_hand.append([hand,1*remaining_cards_ranks[i],count_rank_current_hand,count_rank_possible_hand,count_rank_all_hand])

            i+=1

    return all_possible_hand
def generate_hand_with_all_suit(current_hand, possible_hand,occur,index_straight):
    ranks = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
    suits = ['s','h','d','c']
    count_possible_hand = 0
    count_flush_hand = 0
    count_straight_hand = 0
    hand=[]
    if index_straight !=-1:
        straight = []
        if index_straight == 0:
            straight = ['T','J','Q','K','A']
        else:
            straight.append(ranks[index_straight])
            straight.append(ranks[index_straight-1])
            straight.append(ranks[index_straight-2])
            straight.append(ranks[index_straight-3])
            straight.append(ranks[index_straight-4])
        
    if len(current_hand) == 3:# 4 cards are remaining
        i=0
        j=0
        k=0
        l=0
        while i < 4:
            suit1 = suits[i]
            j = 0
            while j< 4:
                suit2 = suits[j]
                k= 0
                while k < 4:
                    suit3 = suits[k]
                    l= 0 
                    while l < 4:
                        count_suit_all_hand = [0,0,0,0]
                        count_suit_all_hand[suits.index(current_hand[0][1:])] =1 +count_suit_all_hand[suits.index(current_hand[0][1:])]
                        count_suit_all_hand[suits.index(current_hand[1][1:])] =1 +count_suit_all_hand[suits.index(current_hand[1][1:])]
                        count_suit_all_hand[suits.index(current_hand[2][1:])] =1 +count_suit_all_hand[suits.index(current_hand[2][1:])]
                        
                        suit4 = suits[l]
                        
                        hand = [possible_hand[0] + suit1,possible_hand[1] + suit2,possible_hand[2] + suit3,possible_hand[3] + suit4]
                       
                        if hand[0] != hand[1] and hand[0] != hand[2] and hand[0] != hand[3] and hand[1] !=hand[2] and hand[1] !=hand[3] and hand[1] !=hand[3] :
                            if occur[suits.index(suit1)][ranks.index(possible_hand[0])] == 0 and occur[suits.index(suit2)][ranks.index(possible_hand[1])] == 0 and occur[suits.index(suit3)][ranks.index(possible_hand[2])] == 0 and occur[suits.index(suit4)][ranks.index(possible_hand[3])] == 0:
                                count_possible_hand +=1
                                count_suit_all_hand[suits.index(suit1)]  = count_suit_all_hand[suits.index(suit1)] + 1
                                count_suit_all_hand[suits.index(suit2)] =1+ count_suit_all_hand[suits.index(suit2)]
                                count_suit_all_hand[suits.index(suit3)] =1+count_suit_all_hand[suits.index(suit3)]
                                count_suit_all_hand[suits.index(suit4)] =1+count_suit_all_hand[suits.index(suit4)]
                                
                                if count_suit_all_hand[0]>= 5 or count_suit_all_hand[1]>= 5 or count_suit_all_hand[2]>= 5 or count_suit_all_hand[3]>=5 :
                                    count_flush_hand +=1
                                    if index_straight !=-1:
                                        final_hand =current_hand + hand
                                        
                                        if count_suit_all_hand[0]>= 5:
                                            suit = suits[0]
                                            possible = True
                                            index_card=0
                                            while index_card<len(final_hand) and possible:
                                                if final_hand[index_card][:-1] in straight:
                                                    if final_hand[index_card][1:] !=suit:
                                                        possible =False
                                                index_card +=1
                                            if possible:
                                                count_straight_hand +=1
                                        elif count_suit_all_hand[1]>= 5:
                                            suit = suits[1]
                                            possible = True
                                            index_card=0
                                            while index_card<len(final_hand) and possible:
                                                if final_hand[index_card][:-1] in straight:
                                                    if final_hand[index_card][1:] !=suit:
                                                        possible =False
                                                index_card +=1
                                            if possible:
                                                count_straight_hand +=1
                                        elif count_suit_all_hand[2]>= 5:
                                            suit = suits[2]
                                            possible = True
                                            index_card=0
                                            while index_card<len(final_hand) and possible:
                                                if final_hand[index_card][:-1] in straight:
                                                    if final_hand[index_card][1:] !=suit:
                                                        possible =False
                                                index_card +=1
                                            if possible:
                                                count_straight_hand +=1
                                        else:
                                            suit = suits[3]
                                            possible = True
                                            index_card=0
                                            while index_card<len(final_hand) and possible:
                                                if final_hand[index_card][:-1] in straight:
                                                    if final_hand[index_card][1:] !=suit:
                                                        possible =False
                                                index_card +=1
                                            if possible:
                                                count_straight_hand +=1
                        l+=1
                    k+=1
                j+=1
            i+=1
        if index_straight == -1:
            return count_flush_hand/count_possible_hand
        else:
            return count_straight_hand/count_possible_hand
    elif len(current_hand) == 4:# 3 cards are remaining
        i=0
        j=0
        k=0
       
        
        while i < 4:
           
            suit1 = suits[i]
            j = 0
            while j< 4:
                suit2 = suits[j]
                k= 0
                while k < 4:
                    suit3 = suits[k]
                    
                    
                    count_suit_all_hand = [0,0,0,0]
                    count_suit_all_hand[suits.index(current_hand[0][1:])] =1 +count_suit_all_hand[suits.index(current_hand[0][1:])]
                    count_suit_all_hand[suits.index(current_hand[1][1:])] =1 +count_suit_all_hand[suits.index(current_hand[1][1:])]
                    count_suit_all_hand[suits.index(current_hand[2][1:])] =1 +count_suit_all_hand[suits.index(current_hand[2][1:])]
                    count_suit_all_hand[suits.index(current_hand[3][1:])] =1 +count_suit_all_hand[suits.index(current_hand[3][1:])]
                        
                    
                        
                    hand = [possible_hand[0] + suit1,possible_hand[1] + suit2,possible_hand[2] + suit3]
                       
                    if hand[0] != hand[1] and hand[0] != hand[2]  and hand[1] !=hand[2]:
                        if occur[suits.index(suit1)][ranks.index(possible_hand[0])] == 0 and occur[suits.index(suit2)][ranks.index(possible_hand[1])] == 0 and occur[suits.index(suit3)][ranks.index(possible_hand[2])] == 0:
                            count_possible_hand +=1
                            count_suit_all_hand[suits.index(suit1)]  = count_suit_all_hand[suits.index(suit1)] + 1
                            count_suit_all_hand[suits.index(suit2)] =1+ count_suit_all_hand[suits.index(suit2)]
                            count_suit_all_hand[suits.index(suit3)] =1+count_suit_all_hand[suits.index(suit3)] 

                            if count_suit_all_hand[0]>= 5 or count_suit_all_hand[1]>= 5 or count_suit_all_hand[2]>= 5 or count_suit_all_hand[3]>=5 :
                                count_flush_hand +=1
                                if index_straight !=-1:
                                    final_hand =current_hand + hand
                                    if count_suit_all_hand[0]>= 5:
                                        suit = suits[0]
                                        possible = True
                                        index_card=0
                                        while index_card<len(final_hand) and possible:
                                            if final_hand[index_card][:-1] in straight:
                                                if final_hand[index_card][1:] !=suit:
                                                    possible =False
                                            index_card +=1
                                        if possible:
                                            count_straight_hand +=1
                                    elif count_suit_all_hand[1]>= 5:
                                        suit = suits[1]
                                        possible = True
                                        index_card=0
                                        while index_card<len(final_hand) and possible:
                                            if final_hand[index_card][:-1] in straight:
                                                if final_hand[index_card][1:] !=suit:
                                                    possible =False
                                            index_card +=1
                                        if possible:
                                            count_straight_hand +=1
                                    elif count_suit_all_hand[2]>= 5:
                                        suit = suits[2]
                                        possible = True
                                        index_card=0
                                        while index_card<len(final_hand) and possible:
                                            if final_hand[index_card][:-1] in straight:
                                                if final_hand[index_card][1:] !=suit:
                                                    possible =False
                                            index_card +=1
                                        if possible:
                                            count_straight_hand +=1
                                    else:
                                        suit = suits[3]
                                        possible = True
                                        index_card=0
                                        while index_card<len(final_hand) and possible:
                                            if final_hand[index_card][:-1] in straight:
                                                if final_hand[index_card][1:] !=suit:
                                                    possible =False
                                            index_card +=1
                                        if possible:
                                            count_straight_hand +=1
                    k+=1
                j+=1
            i+=1
        if index_straight == -1:
            return count_flush_hand/count_possible_hand
        else:
            return count_straight_hand/count_possible_hand
        
    elif len(current_hand) == 5:# 2 cards are remaining
        i=0
        j=0
        while i < 4:
            
            suit1 = suits[i]
            j = 0
            while j< 4:
                suit2 = suits[j]
                
                    
                count_suit_all_hand = [0,0,0,0]
                count_suit_all_hand[suits.index(current_hand[0][1:])] =1 +count_suit_all_hand[suits.index(current_hand[0][1:])]
                count_suit_all_hand[suits.index(current_hand[1][1:])] =1 +count_suit_all_hand[suits.index(current_hand[1][1:])]
                count_suit_all_hand[suits.index(current_hand[2][1:])] =1 +count_suit_all_hand[suits.index(current_hand[2][1:])]
                count_suit_all_hand[suits.index(current_hand[3][1:])] =1 +count_suit_all_hand[suits.index(current_hand[3][1:])]
                count_suit_all_hand[suits.index(current_hand[4][1:])] =1 +count_suit_all_hand[suits.index(current_hand[4][1:])]
                if count_suit_all_hand[0]>= 5 or count_suit_all_hand[1]>= 5 or count_suit_all_hand[2]>= 5 or count_suit_all_hand[3]>=5 :
                    return 1
                    if index_straight !=-1:
                        final_hand =current_hand + hand
                        if count_suit_all_hand[0]>= 5:
                            suit = suits[0]
                            possible = True
                            index_card=0
                            while index_card<len(final_hand) and possible:
                                if final_hand[index_card][:-1] in straight:
                                    if final_hand[index_card][1:] !=suit:
                                        possible =False
                                index_card +=1
                            if possible:
                                return 1
                        elif count_suit_all_hand[1]>= 5:
                            suit = suits[1]
                            possible = True
                            index_card=0
                            while index_card<len(final_hand) and possible:
                                if final_hand[index_card][:-1] in straight:
                                    if final_hand[index_card][1:] !=suit:
                                        possible =False
                                index_card +=1
                            if possible:
                                return 1
                        elif count_suit_all_hand[2]>= 5:
                            suit = suits[2]
                            possible = True
                            index_card=0
                            while index_card<len(final_hand) and possible:
                                if final_hand[index_card][:-1] in straight:
                                    if final_hand[index_card][1:] !=suit:
                                        possible =False
                                index_card +=1
                            if possible:
                                return 1
                        else:
                            suit = suits[3]
                            possible = True
                            index_card=0
                            while index_card<len(final_hand) and possible:
                                if final_hand[index_card][:-1] in straight:
                                    if final_hand[index_card][1:] !=suit:
                                        possible =False
                                index_card +=1
                            if possible:
                                return 1

                hand = [possible_hand[0] + suit1,possible_hand[1] + suit2]
                if hand[0] != hand[1] :
                    if occur[suits.index(suit1)][ranks.index(possible_hand[0])] == 0 and occur[suits.index(suit2)][ranks.index(possible_hand[1])] == 0:
                        count_possible_hand +=1
                        count_suit_all_hand[suits.index(suit1)]  = count_suit_all_hand[suits.index(suit1)] + 1
                        count_suit_all_hand[suits.index(suit2)] =1+ count_suit_all_hand[suits.index(suit2)] 
                        if count_suit_all_hand[0]>= 5 or count_suit_all_hand[1]>= 5 or count_suit_all_hand[2]>= 5 or count_suit_all_hand[3]>=5 :
                            count_flush_hand +=1
                            if index_straight !=-1:
                                final_hand =current_hand + hand
                                if count_suit_all_hand[0]>= 5:
                                    suit = suits[0]
                                    possible = True
                                    index_card=0
                                    while index_card<len(final_hand) and possible:
                                        if final_hand[index_card][:-1] in straight:
                                            if final_hand[index_card][1:] !=suit:
                                                possible =False
                                        index_card +=1
                                    if possible:
                                        count_straight_hand +=1
                                elif count_suit_all_hand[1]>= 5:
                                    suit = suits[1]
                                    possible = True
                                    index_card=0
                                    while index_card<len(final_hand) and possible:
                                        if final_hand[index_card][:-1] in straight:
                                            if final_hand[index_card][1:] !=suit:
                                                possible =False
                                        index_card +=1
                                    if possible:
                                        count_straight_hand +=1
                                elif count_suit_all_hand[2]>= 5:
                                    suit = suits[2]
                                    possible = True
                                    index_card=0
                                    while index_card<len(final_hand) and possible:
                                        if final_hand[index_card][:-1] in straight:
                                            if final_hand[index_card][1:] !=suit:
                                                possible =False
                                        index_card +=1
                                    if possible:
                                        count_straight_hand +=1
                                else:
                                    suit = suits[3]
                                    possible = True
                                    index_card=0
                                    while index_card<len(final_hand) and possible:
                                        if final_hand[index_card][:-1] in straight:
                                            if final_hand[index_card][1:] !=suit:
                                                possible =False
                                        index_card +=1
                                    if possible:
                                        count_straight_hand +=1

                j+=1
            i+=1
        if index_straight == -1:
            return count_flush_hand/count_possible_hand
        else:
            return count_straight_hand/count_possible_hand
    elif len(current_hand) == 6:# 1 card is remaining
        i=0
        while i < 4:
            
            suit1 = suits[i]   
            count_suit_all_hand = [0,0,0,0]
            count_suit_all_hand[suits.index(current_hand[0][1:])] =1 +count_suit_all_hand[suits.index(current_hand[0][1:])]
            count_suit_all_hand[suits.index(current_hand[1][1:])] =1 +count_suit_all_hand[suits.index(current_hand[1][1:])]
            count_suit_all_hand[suits.index(current_hand[2][1:])] =1 +count_suit_all_hand[suits.index(current_hand[2][1:])]
            count_suit_all_hand[suits.index(current_hand[3][1:])] =1 +count_suit_all_hand[suits.index(current_hand[3][1:])]
            count_suit_all_hand[suits.index(current_hand[4][1:])] =1 +count_suit_all_hand[suits.index(current_hand[4][1:])]
            count_suit_all_hand[suits.index(current_hand[5][1:])] =1 +count_suit_all_hand[suits.index(current_hand[5][1:])]
            if count_suit_all_hand[0]>= 5 or count_suit_all_hand[1]>= 5 or count_suit_all_hand[2]>= 5 or count_suit_all_hand[3]>=5 :
                return 1
                if index_straight !=-1:
                    final_hand =current_hand + hand
                    if count_suit_all_hand[0]>= 5:
                        suit = suits[0]
                        possible = True
                        index_card=0
                        while index_card<len(final_hand) and possible:
                            if final_hand[index_card][:-1] in straight:
                                if final_hand[index_card][1:] !=suit:
                                    possible =False
                            index_card +=1
                        if possible:
                            return 1
                    elif count_suit_all_hand[1]>= 5:
                        suit = suits[1]
                        possible = True
                        index_card=0
                        while index_card<len(final_hand) and possible:
                            if final_hand[index_card][:-1] in straight:
                                if final_hand[index_card][1:] !=suit:
                                    possible =False
                            index_card +=1
                        if possible:
                            return 1
                    elif count_suit_all_hand[2]>= 5:
                        suit = suits[2]
                        possible = True
                        index_card=0
                        while index_card<len(final_hand) and possible:
                            if final_hand[index_card][:-1] in straight:
                                if final_hand[index_card][1:] !=suit:
                                    possible =False
                            index_card +=1
                        if possible:
                            return 1
                    else:
                        suit = suits[3]
                        possible = True
                        index_card=0
                        while index_card<len(final_hand) and possible:
                            if final_hand[index_card][:-1] in straight:
                                if final_hand[index_card][1:] !=suit:
                                    possible =False
                            index_card +=1
                        if possible:
                            return 1

            hand = [possible_hand[0] + suit1]
            if occur[suits.index(suit1)][ranks.index(hand[0][:-1])] == 0 :
                count_possible_hand +=1
                count_suit_all_hand[suits.index(suit1)]  = count_suit_all_hand[suits.index(suit1)] + 1
                
                if count_suit_all_hand[0]>= 5 or count_suit_all_hand[1]>= 5 or count_suit_all_hand[2]>= 5 or count_suit_all_hand[3]>=5 :
                    count_flush_hand +=1
                    if index_straight !=-1:
                        final_hand =current_hand + hand
                        if count_suit_all_hand[0]>= 5:
                            suit = suits[0]
                            possible = True
                            index_card=0
                            while index_card<len(final_hand) and possible:
                                if final_hand[index_card][:-1] in straight:
                                    if final_hand[index_card][1:] !=suit:
                                        possible =False
                                index_card +=1
                            if possible:
                                count_straight_hand +=1
                        elif count_suit_all_hand[1]>= 5:
                            suit = suits[1]
                            possible = True
                            index_card=0
                            while index_card<len(final_hand) and possible:
                                if final_hand[index_card][:-1] in straight:
                                    if final_hand[index_card][1:] !=suit:
                                        possible =False
                                index_card +=1
                            if possible:
                                count_straight_hand +=1
                        elif count_suit_all_hand[2]>= 5:
                            suit = suits[2]
                            possible = True
                            index_card=0
                            while index_card<len(final_hand) and possible:
                                if final_hand[index_card][:-1] in straight:
                                    if final_hand[index_card][1:] !=suit:
                                        possible =False
                                index_card +=1
                            if possible:
                                count_straight_hand +=1
                        else:
                            suit = suits[3]
                            possible = True
                            index_card=0
                            while index_card<len(final_hand) and possible:
                                if final_hand[index_card][:-1] in straight:
                                    if final_hand[index_card][1:] !=suit:
                                        possible =False
                                index_card +=1
                            if possible:
                                count_straight_hand +=1
            i+=1
            
        if index_straight == -1:
            return count_flush_hand/count_possible_hand
        else:
            return count_straight_hand/count_possible_hand
    else:
        if len(current_hand) > 6:
            count_suit_all_hand = [0,0,0,0]
            hand =[]
            count_suit_all_hand[suits.index(current_hand[0][1:])] =1 +count_suit_all_hand[suits.index(current_hand[0][1:])]
            count_suit_all_hand[suits.index(current_hand[1][1:])] =1 +count_suit_all_hand[suits.index(current_hand[1][1:])]
            count_suit_all_hand[suits.index(current_hand[2][1:])] =1 +count_suit_all_hand[suits.index(current_hand[2][1:])]
            count_suit_all_hand[suits.index(current_hand[3][1:])] =1 +count_suit_all_hand[suits.index(current_hand[3][1:])]
            count_suit_all_hand[suits.index(current_hand[4][1:])] =1 +count_suit_all_hand[suits.index(current_hand[4][1:])]
            count_suit_all_hand[suits.index(current_hand[5][1:])] =1 +count_suit_all_hand[suits.index(current_hand[5][1:])]
            if count_suit_all_hand[0]>= 5 or count_suit_all_hand[1]>= 5 or count_suit_all_hand[2]>= 5 or count_suit_all_hand[3]>=5 :
                if index_straight !=-1:
                    final_hand =current_hand + hand
                    if count_suit_all_hand[0]>= 5:
                        suit = suits[0]
                        possible = True
                        index_card=0
                        while index_card<len(final_hand) and possible:
                            if final_hand[index_card][:-1] in straight:
                                if final_hand[index_card][1:] !=suit:
                                    possible =False
                            index_card +=1
                        if possible:
                            return 1
                    elif count_suit_all_hand[1]>= 5:
                        suit = suits[1]
                        possible = True
                        index_card=0
                        while index_card<len(final_hand) and possible:
                            if final_hand[index_card][:-1] in straight:
                                if final_hand[index_card][1:] !=suit:
                                    possible =False
                            index_card +=1
                        if possible:
                            return 1
                    elif count_suit_all_hand[2]>= 5:
                        suit = suits[2]
                        possible = True
                        index_card=0
                        while index_card<len(final_hand) and possible:
                            if final_hand[index_card][:-1] in straight:
                                if final_hand[index_card][1:] !=suit:
                                    possible =False
                            index_card +=1
                        if possible:
                            return 1
                    else:
                        suit = suits[3]
                        possible = True
                        index_card=0
                        while index_card<len(final_hand) and possible:
                            if final_hand[index_card][:-1] in straight:
                                if final_hand[index_card][1:] !=suit:
                                    possible =False
                            index_card +=1
                        if possible:
                            return 1
                else:
                    return 1
            else: 
                return 0


     


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
        prob_royal_flush,rf_zero =0,0
        prob_straight_flush,sf_zero=0,0
        prob_four_of_Kind,fok_zero=0,0
        prob_full_house,fh_zero = 0,0
        prob_flush,f_zero=0,0
        prob_straight,s_zero = 0,0
        prob_three_of_kind,tok_zero = 0,0
        prob_two_pairs,tp_zero = 0,0
        prob_pair,p_zero = 0,0
        prob_high_card,h_zero = 0,0
        all_comb = 0
        odd_5low = 0.
        odd_6low = 0.
        odd_7low = 0.
        odd_8low = 0.
        have_5low = 0
        have_6low = 0
        have_7low = 0
        have_8low = 0
        current_hand = find_current_hand(occur)
        if len(current_hand) <7:
            lst_all_possibilities = generate_all_remaining_hand(current_hand,count_cards_remaining_by_rank(occur))
            for possibility in lst_all_possibilities: #[hand,combinaisons,count_rank_current_hand,count_rank_possible_hand,count_rank_all_hand,Bool]
                comb = possibility[1]
                lst_rank = possibility[4]
                lst_straight = have_straigth(lst_rank)
                all_comb+= comb
                prob_Royal_flush_hand = probability_Royal_flush(current_hand,possibility[0],lst_straight,occur)
                prob_straight_flush_hand = probability_straight_flush(current_hand,possibility[0],lst_straight,occur)
                prob_4kind_hand = probability_4Kind(lst_rank)
                if prob_4kind_hand == 0:
                    prob_full_house_hand = probability_Full_House(lst_rank)
                    if prob_full_house_hand == 0:
                        
                                
                        prob_flush_hand = generate_hand_with_all_suit(current_hand, possibility[0],occur,-1)
                        prob_flush_given_hand = prob_flush_hand 
                        if prob_flush_hand !=1 :
                            if prob_flush_hand != 0:
                                f_zero = 1
                            prob_flush += prob_flush_hand *comb
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
                                            h_zero = 1
                                        else:
                                            prob_pair +=prob_pair_hand * comb
                                            p_zero = 1
                                    else:
                                        prob_two_pairs +=prob_2pairs_hand * comb
                                        tp_zero = 1
                                else:
                                    prob_three_of_kind += prob_3kind_hand * comb
                                    tok_zero = 1
                            else:
                                prob_straight +=prob_straight_hand *comb
                                s_zero = 1
                        else:
                            prob_flush += prob_flush_hand *comb    
                            f_zero = 1
                    else:
                        prob_full_house += prob_full_house_hand * comb
                        fh_zero = 1

                else:
                    prob_four_of_Kind += comb  * prob_4kind_hand
                    fok_zero = 1
                
                    prob_straight_flush += comb  * prob_straight_flush_hand
                    if prob_straight_flush != 0:
                        sf_zero = 1
                
                    prob_royal_flush += comb  * prob_Royal_flush_hand
                    if prob_Royal_flush_hand !=0:
                        rf_zero = 1
                lst_low = have_low(lst_rank)
                odd_5low +=prob_5_low(lst_low)*comb
                if odd_5low !=0:
                    have_5low = 1
                odd_6low +=prob_6_low(lst_low)*comb
                if odd_6low !=0:
                    have_6low = 1
                odd_7low +=prob_7_low(lst_low)*comb
                if odd_7low !=0:
                    have_7low = 1
                odd_8low +=prob_8_low(lst_low)*comb
                if odd_8low !=0:
                    have_8low = 1
                print(lst_low,possibility[0])
            if all_comb != 0:
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
                odd_5low/=all_comb
                odd_6low/=all_comb
                odd_7low/=all_comb
                odd_8low/=all_comb



        else:
            lst_rank =  count_cards_having_by_ranks(current_hand)
            lst_straight = have_straigth(lst_rank)
            prob_Royal_flush_hand = probability_Royal_flush(current_hand,current_hand,lst_straight,occur)
            
            if prob_Royal_flush_hand == 0:
                prob_straight_flush_hand = probability_straight_flush(current_hand,current_hand,lst_straight,occur)
                if prob_straight_flush_hand == 0:
                    
                    prob_4kind_hand = probability_4Kind(lst_rank)
                    if prob_4kind_hand == 0:
                        prob_full_house_hand = probability_Full_House(lst_rank)
                        if prob_full_house_hand == 0:
                            #prob_flush_hand = probability_flush_given_hand(current_hand,possibility,occur,count_cards_remaining_by_rank(occur),list_numplayers)/comb
                            #prob_flush_given_hand = prob_flush_hand
                                
                            prob_flush_hand = generate_hand_with_all_suit(current_hand, current_hand,occur,-1)
                            prob_flush_given_hand = prob_flush_hand 
                            if prob_flush_hand !=1 :
                                if prob_flush_hand != 0:
                                    f_zero = 1
                                prob_flush += prob_flush_hand 
                                prob_straight_hand = probability_straight(lst_straight,prob_flush_given_hand)
                                if prob_straight_hand == 0:
                                    prob_3kind_hand = probability_3KIND(lst_rank,prob_flush_given_hand)
                                    if prob_3kind_hand == 0:
                                        prob_2pairs_hand = probability_2PAIRS(lst_rank,prob_flush_given_hand)
                                        if prob_2pairs_hand == 0:
                                            prob_pair_hand = probability_PAIR(lst_rank,prob_flush_given_hand)
                                            if prob_pair_hand == 0:
                                                prob_high_card_hand = probability_high_card(lst_rank,prob_flush_given_hand)
                                                prob_high_card +=prob_high_card_hand 
                                                h_zero = 1
                                            else:
                                                prob_pair +=prob_pair_hand 
                                                p_zero = 1
                                        else:
                                            prob_two_pairs +=prob_2pairs_hand 
                                            tp_zero = 1
                                    else:
                                        prob_three_of_kind += prob_3kind_hand 
                                        tok_zero = 1
                                        
                                else:
                                    prob_straight +=prob_straight_hand 
                                    s_zero = 1
                            else:
                                prob_flush += prob_flush_hand    
                                f_zero = 1
                        else:
                            prob_full_house += prob_full_house_hand 
                            fh_zero = 1

                    else:
                        prob_four_of_Kind += prob_4kind_hand
                        fok_zero = 1
                else:
                    prob_straight_flush += prob_straight_flush_hand
                    sf_zero = 1
            else:
                prob_royal_flush +=  prob_Royal_flush_hand
                rf_zero = 1
            lst_low = have_low(lst_rank)
            odd_5low +=prob_5_low(lst_low)
            if odd_5low !=0:
                have_5low = 1
            odd_6low +=prob_6_low(lst_low)
            if odd_6low !=0:
                have_6low = 1
            odd_7low +=prob_7_low(lst_low)
            if odd_7low !=0:
                have_7low = 1
            odd_8low +=prob_8_low(lst_low)
            if odd_8low !=0:
                have_8low = 1

        return ([['Royal Flush',prob_royal_flush,rf_zero],
                ['Straight Flush',prob_straight_flush,sf_zero],
                ['Four of Kind',prob_four_of_Kind,fok_zero],
                ['Full House',prob_full_house,fh_zero],
                ['Flush',prob_flush,f_zero],
                ['Straight',prob_straight,s_zero],
                ['Three of Kind',prob_three_of_kind,tok_zero],
                ['Two Pairs',prob_two_pairs,tp_zero],
                ["Pair",prob_pair,p_zero],
                ["High_card",prob_high_card,h_zero],
                ["Total",prob_royal_flush+prob_straight_flush+prob_four_of_Kind+prob_full_house+prob_high_card+prob_flush+prob_straight+prob_three_of_kind+prob_two_pairs+prob_pair,1]],
                [["5-Low",odd_5low,have_5low],
                 ["6-Low",odd_6low,have_6low],
                 ["7-Low",odd_7low,have_7low],
                 ["8-Low",odd_8low,have_8low],
                 ["Total",odd_5low+odd_6low+odd_7low+odd_8low,1]]
        )



def probability_Royal_flush(current_hand,possible_hand,lst_straight,occur):
    prob_st_flush = 0
    if lst_straight[0] == 1 :
        prob_st_flush = generate_hand_with_all_suit(current_hand, possible_hand,occur,0)
    return prob_st_flush

def probability_straight_flush(current_hand,possible_hand,lst_straight,occur):
    prob_st_flush = 0
    for i in range (1,13):
        if lst_straight[i] == 1 :
            prob_st_flush += generate_hand_with_all_suit(current_hand, possible_hand,occur,i)
    return prob_st_flush


def have_low(lst_rank):
    lst_low = [0,0,0,0]
    low_cards = 0
    for i in range (4,8):
        low_cards = 0
        for j in range(0,i+1):
            if lst_rank[j] !=0 :
                low_cards+=1
        print(low_cards,lst_rank)
        if  low_cards >=5:
            lst_low[i-4] = 1
    return lst_low
def prob_5_low(lst_low):
    if lst_low[0] == 1:
        return 1
    else:
        return 0
def prob_6_low(lst_low):
    if lst_low[0] == 0 and lst_low[1] == 1:
                
        return 1
    else:
        return 0
def prob_7_low(lst_low):
    if lst_low[0] == 0 and lst_low[1] == 0 and lst_low[2] == 1:
        return 1
    else:
        return 0
def prob_8_low(lst_low):
    if lst_low[0] == 0 and lst_low[1] == 0 and lst_low[2] == 0 and lst_low[3] == 1:
                
        return 1
    else:
        return 0
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