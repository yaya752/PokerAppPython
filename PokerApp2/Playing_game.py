from Calcul import Calculate_odds
from Odds import Table, Append_cards
from Decisions import third_street_decision,add,index_poss,sumarry_tab, quiz_4th, quiz_5th

########################################################################################
#   Function Name: Generalities                                                        #
#                                                                                      #
#   Parameters:                                                                        #
#       - line : first line of one of a file game of a tournament                      #
#                   (this file has to be put in the " Game_File" folder)               #
#                                                                                      #
#   Returns:                                                                           #
#       - game_generalities : list of generalities about the game                      #
#                                                                                      #
#   Description:                                                                       #
#       - Allow to get the date, the tournament id and the hand id                     #
#                                                                                      #
########################################################################################

def Generalities(line):
    #Intialisation of the variable
    game_generalities = []

    #split a line into a list of words
    words = line.split()
    
    # Retrieved the list of words the good data (date, id etc...)
    game_generalities.append(words[2])
    game_generalities.append(words[4])
    game_generalities.append(words[17:19])

    return game_generalities

########################################################################################
#   Function Name: file_index                                                          #
#                                                                                      #
#   Parameters:                                                                        #
#       - game_file : the name of the game file .txt                                   #
#                                                                                      #
#   Returns:                                                                           #
#       - lines : list of lines of the game file                                       #
#       - street_index : list of index, each index is link to a street                 #
#                                                                                      #
#   Description:                                                                       #
#       - This function is used in other function to browse into the file easly        #
#                                                                                      #
########################################################################################
def file_index(game_file,path):
    #Intialisation of the variable
    file_name =path + game_file #change ./Game_File/ into ./Game_File/ if you are on linux
    lines = []
    i = 0

    #open the file 
    with open(file_name, "r") as f:
        # put/add each line into a list
        for line in f:
            lines.append(line.strip())
        street_index = []
        # read each lines and retrieved the index of the lines where the street changes
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
                street_index.append(i)
            # i = index of the current line in the lines ' s list 
            i+=1
    #return the list of lines and the list of index of the beginning of a new street
    
    return (lines,street_index,)

########################################################################################
#   Function Name: raises                                                              #
#                                                                                      #
#   Parameters:                                                                        #
#       - Sum :  get the amount of chips put by on the table when a player is raising  #
#                                                                                      #
#   Returns:                                                                           #
#       - index : index of the raise action                                            #
#       - lines : lines of the game file                                               #
#       - player : player who raised                                                   #
#   Description:                                                                       #
#       - When a player raised the way we calculate the amount of chips                #
#       put on the table is determined by what the players have done before            #
########################################################################################
def raises(index,lines,player):
    #Intialisation of the variable
    Sum = 0
    i = index
    #split a line into words
    words = lines[i].split()
    if words[1] == "raises" and words[0] == player + ':':
        # when raises the player will add chips to update is bet to a certain amount
        Sum +=int(words[4]) # amount wanted 
        # We look each line until we meet a street line or we get to the beginning of the list of lines
        while lines[i][:3] !="***" and i > 0:
            words = lines[i].split()
            #if the player have called brung or bet during the street the amount of chips that he have to put on the table is less than if has done nothing
            if words[0] == player + ":":
                if words[1] == "brings":
                    Sum-= int(words[4])
                elif words[1] == "calls":
                    Sum-= int(words[2])
                elif words[1] == "bets":
                    Sum-= int(words[2])
            i-=1
    return Sum

########################################################################################
#   Function Name: Count_Chips                                                         #
#                                                                                      #
#   Parameters:                                                                        #
#       - player : used to identify quickly the player whose chips we want to count    #
#       - lines  : list of the lines of the game file                                  #
#       - idSummary :  used to stop earlier the programme                              #
#                                                                                      #
#   Returns:                                                                           #
#       - Sum : How much a player put chips                                            #
#                                                                                      #
#   Description:                                                                       #
#       - Calculate how much a player put chips during the game                        #
#                                                                                      #
########################################################################################
def Count_Chips(player,lines, idSummary):
    #Intialisation of the variable
    Sum = 0
    i = 0
    words = lines[i].split()
    #we look just at the playing phase (like the 3rd 4th ... to the show down)
    while i < idSummary:        
        words = lines[i].split()
        # we count every chips that the player put on the table
        if words[1] == 'posts' and words[0] == player + ":":
            Sum += int(words[4])
        elif words[0] == player + ":":
            if words[1] == 'brings':
                Sum+= int(words[4])
            elif words[1] == 'calls':
                Sum+= int(words[2])
            elif words[1] == 'bets':
                Sum+= int(words[2])
            elif words[1] == 'raises':
                Sum+= raises(i,lines,player)
            elif words[1] == "folds" or words[1] == "mucks":
                Sum =-Sum
                i = idSummary
        i+=1
    return Sum

