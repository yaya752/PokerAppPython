class Card:
    def __init__(self, Value, Shape):
        self.Value = Value
        self.Shape = Shape


    def display(self):
        print("Value :", self.Value)
        print("Shape :", self.Shape)

    def __json__(self):
        return {
            'Value': self.Value,
            'Shape': self.Shape
        }
