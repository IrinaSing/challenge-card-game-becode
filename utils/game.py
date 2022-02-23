# game

from typing import List
from utils.card import Card
from utils.card import Deck, Player


class Board:
    def __init__(self, players: List[Player], turn_count: int, active_cards: List[Card], history_cards):
        self.players = players
        self.turn_count = 0
        self.active_cards = []
        self.history_cards = []

        def start_game(self):
            Deck.fill_cards()
            Deck.shuffle()
            Deck.distribute()