########################################################################################
#   Function Name : Average                                                            #
#                                                                                      #
#   Parameters:                                                                        #
#       - lst : list of all the chips won or lost played in all game                   #
#                                                                                      #
#   Returns:                                                                           #
#       - average of chips won or lost                                                 #
#                                                                                      #
#   Description:                                                                       #
#       - calculates on average how many poker chips the player has won or lost        #
#                                                                                      #
########################################################################################
def Average(lst):
    if len(lst) == 0 :
        return 0
    else:
        return sum(lst) / len(lst)


########################################################################################
#   Function Name : Max_Bet                                                            #
#                                                                                      #
#   Parameters:                                                                        #
#       - line : the first line of a game file                                         #
#                                                                                      #
#   Returns:                                                                           #
#       - the maximum bet that a player can bet                                        #
#                                                                                      #
#   Description:                                                                       #
#       - This function is used to have a concrete idea of the amount of chips the     #
#           player put on the table (if he was aggressive or not for exemple)          #
#                                                                                      #
########################################################################################
def Max_Bet(line):
    #Intialisation of the variable
    index = 0
    i = 0
    words = line.split()
    #we look each letter to find the / caracter to supress it and acess to the max bet
    for letter in words[15]:
        if (letter == '/'):
            index = i
        i+=1
    # int("1") will return the int 1 so in our case it willl be retrun a bet in a the type : Number (it's easier to manipulate number than caracter)
    return int(words[15][index+1:-1])

########################################################################################
#   Function Name : Summary_Chips                                                      #
#                                                                                      #
#   Parameters:                                                                        #
#       - game_file : the file of the game                                             #
#       - main_player : the "HERO" of the game                                         #
#                                                                                      #
#   Returns:                                                                           #
#       - the number of chips bet divided by the max_bet possible                      #
#                                                                                      #
#   Description:                                                                       #
#       - This function is used to have a concrete idea of the amount of chips the     #
#           player put on the table (if he lost or won lot or not)                     #
#                                                                                      #
########################################################################################
def Summary_Chips(game_file,main_player,path):
    (lines,street_index) = file_index(game_file,path)
    if len(street_index) >=2:
        # For this function we need the list of line of the file and the index of the street so we used the file_index function
        (lines,street_index) = file_index(game_file,path)
        idSummary = street_index[-1]
        # We juste need to look at the summary part because we can find the necessary to calculate how many chips did the player played during the game
        i = idSummary
    
        while i < len(lines):
            words = lines[i].split()
            # if the player played all the game the amount is accessible directly in the summary part 
            if words[2] == main_player and words[3] == "showed":
                if words[12] == "won" :
                    return round((int(words[13][1:-1]) - Count_Chips(main_player,lines, idSummary))/Max_Bet(lines[0]),2)
                else:
                    return round(-Count_Chips(main_player,lines, idSummary)/Max_Bet(lines[0]),2)
            i+=1
        # else we can go through all the file and count line by line how chips the player played
        return round(Count_Chips(main_player,lines, idSummary)/Max_Bet(lines[0]),2)
    else:
        return -1
 
