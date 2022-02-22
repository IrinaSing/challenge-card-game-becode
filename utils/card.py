# card

class Symbol:
    """Class representing symbol (suit)"""

    def __init__(self, color: str, icon: str):        
        suits = ["♥", "♦", "♣", "♠"]
        # check if entered suit is among existing suits
        if (icon in suits):
            self.icon = icon
        else:
            raise ValueError("Such suit does not exist")
        self.color = color

print(Symbol("red", "♥"))


        

class Cards(Symbol):  # <--- Inherits from Symbol
    """
    A class that defines a card.

    It inherits from the class symbol.
    """
    def __init__(self, color: str, icon: str, value: str):
        super().__init__(color, icon)       
        values = ['A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K']
        values = [word for line in values for word in line.split()]
        # check if entered suit is among existing suits
        if (value in values):
            self.value = value
        else:
            raise ValueError("Such value does not exist")

print(Cards("red", "♥", "K"))