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
                if (player.Position == -1):
                    player.Action = Action
                    player.Position = pos
                '''else:
                    newPlayer = Player(player.Name,player.AllCards,player.CardSeen,player.Chips,Action,pos)
                    self.Players.append(newPlayer)'''
    def Sort(self):
        i = 0
        Players = self.Players
        PlayerSorted = []
        while (i < len(Players)):
            j = 0
            print(Players[i].Position)
            while (i != Players[j].Position):
                
                j+=1
            PlayerSorted.append(Players[j])
            i+=1   
        self.Players = PlayerSorted


