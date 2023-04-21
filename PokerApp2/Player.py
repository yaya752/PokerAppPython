from Card import *
class Player:
    def __init__(self,Name, AllCards, CardSeen, Chips , Action, Position, ChipsOnTable):
        self.Name = Name
        self.AllCards = AllCards
        self.CardSeen = CardSeen
        self.Chips = Chips
        self.Action = Action
        self.Position = Position
        self.ChipsOnTable = ChipsOnTable
    def __json__(self):
        AllCards_list = []

        for Cards in self.AllCards:
           card = Cards.__json__()
           AllCards_list.append(card)
        CardSeen_list = []
        for Cards in self.CardSeen:
           card = Cards.__json__()
           CardSeen_list.append(card)
        Action_str = ' '.join (self.Action)
        
        return {
            'Name': self.Name,
            'AllCards': AllCards_list,
            'CardSeen': CardSeen_list,
            'Chips' : self.Chips,
            'Action': Action_str,
            'Position': self.Position,
            'ChipsOnTable': self.ChipsOnTable
        }

            
    def display(self):
        print("Name of the player :",self.Name)
        for card in self.AllCards: 
            card.display()#print cards by using the fonction display() of the class Card
        for card in self.CardSeen:
            card.display()
        print("Chips of the player :", self.Chips)
        print(self.Name, self.Action)
        print(self.Position)
        print(self.ChipsOnTable)

    def ActionsToChips(self):
        ligne = self.Action
        if ligne[0] == "brings" :
            self.ChipsOnTable += int(ligne[3])
            self.Chips = self.Chips - self.ChipsOnTable
        elif ligne[0] == "calls":
            self.ChipsOnTable =self.ChipsOnTable + int(ligne[1])
            self.Chips = self.Chips - self.ChipsOnTable
        elif ligne[0] == "folds" :
            self.ChipsOnTable += 0
            self.Chips -= self.ChipsOnTable
        elif ligne[0] == "raises" :
            self.ChipsOnTable += int(ligne[3])
            self.Chips -= self.ChipsOnTable
        elif ligne[0] == "bets":
            self.ChipsOnTable += int(ligne[1])
            self.Chips -= self.ChipsOnTable
