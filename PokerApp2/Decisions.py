

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
    for j in range(0,len(occur[0]-3)):
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
            action = [0]
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
        