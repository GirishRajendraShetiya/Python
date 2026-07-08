class GameRound():
    def __init__(self, deck, players):
        self.deck = deck
        self.players = players
        
    def play(self):
        # Shuffle the deck
        self._shuffle_deck()
        self._deal_initial_two_cards_to_each_player()
        self._make_bets()

        # 29th Jun, 2026
        self._deal_flop_cards()
        self._make_bets()
        # 29th Jun, 2026
        
        # 01st Jul, 2026
        self._deal_turn_card()
        self._make_bets()
        
        self._deal_river_card()
        self._make_bets()
        # 01st Jul, 2026
        
    def _shuffle_deck(self):
        self.deck.shuffle()
        
    def _deal_initial_two_cards_to_each_player(self):
        for player in self.players:
            two_cards = self.deck.remove_cards(2)
            player.add_cards(two_cards)
            
    def _make_bets(self):
        for player in self.players:
            if player.wants_to_fold():
                # Remove the player
                self.players.remove(player)
    
    # 01st Jul, 2026
    def _deal_community_cards(self, number_of_cards):
        community_cards = self.deck.remove_cards(number_of_cards)
        for player in self.players:
            player.add_cards(community_cards)
    # 01st Jul, 2026
    
    # 29th Jun, 2026
    def _deal_flop_cards(self):
        self._deal_community_cards(3)
    # 29th Jun, 2026
    
    # 01st Jul, 2026
    # def _deal_turn_card(self):
    #     turn_card = self.deck.remove_cards(1)
    #     for player in self.players:
    #         player.add_cards(turn_card)
    
    # Simplest form as compared to the above one
    def _deal_turn_card(self):
        self._deal_community_cards(1)  
            
    # def _deal_river_card(self):
    #     river_card = self.deck.remove_cards(1)
    #     for player in self.players:
    #         player.add_cards(river_card)

    def _deal_river_card(self):
        self._deal_community_cards(1)

    # # 01st Jul, 2026