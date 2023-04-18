from Card import *
class Player:
    def __init__(self,Name, AllCards, CardSeen, Chips):
        self.Name = Name
        self.AllCards = AllCards
        self.CardSeen = CardSeen
        self.Chips = Chips

            
    def display(self):
        print("Name of the player :",self.Name)
        for card in self.AllCards: 
            card.display()#print cards by using the fonction display() of the class Card
        for card in self.CardSeen:
            card.display()
        print("Chips of the player :", self.Chips)
