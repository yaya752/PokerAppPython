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

def pair_4th(hand,aggresive_prec,aggressive):
    result = False
    if aggressive != -1 :
        if hand[0][:-1] == 'T' or hand[0][:-1] == 'J' or hand[0][:-1] == 'Q' or hand[0][:-1] == 'K' or hand[0][:-1] == 'A':
            if aggresive_prec >= 2:
                result = True
    return result

def brelan_4th(hand,aggressive_prec, aggressive):
    result = False
    if aggressive != -1 :
        if hand[0][:-1] == 'T' or hand[0][:-1] == 'J' or hand[0][:-1] == 'Q' or hand[0][:-1] == 'K' or hand[0][:-1] == 'A':
                if hand[0][:-1] == hand[1][:-1]:
                    if aggressive_prec < 2 and aggressive >= 2 :
                        result = True
    return result

def flush_4th(hand,aggressive):
    result = False
    if aggressive != -1 :
        if hand[0][:-1] == hand[1][:-1]:
            result = True
    return result

def quiz_4th(decision,tab_player,tab_prec_player,main_player):
    player_name = []
    player_possibilities =[]
    round2 = 0
    for i in range (0, len (tab_player)):
        player = tab_player[i]
        aggressive = player[3]
        j = index_poss(player[0],tab_prec_player)
        aggressive_prec = tab_prec_player[j][3]
        print(tab_player)
        if player[0] != main_player:
            if player[0] in player_name:
                hand = player[1]
                if round2 == 0:
                    decision.append(player_possibilities)
                    player_possibilities = []
                if flush_4th(hand):
                    player_possibilities.append([player[0],Card_To_Html(hand),'might have flush'])
                elif brelan_4th(hand,aggressive_prec, aggressive):
                    player_possibilities.append([player[0],Card_To_Html(hand),'might have brelan'])
                elif pair_4th(hand,aggressive_prec):
                    player_possibilities.append([player[0],Card_To_Html(hand),'might have pair'])
                elif aggressive == -1:
                    player_possibilities.append([player[0],Card_To_Html(hand),'folded'])
                else:
                    player_possibilities.append([player[0],Card_To_Html(hand),'might have low'])
            else:
                hand = player[1]
                if flush_4th(hand,aggressive):
                    player_possibilities.append([player[0],Card_To_Html(hand),'might have flush'])
                elif brelan_4th(hand,aggressive_prec, aggressive):
                    player_possibilities.append([player[0],Card_To_Html(hand),'might have brelan'])
                elif pair_4th(hand,aggressive_prec,aggressive):
                    player_possibilities.append([player[0],Card_To_Html(hand),'might have pair'])
                elif aggressive == -1:
                    player_possibilities.append([player[0],Card_To_Html(hand),'folded'])
                else:
                    player_possibilities.append([player[0],Card_To_Html(hand),'might have low'])
    decision.append(player_possibilities)
def odd_full_house(occur):
    odd = 0
    column = -1
    column1 = -1
    count = 0
    for j in range(0,13):
        if occur[5][j] == 1:
            column = j
        elif occur[4][j] == 1 and occur[5][j] != 1:
            column1 = j
    for j in range(0,13):
        if occur[4][j] == 1 and j != column and column != -1:
            return  1
        elif j != column and column != -1:
            odd += occur[4][j]
            count +=1
        if occur[5][j] == 1 and j != column1 and column1 != -1:
            return  1
        elif j != column1 and column1 != -1:
            odd += occur[5][j]
            count +=1
    return odd/count
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
        