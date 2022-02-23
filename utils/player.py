# How to check arguments: few ways
# https://stackoverflow.com/questions/19684434/best-way-to-check-function-arguments

import random
from typing import List
from card import Card
class Player:
    players = []
    
    def __init__(self, cards: List[Card], turn_count: int, number_of_cards: int, history: List[Card]):
        
        self.cards = cards
        self.turn_count = 0
        self.number_of_cards = 0
        self.history = []

        Player.players.append(self)
        

    """    

    def play(self):
        Card = random.choice(self.cards)
        print("Card:", Card)
        self.history.append(Card)
        print("{PLAYER_NAME} {TURN_COUNT} played: {CARD_NUMBER} {CARD_SYMBOL_ICON}.")
        return Card
"""

# create instances of players

player1 = Player([], 0, 0, [])
player2 = Player([], 0, 0, [])
print("players", Player.players)
class Deck:
    def __init__(self, cards: List, icons: List[str], values: List[str], players: List):
        self.icons = icons
        self.values = values
        self.cards = []
        self.players = players

    def fill_deck(self):
        for i in range (0, len(self.values)):
            for j in range (0, len(self.icons)):
                card = (self.values[i] + self.icons[j])
                self.cards.append(card)
        return self.cards

    def shuffle(self):
        random.shuffle(self.cards)
        return self.cards

    
    def distribute(self):
        print("players in distr", self.players)

        # Distribute cards to players
        
        while len(self.cards) > 0:
            for player in self.players:    
                player.cards.append(self.cards[0])
                self.cards.pop(0)
                print(len(self.cards))
                print(player.cards)
                continue     

    

deck_1 = Deck([],["♥", "♦", "♣", "♠"], ['A', "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"], Player.players)
deck_1.fill_deck()
deck_1.shuffle()
print(deck_1.distribute())




        
  
