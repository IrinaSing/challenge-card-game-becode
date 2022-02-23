# main file

    def fill_cards(self):
        suits = "♠ ♡ ♢ ♣".split()
        ranks = "2 3 4 5 6 7 8 9 10 J Q K A".split()
        
        for i in range (0, len(ranks)):
            for j in range (0, len(suits)):
                card = (ranks[i] + suits[j])
                self.cards.append(card)
            return self.cards


    def distribute(players: List[Player]):
        player1 = []
        player2 = []
        player3 = []
        player4 = []

        # Distribute cards to payers
        for c in range (len(Deck)):
            if len(Deck) == 0:
                break
            else:        
                player1.append(Deck[0])
                Deck.pop(0)

                player2.append(Deck[0])
                Deck.pop(0)
                
                player3.append(Deck[0])
                Deck.pop(0)
                
                player4.append(Deck[0])
                Deck.pop(0)