########################################################################################
#   Function Name : Card_Street                                                        #
#                                                                                      #
#   Parameters:                                                                        #
#       - word : The word define the street where we work                              #
#       - lines : list of the lines of the game file                                   #
#       - street_index : list of the index of the different streets                    #
#                              in the list of the game files                           #
#       - player : name of the player we are interested in                             #
#       - occur : table of card that have been dealt during the game                   #
#                   (divide between each street of the game)                           #
#       - main_player : name of the "HERO", it's used in the Append_cards function     #
#                                                                                      #
#   Returns:                                                                           #
#       - hand : list of cards                                                         #
#                                                                                      #
#   Description:                                                                       #
#       - This function allow to extract cards                                         #
#               from the file to create the hand of the players during the game        #
#                                                                                      #
########################################################################################
def Card_Street(word,street_index, lines, player, occur,main_player,Players):
    #Intialisation of the variable
    i = 0
    # each street all the past cards and the new cards are given so we can just look at the street that we need and retrieved the hand
    if word == '3rd':
        i = street_index[0]
    elif word == '4th':
        i = street_index[1]
    elif word == '5th':
        i = street_index[2]
    elif word == '6th':
        i = street_index[3]
    elif word == 'RIVER' or word == 'River':   
        i = street_index[4]
        if player !=main_player:
            k = 0
            while k < len(Players) and Players[k][0] != player:
                k+=1
            Players[k][1].append('x')
            
            return Players[k][1]
    elif word == 'SHOW':   
        i = street_index[-2]
    words = lines[i].split()
    # When we have the index of the street we go through lines and find the lines where the cards of the player are given 
    while ((words[0] != 'Dealt' or words[1] != 'shows' ) and words[2] != player  ):
        i+=1
        words = lines[i].split()
    hand = []
    # when we have the good line we extract the cards from the text 
    if  words[1] == 'shows': 
        
        for card in words[2:9]:
            c = ''
            for letter in card:
                if letter != "[" and  letter != "]":
                    c += letter
            hand.append(c)

    else :
        if player != main_player:
            if word != 'RIVER' or word != 'River':
                hand.append('x')
                hand.append('x')
            else:
                hand.append('x')
        for card in words[3:]:
            
            c = ''
            for letter in card:
                if letter != "[" and  letter != "]":
                    c += letter
            hand.append(c)
    Append_cards(hand,occur,main_player,player)
    return hand
########################################################################################
#   Function Name : Card_To_Html                                                       #
#                                                                                      #
#   Parameters:                                                                        #
#       - hand : list of cards                                                         #
#                                                                                      #
#   Returns:                                                                           #
#       - Html_cards : list of html code for each cards in the hand                    #
#                                                                                      #
#   Description:                                                                       #
#       - convert the card (like As or 2h) to their equivalent in html code            #
#           to display them properly                                                   #
#                                                                                      #
########################################################################################
def Card_To_Html(hand):
    #Intialisation of the variable
    Html_Cards = []
    num_cards = ['A','2','3','4','5','6','7','8','9','T','J','C','Q','K']
    shape_card = ['s','h','d','c']
    for card in hand:
        if card == 'x':
            Html_Cards.append(["#127136;",4])
        else:
            i= num_cards.index(card[0])
            j= shape_card.index(card[1])
            #in html we can display graphical card by using a unicode
            Html_Cards.append(["#1271" + str(i+16*j + 37)+";",j])
    return Html_Cards
########################################################################################
#   Function Name : Summary_Hands                                                      #
#                                                                                      #
#   Parameters:                                                                        #
#       - game_file : name of the file of the game                                     #
#       - main_player : name of the "HERO"                                             #
#                                                                                      #
#   Returns:                                                                           #
#       - Html cards of the hand of the main player at the end of the game             #
#                                                                                      #
#   Description:                                                                       #
#       - extrat the last hand of the player                                           #
#                                                                                      #
########################################################################################
def Summary_Hands(game_file,main_player,path):
    # For this function we need the list of line of the file and the index of the street so we used the file_index function
    (lines,street_index) = file_index(game_file,path)
    # We juste need to look at the summary part because we can find the necessary to calculate how many chips did the player played during the game
    i = street_index[-1] # street_index[-1] is the index of the summary
    occur =Table() 
    while i < len(lines):
        words = lines[i].split()
        # if he showed or mucked is card we have access to his finnal hand directly
        if words[2] == main_player and (words[3] == "showed" or words[3] == "mucked") :
            hand = []
            for card in words[4:11]:
                c = ''
                for letter in card:
                    if letter != "[" and  letter != "]":
                        c += letter
                hand.append(c)
            return Card_To_Html(hand)
        # else we can find in which street he folded and retrieved his hand by using Card Street function 
        # ( Card-To_ html function is only used for displaying the card on the html page)
        elif words[2] == main_player and words[3] == "folded" :
            return Card_To_Html(Card_Street(words[6],street_index, lines, main_player,occur,main_player,[]))
        i+=1
