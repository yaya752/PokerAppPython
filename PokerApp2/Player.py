import Card
class Table:
    def __init__(self, AllCards, CardSeen, Chips):
        self.AllCards = AllCards
        self.CardSeen = CardSeen
        self.Chips = Chips


    def display(self):
        for card in self.AllCards: 
            Card.display(card)#print cards by using the fonction display() of the class Card
        for card in self.CardSeen:
            Card.display(card)
        print("Chips of the player :", self.Chips)
