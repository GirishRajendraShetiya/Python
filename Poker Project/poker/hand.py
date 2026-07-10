# 07th Jul, 2026
from poker.validators import (
    FullHouseValidator,
    FlushValidator,
    StraightValidator,
    ThreeOfAKindValidator,
    NoCardsValidator, 
    HighCardValidator, 
    PairCardValidator,
    TwoPairValidator
)
# 07th Jul, 2026

# 13th Jun, 2026
class Hand():
    def __init__(self):
        self.cards = []
    
    def __repr__(self):
        cards_as_strings = [str(card) for card in self.cards]
        return ", ".join(cards_as_strings)
    
    def add_cards(self, cards):
        copy = self.cards[:]
        copy.extend(cards)
        copy.sort()
        self.cards = copy
    
    @property
    def _ranks_validation_from_best_to_worst(self):
        return (
            ("Royal Flush", self._royal_flush),  # 14th Jun, 2026
            ("Straight Flush", self._straight_flush),  # 14th Jun, 2026
            ("Four of a Kind", self._four_of_a_kind),  # 14th Jun, 2026
            
            # 10th Jul, 2026
            # ("Full House", self._full_house),  # 14th Jun, 2026
            ("Full House", FullHouseValidator(cards = self.cards).is_valid),

            # ("Flush", self._flush),  # 14th Jun, 2026
            ("Flush", FlushValidator(cards = self.cards).is_valid),

            # ("Straight", self._straight),  # 14th Jun, 2026
            ("Straight", StraightValidator(cards = self.cards).is_valid),
            # 10th Jul, 2026

            # 09th Jul, 2026
            # ("Three of a Kind", self._three_of_a_kind),
            ("Three of a Kind", ThreeOfAKindValidator(cards = self.cards).is_valid),
            # 09th Jul, 2026

            # 08th Jul, 2026
            # ("Two Pair", self._two_pair),
            ("Two Pair", TwoPairValidator(cards = self.cards).is_valid),
            # ("Pair", self._pair),
            ("Pair", PairCardValidator(cards = self.cards).is_valid),
            # 08th Jul, 2026

            # 07th Jul, 2026
            # ("High Card", self._high_card),
            ("High Card", HighCardValidator(cards = self.cards).is_valid),
            ("No Card", NoCardsValidator(cards = self.cards).is_valid),

            # 27th Jun, 2026
            # ("No Cards", self._no_cards)
            # 27th Jun, 2026
            # 07th Jul, 2026
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
        
        # 27th Jun, 2026
        if not is_straight_flush:
            return False
        # 27th Jun, 2026
        
        is_royal = self.cards[-1].rank == "Ace"
        return is_straight_flush and is_royal    
    
    def _straight_flush(self):
        return FlushValidator(cards = self.cards).is_valid() and StraightValidator(cards = self.cards).is_valid()
    
    def _four_of_a_kind(self):
        ranks_with_four_of_a_kind = self._ranks_with_count(4)
        return len(ranks_with_four_of_a_kind) == 1
    
    # 10th Jul, 2026
    # def _full_house(self):
    #     return ThreeOfAKindValidator(cards = self.cards).is_valid() and PairCardValidator(cards = self.cards).is_valid()
    
    # def _flush(self):
    #     suit_that_occurs_5_or_more_times = {
    #         suit: suit_count
    #         for suit, suit_count in self._card_suit_counts.items()
    #         if suit_count >= 5
    #     }
        
    #     return len(suit_that_occurs_5_or_more_times) == 1
    
    # def _straight(self):
    #     if len(self.cards) < 5:
    #         return False
        
    #     rank_indexes = [card.rank_index for card in self.cards]
    #     starting_rank_index = rank_indexes[0]
    #     last_rank_index = rank_indexes[-1]
    #     straight_consecutive_indexes = list(
    #         range(starting_rank_index, last_rank_index + 1)
    #     )
    #     return rank_indexes == straight_consecutive_indexes
    # 10th Jul, 2026

    # 14th Jun, 2026
    
    # 09th Jul, 2026
    # def _three_of_a_kind(self):
    #     ranks_with_three_of_a_kind = self._ranks_with_count(3)
    #     return len(ranks_with_three_of_a_kind) == 1
            # return True
    # 09th Jul, 2026

    # 08th Jul, 2026
    # def _two_pair(self):
    #     ranks_with_pairs = self._ranks_with_count(2)
    #     return len(ranks_with_pairs) == 2
    
    # def _pair(self):
    #     ranks_with_pairs = self._ranks_with_count(2)
    #     return len(ranks_with_pairs) == 1
    # 08th Jul, 2026

    # 07th Jul, 2026    
    # def _high_card(self):
    #     return len(self.cards) >= 2
    
    # def _no_cards(self):
    #     return len(self.cards) == 0
    # 07th Jul, 2026

    def _ranks_with_count(self, count):
        return {
            rank: rank_count
            for rank, rank_count in self._card_rank_counts.items()  # The dictionary will be from the protected _card_rank_counts method
            if rank_count == count
        }
    
    # 10th Jul, 2026
    # 14th Jun, 2026
    # @property
    # def _card_suit_counts(self):
    #     card_suit_counts = {}  # To get the relation between the rank and the count of ranks, a dictionary can be used.
        
    #     for card in self.cards:
    #         card_suit_counts.setdefault(card.suit, 0)  # At first, the rank won't be in the card_rank_counts dictionary, so to add it to the dictionary, setdefault method is used.
    #         card_suit_counts[card.suit] += 1  # {"Hearts": 5}
    #     return card_suit_counts
    # 14th Jun, 2026
    # 10th Jul, 2026
    
    @property
    def _card_rank_counts(self):
        card_rank_counts = {}  # To get the relation between the rank and the count of ranks, a dictionary can be used.
        
        for card in self.cards:
            card_rank_counts.setdefault(card.rank, 0)  # At first, the rank won't be in the card_rank_counts dictionary, so to add it to the dictionary, setdefault method is used.
            card_rank_counts[card.rank] += 1  # {"Ace": 2}
        return card_rank_counts
# 13th Jun, 2026
