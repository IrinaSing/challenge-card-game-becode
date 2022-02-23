# game

from typing import List
from card import Card
from player import Deck, Player


class Board:
    def __init__(self, players: List[Player], turn_count: int, active_cards: List[Card], history_cards):
        self.players = players
        print(self.players)
        self.turn_count = 0
        print(self.turn_count)
        self.active_cards = []
        print(self.active_cards)
        self.history_cards = []
        print(self.history_cards)

    def start_game(self):
        Deck.fill_deck(self)
        Deck.shuffle(self)
        Deck.distribute(self)

board1 = Board(Player.players, 0, [], [])
board1.start_game()