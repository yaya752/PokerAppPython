from Card import *
class Player:
    def __init__(self,Name, AllCards, CardSeen, Chips , Action):
        self.Name = Name
        self.AllCards = AllCards
        self.CardSeen = CardSeen
        self.Chips = Chips
        self.Action = Action
    def __json__(self):
        AllCards_list = []

        for Cards in self.AllCards:
           card = Cards.__json__()
           AllCards_list.append(card)
        CardSeen_list = []
        for Cards in self.CardSeen:
           card = Cards.__json__()
           CardSeen_list.append(card)
        return {
            'Name': self.Name,
            'AllCards': AllCards_list,
            'CardSeen': CardSeen_list,
            'Chips' : self.Chips,
            'Action': self.Action
        }

            
    def display(self):
        print("Name of the player :",self.Name)
        for card in self.AllCards: 
            card.display()#print cards by using the fonction display() of the class Card
        for card in self.CardSeen:
            card.display()
        print("Chips of the player :", self.Chips)
        print(self.Name, self.Action)