########################################################################################
#   Function Name : Init                                                               #
#                                                                                      #
#   Parameters:                                                                        #
#       - game_file : name of the file of the game                                     #
#                                                                                      #
#   Returns:                                                                           #
#       - players : number of the player at the beggining                              #
#       - Pot : amount of chips in the middle of the table at the beginning            #
#            with the ante                                                             #
#       - Players_Init : list of players with their name                               #
#           and the amount of chips they have at the beginning                         #
#                                                                                      #
#   Description:                                                                       #
#       - Initialise the game                                                          #
#                                                                                      #
########################################################################################
def Init(game_file,path):
    # For this function we need the list of line of the file and the index of the street so we used the file_index function
    (lines,street_index) = file_index(game_file,path)
    #Intialisation of the variable
    Pot = 0
    players = 0
    Players = []
    i  = 2
    Players_Init = []
    ante  = 0
    # We need to calculate the beginning pot because each player have to put an ante even if they fold directly
    while i < street_index[0]:
        words = lines[i].split()
        if words[1] =='posts':
           ante = int(words[4])
           Pot += ante
        i+=1
    i=0
    # at the beginning of the file the player are given when we know their seat
    while i < street_index[0]:
        words = lines[i].split()
        if words[0] =='Seat':
            # words[3][1:] amount of chips own by the player at the beginning 
            # words[2] name of the player
            Players.append([words[2],"play"])
            Players_Init.append([words[2],int(words[3][1:])-ante])
            players +=1
        i+=1
    return ([Sort_Player(Players_Init),Pot],[players],Players)
def Sort_Player(player_list):
    index_hero = -1
    for i in range (len(player_list)):
        if player_list[i][0] == 'Hero':
            index_hero = i
    new_list = []
    j = index_hero
    new_list.append(player_list[j])
    if j+1 == len(player_list):
        j=0
    else:
        j+=1
    while j != index_hero:
        new_list.append(player_list[j])
        if j+1 == len(player_list):
            j=0
        else:
            j+=1
    length = len(player_list)
    
    if length == 2:
        new_list = [new_list[1],new_list[0]]
    elif length == 3:
        new_list = [new_list[1],new_list[2],new_list[0]]
    elif length == 4:
        new_list = [new_list[1],new_list[2],new_list[3],new_list[0]]
    elif length == 5:
        new_list = [new_list[1],new_list[2],new_list[3],new_list[4],new_list[0]]
    elif length == 6:
        new_list = [new_list[2],new_list[3],new_list[4],new_list[5],new_list[0],new_list[1]]
    elif length == 7:
        new_list = [new_list[3],new_list[4],new_list[5],new_list[6],new_list[0],new_list[1],new_list[2]]
    elif length == 8:
        new_list = [new_list[4],new_list[5],new_list[6],new_list[7],new_list[0],new_list[1],new_list[2],new_list[3]]
    return new_list
