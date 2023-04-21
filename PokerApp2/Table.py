from Player import *
class Table:
    def __init__(self, Players, Pot, Rake, Name ,Ante):
        self.ManePlayer = Name
        self.Players = Players 
        self.Pot = Pot
        self.Rake = Rake
        self.Ante = Ante

    def __json__(self):
        Players_list = [] 
        for player in self.Players:
            player_json = player.__json__()
            Players_list.append(player_json)
        return{
            'ManePlayer' : self.ManePlayer,
            'Players':Players_list,
            'Pot':self.Pot,
            'Rake': self.Rake,
            'Ante': self.Ante
            }

    def display(self):
        for player in self.Players:
            player.display()
        print("Pot :", self.Pot)
        print("Rake :", self.Rake)
        

    def AppendPlayer(self,player):
        self.Players.append(player)
    def GetPlayer(self,name):
        for player in self.Players:
            if player.Name == name:
                return player
    def DealtAllCards(self,name,card):
        for player in self.Players:
            if player.Name == name:
                player.AllCards.append(card)

    def DealtSeenCards(self,name,card):
        for player in self.Players:
            if player.Name == name:
                player.AllCards.append(card)
                player.CardSeen.append(card)

    def SetAnte(self):
        for player in self.Players:
            player.Chips -= self.Ante

    def Do(self,Name,Action,pos):
        for player in self.Players:
            if player.Name == Name:
                player.Action = Action
                player.Position = pos
                player.ActionsToChips()
            
    def Actions(self):
        for player in self.Players:
            player.ActionsToChips()
                    
    def Sort(self):
        i = 0
        Players = self.Players
        self.Players = []
        while (i < len(Players)):
            j = 0
            while (i != Players[j].Position):
                j+=1
            self.Players.append(Players[j])
            i+=1   


