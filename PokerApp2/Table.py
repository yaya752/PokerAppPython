import Player
class Table:
    def __init__(self, Players, Pot, Rake):
        self.Players = Players 
        self.Pot = Pot
        self.Rake = Rake


    def afficher(self):
        for player in Player:
            Player.display
        print("Pot :", self.Pot)
        print("Rake :", self.Rake)