########################################################################################
#   Function Name : Action                                                             #
#                                                                                      #
#   Parameters:                                                                        #
#       - lines : list of the lines of the game file                                   #
#       - line : line of the file of the action to identify                            #
#       - street : index of the street where the action have been done                 #
#       - street_index : list of the index of the different streets                    #
#                              in the list of the game files                           #
#       - occur : table of card that have been dealt during the game                   #
#                   (divide between each street of the game)                           #
#       - main_player : name of the "HERO"                                             #
#       -tab_player : used in the decision system                                      #
#   Returns:                                                                           #
#       - list of the action                                                           #
#                                                                                      #
#   Description:                                                                       #
#       - allow to identify who did the action and what he did                         #
#                                                                                      #
########################################################################################
def Action(lines,line,street,street_index, occur, main_player,Player):
    words = line.split()
    
    # words[0][:-1] name of the player
    # words[1] is generally an action 
    action = [words[0][:-1],words[1]]
    # We read the line of the action and if it feats a specific patern we can access to all the information we nead 
    # to update the list of players we create the lists when the cards are dealt and we increment a counter to know in what order the players played
    
    if words[0] == 'Dealt':
        street_words = lines[street].split()
        k = 0
        while k < len(Player) and Player[k][0] != words[2]:
            k+=1
        Player[k][1] = Card_Street(street_words[1],street_index, lines, words[2],occur,main_player,Player)
        return [words[2],'Dealt',Card_To_Html(Card_Street(street_words[1],street_index, lines, words[2],occur,main_player,Player))]
    elif words[1] == 'raises':
        i = lines.index(line)
        
        action.append(raises(i,lines,words[0][:-1]))
        
        return action
    elif words[1] == 'brings':
        action.append(int(words[4]))
        
        
        return action
    elif words[1] == 'calls' :
        action.append(int(words[2]))
        
       
        return action
    elif words[1] == 'bets':
        action.append(int(words[2]))
        
       
        return action
    elif words[1] == 'folds' :
        
        return action
    elif words[1] == 'checks':
        
        
        return action
    elif words[1] == 'shows':
        street_words = lines[street].split()
        return [words[0][:-1],words[1],Card_To_Html(Card_Street(street_words[1],street_index, lines, words[2],occur,main_player,Player))]
    elif words[1] == 'mucks':
        return action
    elif words[0] == 'Uncalled':
        return [words[5],words[0],int(words[2][1:-1])]
    elif words[1] == 'collected':
        return [words[0],words[1],int(words[2])]
    elif words[0] == 'Seat':
        if words[3] == 'showed' and words[12] == 'won':
            return [words[2],'Won']
        elif words[3] == 'collected':
            return [words[2],words[3],int(words[4][1:-1])]
    elif words[0] == 'Seat':
        if words[3] == 'showed' and words[12] == 'won':
            return [words[2],'Won']
        elif words[3] == 'collected':
            return [words[2],words[3:]]

########################################################################################
#   Function Name : Action                                                             #
#                                                                                      #
#   Parameters:                                                                        #
#       - game_file : name of the file of the game                                     #
#       - main_player : name of the "HERO"                                             #
#       - list_numplayers : list of numbers of player currently playing for each street#
#                                                                                      #
#   Returns:                                                                           #
#       - Players_Actions : list of action made by players during the game             #
#       - tab_street : table of table of state of the game (odds + cards dealt)        #
#       - decision : decision tab                                                      #
#                                                                                      #
#   Description:                                                                       #
#       - recreate the game and add odds and quiz                                      #
#                                                                                      #
########################################################################################
def Play(game_file,main_player,list_numplayers,path):
    #Intialisation of the variable
    (initialisation,list_numplayers,Players) = Init(game_file,path)
    Players_Actions = []
    occur = Table()
    tab_street = []

    tab_player = [] #List of info about player, [[name,list_cards,position during the street, if he has been aggressive, what hand he can play],....]
    tab_prec_player = [] #Same as before but for the previous street  
    (lines,street_index) = file_index(game_file,path)
    max_bet = Max_Bet(lines[0])
    i = street_index[0]
    street = i
    time = 0 # where we are in the game
    j = 0
    order = [] 
    order.append(0)
    decision = []
    players = list_numplayers[-1]
    while i < len(lines):
        if i in street_index:
            street = i  
        words = lines[i].split()
        # if we met a new street we calculate the new occurence tab and odds associate to it 
        if words[0] == '***':

            
            
            if words[1] != "3rd": 
                list_numplayers.append(players)
                (occur1,low_hand_odds,high_hand_odds)= Calculate_odds(occur,words[1],list_numplayers) #calculate the odds using the occur tab (occurence of the cards)
                tab_street.append([occur1,low_hand_odds,high_hand_odds])
            Players_Actions.append([lines[i]])
            if words[1] == "RIVER":
                for k in range(0,len(Players)):
                    if Players[k][1] != "folds":
                        
                        Players_Actions.append([Players[k][0],"Dealt",Card_To_Html(Card_Street('RIVER',street_index, lines, Players[k][0],occur,main_player,Players))])
                
            
            j+=1
       #else we add the action to the list with a specific pattern [name of the player,action, chips or cards]
        else:
            act = (Action(lines,lines[i],street,street_index,occur,main_player,Players))
            if act :
                words = lines[i].split()
                if words[1] == 'folds':
                    k = 0
                    while k <len(Players) and Players[k][0] !=words[0][:-1]:
                        k+=1
                    
                    Players[k][1] ="folds"
                    
                    players-=1
                Players_Actions.append(act)
        i+=1
    return (Players_Actions,tab_street,decision,max_bet)