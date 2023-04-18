from Player import *
class Table:
    def __init__(self, Players, Pot, Rake):
        self.Players = Players 
        self.Pot = Pot
        self.Rake = Rake


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
