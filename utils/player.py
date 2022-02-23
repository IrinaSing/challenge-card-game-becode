# How to check arguments: few ways
# https://stackoverflow.com/questions/19684434/best-way-to-check-function-arguments

import random
from typing import List
from card import Card
class Player:

    players = []
    
    def __init__(self, name: str, cards: List[Card], turn_count: int, number_of_cards: int, history: List[Card]):
        
        self.name = name
        self.cards = cards
        self.turn_count = 0
        self.number_of_cards = 0
        self.history = []

        Player.players.append(self)        
    

    def play(self):
        random_card = random.choice(self.cards)
        self.history.append(random_card)
        self.cards.remove(random_card)
        self.turn_count += 1
        print(f"{self.name} (turn {self.turn_count}) played: {random_card}. History: {self.history}. Cards left: {self.cards}")
        return random_card
    

# create instances of players

player1 = Player("Cecil", [], 0, 0, [])
player2 = Player("Maria", [], 0, 0, [])
# print("players", Player.players)
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

        # Distribute cards to players
        
        while len(self.cards) > 0:
            for player in self.players:    
                player.cards.append(self.cards[0])
                self.cards.pop(0)
                # print(len(self.cards))
                # print(player.cards)
                continue     

    

deck_1 = Deck([],["♥", "♦", "♣", "♠"], ['A', "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"], Player.players)
# deck_1.fill_deck()
# deck_1.shuffle()
# deck_1.distribute()

# print(player1.play())
# print(player2.play())






        
  
