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

Cardesses = Symbol("red", "♥")
        

class Cards(Symbol):  # <--- Inherits from Symbol
    """
    A class that defines a card.

    It inherits from the class symbol.
    """
    def __init__(self, color: str, icon: str, value: str):
        pass