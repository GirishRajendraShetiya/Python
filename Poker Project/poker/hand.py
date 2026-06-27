# 13th Jun, 2026
class Hand():
    def __init__(self, cards):
        copy = cards[:]  # A copy of the cards is made to avoid any issues.
        copy.sort()
        self.cards = copy
    
    @property
    def _ranks_validation_from_best_to_worst(self):
        return (
            ("Royal Flush", self._royal_flush),  # 14th Jun, 2026
            ("Straight Flush", self._straight_flush),  # 14th Jun, 2026
            ("Four of a Kind", self._four_of_a_kind),  # 14th Jun, 2026
            ("Full House", self._full_house),  # 14th Jun, 2026
            ("Flush", self._flush),  # 14th Jun, 2026
            ("Straight", self._straight),  # 14th Jun, 2026
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
    
    # 14th Jun, 2026
    def _royal_flush(self):
        is_straight_flush = self._straight_flush()
        is_royal = self.cards[-1].rank == "Ace"
        return is_straight_flush and is_royal    
    
    def _straight_flush(self):
        return self._flush() and self._straight()
    
    def _four_of_a_kind(self):
        ranks_with_four_of_a_kind = self._ranks_with_count(4)
        return len(ranks_with_four_of_a_kind) == 1
    
    def _full_house(self):
        return self._three_of_a_kind() and self._pair()
    
    def _flush(self):
        suit_that_occurs_5_or_more_times = {
            suit: suit_count
            for suit, suit_count in self._card_suit_counts.items()
            if suit_count >= 5
        }
        
        return len(suit_that_occurs_5_or_more_times) == 1
    
    def _straight(self):
        if len(self.cards) < 5:
            return False
        
        rank_indexes = [card.rank_index for card in self.cards]
        starting_rank_index = rank_indexes[0]
        last_rank_index = rank_indexes[-1]
        straight_consecutive_indexes = list(
            range(starting_rank_index, last_rank_index + 1)
        )
        return rank_indexes == straight_consecutive_indexes
    # 14th Jun, 2026
    
    def _three_of_a_kind(self):
        ranks_with_three_of_a_kind = self._ranks_with_count(3)
        return len(ranks_with_three_of_a_kind) == 1
            # return True

    def _two_pair(self):
        ranks_with_pairs = self._ranks_with_count(2)
        return len(ranks_with_pairs) == 2
    
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
    
    # 14th Jun, 2026
    @property
    def _card_suit_counts(self):
        card_suit_counts = {}  # To get the relation between the rank and the count of ranks, a dictionary can be used.
        
        for card in self.cards:
            card_suit_counts.setdefault(card.suit, 0)  # At first, the rank won't be in the card_rank_counts dictionary, so to add it to the dictionary, setdefault method is used.
            card_suit_counts[card.suit] += 1  # {"Hearts": 5}
        return card_suit_counts
    # 14th Jun, 2026
    
    @property
    def _card_rank_counts(self):
        card_rank_counts = {}  # To get the relation between the rank and the count of ranks, a dictionary can be used.
        
        for card in self.cards:
            card_rank_counts.setdefault(card.rank, 0)  # At first, the rank won't be in the card_rank_counts dictionary, so to add it to the dictionary, setdefault method is used.
            card_rank_counts[card.rank] += 1  # {"Ace": 2}
        return card_rank_counts
# 13th Jun, 2026
