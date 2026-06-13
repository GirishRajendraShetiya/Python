class Hand():
    def __init__(self, cards):
        self.cards = cards
    
    @property
    def _ranks_validation_from_best_to_worst(self):
        return (
            ("Three of a Kind", self._three_of_a_kind),
            ("Two Pair", self._two_pair),
            ("Pair", self._pair),
            ("High Card", self._high_card)
        )
    
    def best_rank(self):        
        for rank in self._ranks_validation_from_best_to_worst:
            name, validator_func = rank
            if validator_func():
                return name
        
        # {"King": 3, "5": 1, "Ace": 1}
        # ranks_with_three_of_a_kind = self._ranks_with_count(3)
        # {"King": 3}
        
        # if len(ranks_with_three_of_a_kind) == 1:
        #     return "Three of a Kind"        

        # {"King": 2, "5": 1, "Ace": 2}
        # ranks_with_pairs = self._ranks_with_count(2)
        # {"Ace": 2, "King": 2}
        
        # if len(ranks_with_pairs) == 2:
        #     return "Two Pair"
        
        # if len(ranks_with_pairs) == 1:
        #     return "Pair"
                
        # return "High Card"
    
    def _three_of_a_kind(self):
        ranks_with_three_of_a_kind = self._ranks_with_count(3)
        return len(ranks_with_three_of_a_kind) == 1
            # return True

    def _two_pair(self):
        ranks_with_pairs = self._ranks_with_count(2)
        return len(ranks_with_pairs) == 2
            # return True
    
    def _pair(self):
        ranks_with_pairs = self._ranks_with_count(2)
        return len(ranks_with_pairs) == 1
    
    def _high_card(self):
        return True
    
    def _ranks_with_count(self, count):
        return {
            rank: rank_count
            for rank, rank_count in self._card_rank_counts.items()  # The dictionary will be from the protected _card_rank_counts method
            if rank_count == count
        }
    
    @property
    def _card_rank_counts(self):
        card_rank_counts = {}  # To get the relation between the rank and the count of ranks, a dictionary can be used.
        
        for card in self.cards:
            card_rank_counts.setdefault(card.rank, 0)  # At first, the rank won't be in the card_rank_counts dictionary, so to add it to the dictionary, setdefault method is used.
            card_rank_counts[card.rank] += 1  # {"Ace": 2}
        return card_rank_counts