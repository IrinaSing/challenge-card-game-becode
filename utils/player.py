# How to check arguments: few ways
# https://stackoverflow.com/questions/19684434/best-way-to-check-function-arguments

import random
from typing import List
from card import Card
class Player:
    def __init__(self, cards: List[Card], turn_count: int, number_of_cards: int, history: List[Card]):
        self.cards = cards
        self.turn_count = 0
        self.number_of_cards = 0
        self.history = []

    """    

    def play(self):
        Card = random.choice(self.cards)
        print("Card:", Card)
        self.history.append(Card)
        print("{PLAYER_NAME} {TURN_COUNT} played: {CARD_NUMBER} {CARD_SYMBOL_ICON}.")
        return Card
"""

class Deck:
    def __init__(self, cards: List, icons: List[str], values: List[str]):
        self.icons = icons
        self.values = values
        self.cards = []

    def fill_deck(self):
        for i in range (0, len(self.values)):
            for j in range (0, len(self.icons)):
                card = (self.values[i] + self.icons[j])
                self.cards.append(card)
        return self.cards

    def shuffle(self):
        random.shuffle(self.cards)
        return self.cards

    """
    def distribute(self, players: List[Player]):
        players = Player.instances
        for player in players:
            player_cards = []
    """

deck_1 = Deck([],["♥", "♦", "♣", "♠"], ['A', "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"])
print(deck_1.fill_deck())
print(deck_1.shuffle())

# create instances of players
player1 = Player([], 0, 0, [])
player2 = Player([], 0, 0, [])

        
  
