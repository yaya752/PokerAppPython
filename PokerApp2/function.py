'''
Function Name: Generalities

Parameters:
 - line : first line of one of a file game of a tournament
        (this file has to be put in the " Game_File" folder)

Returns: 
 - gene : list of generalitites about the games
Description:
    allow to get the date, the tournament id and the hand id
'''


def Generalities(line):
    gene = []
    words = line.split()
    gene.append(words[2])
    gene.append(words[4])
    gene.append(words[17:19])
    return gene
def file_index(game_file):
    file_name ='Game_File\\' + game_file
    lines = []
    i = 0
    with open(file_name, "r") as f:
        for line in f:
            lines.append(line.strip())
        street_index = []
        
        for line in lines:
            if line[:5] == '*** 3':

                street_index.append(i)
            elif line[:5] == '*** 4':

                street_index.append(i)
            elif line[:5] == '*** 5':

                street_index.append(i)
            elif line[:5] == '*** 6':

                street_index.append(i)
            elif line[:5] == '*** R':

                street_index.append(i)
            elif line[:6] == '*** SH':

                street_index.append(i)
            elif line[:6] == '*** SU':
                idSummary = i
                street_index.append(i)
            i+=1
    return (lines,street_index)
'''
Function Name: raises

Parameters:
 - Sum : get the amount of chips put by on the table when he raised

Returns: 
 - Sum
Description:
    When a player raised the way we calculate the amount of chips put on the table
    is determined by what the players have done befire
'''
def raises(index,lines,player):
    Sum = 0
    i = index
    print(lines[i])
    while lines[i][:3] !="***" and i > 0:
        words = lines[i].split()
        print(lines[i])
        if words[1] == "raises" and words[0] == player + ':':
            Sum +=int(words[4])
            while lines[i][:3] !="***" and i > 0:
                if words[0] == player + ":":
                    if words[1] == 'brings':
                        Sum-= int(words[4])
                    elif words[1] == 'calls':
                        Sum-= int(words[2])
                    elif words[1] == 'bets':
                        Sum-= int(words[2])
                i-=1
        i-=1
    return Sum

'''
Function Name: Count_Chips

Parameters:
 - Sum

Returns: 
 - Sum : How much a player put chips
Description:
    calculate how much a player put chips during the game 
'''
def Count_Chips(main_player,lines, idSummary):
    Sum = 0
    i = 0
    words = lines[i].split()
    while i < idSummary:        
        words = lines[i].split()
        if words[1] == 'posts' and words[0] == main_player + ":":
            Sum += int(words[4])
        elif words[0] == main_player + ":":
            if words[1] == 'brings':
                Sum+= int(words[4])
            elif words[1] == 'calls':
                Sum+= int(words[2])
            elif words[1] == 'bets':
                Sum+= int(words[2])
            elif words[1] == 'raises':
                Sum+= raises(i,lines,main_player)
            elif words[1] == "folds" or words[1] == "mucks":
                Sum =-Sum
                i = idSummary
        i+=1
    return Sum
'''
Function Name: average

Parameters:
- lst : list of all the chips won or lost played in all game

Returns: 
 - average of chips won or lost
Description:
'''
def Average(lst):
    return sum(lst) / len(lst)
'''
Function Name: Summary_Chips

Parameters:
only need the game_file

Returns: 
 - how much the player have won or have lost 
'''
def max_bet(line):
    index = 0
    i = 0
    words = line.split()
    for letter in words[15]:
        if (letter == '/'):
            index = i
        i+=1
    return int(words[15][index+1:-1])
def Summary_Chips(game_file,main_player):
    (lines,street_index) = file_index(game_file)
    idSummary = street_index[-1]
    i = idSummary
    
    while i < len(lines):
        words = lines[i].split()
        if words[2] == main_player and words[3] == "showed":
            if words[12] == "won" :
                return round((int(words[13][1:-1]) - Count_Chips(main_player,lines, idSummary))/max_bet(lines[0]),2)
            else:
                return round(-Count_Chips(main_player,lines, idSummary)/max_bet(lines[0]),2)
        i+=1
    return round(Count_Chips(main_player,lines, idSummary)/max_bet(lines[0]),2)
'''
Function Name: Card_Street


'''
def Card_street(word,street_index, lines, player):
    i = 0
    if word == '3rd':
        i = street_index[0]
    elif word == '4th':
        i = street_index[1]
    elif word == '5th':
        i = street_index[2]
    elif word == '6th':
        i = street_index[3]
    elif word == 'River':
        i = street_index[4]
    words = lines[i].split()
    while (words[0] != 'Dealt' or words[2] != player):
        i+=1
        words = lines[i].split()
    hand = []
    for card in words[3:]:
        c = ''
        for letter in card:
            if letter != "[" and  letter != "]":
                c += letter
        hand.append(c)
    return hand
'''
Function Name: Card_to_html

'''
def Card_to_html(hand):
    Html_Cards = []
    num_cards = ['A','2','3','4','5','6','7','8','9','T','J','C','Q','K']
    shape_card = ['s','h','d','c']
    for card in hand:
        i= num_cards.index(card[0])
        j= shape_card.index(card[1])
        Html_Cards.append(["#1271" + str(i+16*j + 37)+";",j])
    return Html_Cards
'''
Function Name: Summary_Hands

'''
def Summary_Hands(game_file,main_player):
    (lines,street_index) = file_index(game_file)
    i = street_index[-1]
    while i < len(lines):
        words = lines[i].split()
        if words[2] == main_player and (words[3] == "showed" or words[3] == "mucked") :
            hand = []
            for card in words[4:11]:
                c = ''
                for letter in card:
                    if letter != "[" and  letter != "]":
                        c += letter
                hand.append(c)
            return Card_to_html(hand)
        elif words[2] == main_player and words[3] == "folded" :
            return Card_to_html(Card_street(words[6],street_index, lines, main_player))
        i+=1

def Init(game_file):
    (lines,street_index) = file_index(game_file)
    Pot = 0
    i  = 2
    Players_Init = []
    ante  = 0
    while i < street_index[0]:
        words = lines[i].split()
        if words[1] =='posts':
           ante = int(words[4])
           Pot += ante
        i+=1
    i=0
    while i < street_index[0]:
        words = lines[i].split()
        if words[0] =='Seat':
            Players_Init.append([words[2],int(words[3][1:])-ante])
        i+=1
    return [Players_Init,Pot]
def Action(lines,line,street,street_index):
    words = line.split()
    action = [words[0][:-1],words[1]]
    if words[0] == 'Dealt':
            street_words = lines[street].split()
            return [words[2],'Dealt',Card_to_html(Card_street(street_words[1],street_index, lines, words[2]))]
    elif words[1] == 'raises':
        i = lines.index(line)
        action.append(raises(i,lines,words[0][:-1]))
        return action
    elif words[1] == 'brings':
        action.append(int(words[4]))
        return action
    elif words[1] == 'calls' or words[1] == 'bets':
        action.append(int(words[2]))
        return action
    elif words[1] == 'folds' or words[1] == 'checks':
        return action
    

def Play(game_file):
    Players_Actions = []
    Street_Change = []
    (lines,street_index) = file_index(game_file)
    i = street_index[0]
    street = i 
    while i < street_index[-1]:
        if i in street_index:
            street = i
        words = lines[i].split()
        if words[0] == '***':
            Street_Change.append(i)
            Players_Actions.append([lines[i]])
        else:
            
            Players_Actions.append(Action(lines,lines[i],street,street_index))
        i+=1
    Players_Actions.append([lines[i]])
    
    return Players_Actions