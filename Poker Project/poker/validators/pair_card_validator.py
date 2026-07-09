from poker.validators import RankValidator

class PairCardValidator(RankValidator):
    def __init__(self, cards):
        self.cards = cards
        self.name = "Pair"
    
    def is_valid(self):
        ranks_with_pairs = self._ranks_with_count(2)
        return len(ranks_with_pairs) == 1
    
    def valid_cards(self):
        ranks_with_pairs = self._ranks_with_count(2)  # {'King': 2, 'Ace': 2}
        cards = [card for card in self.cards if card.rank in ranks_with_pairs.keys()]
        return cards

    # def _ranks_with_count(self, count):
    #     return {
    #         rank: rank_count
    #         for rank, rank_count in self._card_rank_counts.items()  # The dictionary will be from the protected _card_rank_counts method
    #         if rank_count == count
    #     }

    # @property
    # def _card_rank_counts(self):
    #     card_rank_counts = {}  # To get the relation between the rank and the count of ranks, a dictionary can be used.
        
    #     for card in self.cards:
    #         card_rank_counts.setdefault(card.rank, 0)  # At first, the rank won't be in the card_rank_counts dictionary, so to add it to the dictionary, setdefault method is used.
    #         card_rank_counts[card.rank] += 1  # {"Ace": 2}
    #     return card_rank_counts                
