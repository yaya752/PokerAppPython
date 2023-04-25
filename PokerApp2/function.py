import json
def Generalities(line):
    gene = []
    words = line.split()
    gene.append(words[2])
    gene.append(words[4])
    gene.append(words[17:19])
    return gene


def raises(index,lines,mane_player):
    Sum = 0
    i = index
    words = lines[i].split()
    while lines[i][:3] !="***" and i > 0:
        words = lines[i].split()
        if words[1] == "raises" and words[0] == mane_player + ":": 
            Sum +=int(words[4])
        elif words[0] == mane_player + ":":
            if words[1] == "brings":
                Sum-= int(words[4])
            elif words[1] == "calls":
                Sum-= int(words[2])
            elif words[1] == "bets":
                Sum-= int(words[2])
        i-=1
    return Sum
def Count_Chips(mane_player,lines, idSummary):
    Sum = 0
    i = 0
    words = lines[i].split()
    while i < idSummary:        
        words = lines[i].split()
        if words[0] == "Seat" and words[2] == mane_player : 
            Chips = int(words[3][1:])
        elif words[1] == "posts" and words[0] == mane_player + ":":
            Sum += int(words[4])
        elif words[0] == mane_player + ":":
            if words[1] == "brings":
                Sum+= int(words[4])
            elif words[1] == "calls":
                Sum+= int(words[2])
            elif words[1] == "bets":
                Sum+= int(words[2])
            elif words[1] == "raises":
                Sum+= raises(i,lines,mane_player)
            elif words[1] == "folds" or words[1] == "mucks":
                Sum =-Sum
                i = idSummary
        i+=1
    return Sum
def Average(lst):
    return sum(lst) / len(lst)
def Summary_Chips(game_file,mane_player):
    file_name ='Game_File\\' + game_file
    lines = []
    i = 0
    with open(file_name, "r") as f:
        for line in f:
            lines.append(line.strip())
        list_index = []
        
        for line in lines:
            if line[:5] == '*** 3':

                list_index.append(i)
            elif line[:5] == '*** 4':

                list_index.append(i)
            elif line[:5] == '*** 5':

                list_index.append(i)
            elif line[:5] == '*** 6':

                list_index.append(i)
            elif line[:5] == '*** R':

                list_index.append(i)
            elif line[:6] == '*** SH':

                list_index.append(i)
            elif line[:6] == '*** SU':
                idSummary = i
            i+=1     
    i = idSummary
    while i < len(lines):
        words = lines[i].split()
        if words[2] == mane_player and words[3] == "showed":
            if words[12] == "won" :
                return int(words[13][1:-1]) - Count_Chips(mane_player,lines, idSummary)
            else:
                return -Count_Chips(mane_player,lines, idSummary)
        i+=1
    return Count_Chips(mane_player,lines, idSummary)
def Card_street(word,street_index, lines, mane_player):
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
    print(i)
    words = lines[i].split()
    while (words[0] != 'Dealt' or words[2] != mane_player):
        i+=1
        print(lines[i])
        words = lines[i].split()
    print("--------------")  
    return words[3:]

def Summary_Hands(game_file,mane_player):
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
            i+=1     
    i = idSummary
    while i < len(lines):
        words = lines[i].split()
        if words[2] == mane_player and (words[3] == "showed" or words[3] == "mucked") :
            return words[4:9]
        elif words[2] == mane_player and words[3] == "folded" :
            return Card_street(words[6],street_index, lines, mane_player)
        i+=1