# card
import random
from typing import List

class Symbol:
    """Class representing symbol (suit)"""

    def __init__(self, icon: str):
        # check if entered suit is among existing suits
        self.icon = icon
        if icon == "♥" or "♦":            
            self.color = "red"
        elif icon == "♣" or "♠":
            self.color = "black"
        else:
            raise ValueError("Such suit does not exist")
        

class Card(Symbol):  # <--- Inherits from Symbol
    """
    A class that defines a card with combination of suit and value.

    It inherits from the class symbol.
    """
    # class variable
    values = ['A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K']
    values = [word for line in values for word in line.split()]

    def __init__(self, icon: str, value: str):
        super().__init__(icon)
        self.value = value      
        
        # check if entered suit is among existing suits

    def check_value(self, value):
        if (self.value in Card.values):
            self.value = value
        else:
            raise ValueError("Such value does not exist")

    def create_card(self):
        print(self.icon, self.value)



      
# check
# card_1 = Card("♣", "K")
# print(card_1.create_card())
