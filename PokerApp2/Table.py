from Player import *
class Table:
    def __init__(self, Players, Pot, Rake):
        self.Players = Players 
        self.Pot = Pot
        self.Rake = Rake

    def __json__(self):
        Players_list = [] 
        for player in self.Players:
            player_json = player.__json__()
            Players_list.append(player_json)
        return{
            'Players':Players_list,
            'Pot':self.Pot,
            'Rake': self.Rake
            }

    def display(self):
        for player in self.Players:
            player.display()
        print("Pot :", self.Pot)
        print("Rake :", self.Rake)

    def AppendPlayer(self,player):
        self.Players.append(player)

    def DealtAllCards(self,name,card):
        for player in self.Players:
            if player.Name == name:
                player.AllCards.append(card)

    def DealtSeenCards(self,name,card):
        for player in self.Players:
            if player.Name == name:
                player.AllCards.append(card)
                player.CardSeen.append(card)
    def Ante(self,ante):
        for player in self.Players:
            player.Chips -= ante
    def Do(self,Name,Action):
        for player in self.Players:
            if player.Name == Name:
                player.Action = Action