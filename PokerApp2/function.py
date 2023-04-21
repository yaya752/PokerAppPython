from Card import Card
from table import Table
from Player import Player
import json

def Summary_json(game_file,mane_player):
    file_name = "Game_File\\" + game_file
    lines = []
    i = 0
    with open(file_name, "r") as f:
        for line in f:
            lines.append(line.strip())
        list_index = []
        
        for line in lines:
            if line[:5] == '*** 3':
                print(line)
                list_index.append(i)
            elif line[:5] == '*** 4':
                print(line)
                list_index.append(i)
            elif line[:5] == '*** 5':
                print(line)
                list_index.append(i)
            elif line[:5] == '*** 6':
                print(line)
                list_index.append(i)
            elif line[:5] == '*** 7':
                print(line)
                list_index.append(i)
            elif line[:5] == '*** S':
                print(line)
                idSummary = i
            i+=1
    print(list_index)