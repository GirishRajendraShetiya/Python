class Card():
    SUITS = ("Hearts", "Clubs", "Spades", "Diamonds")
    RANKS = ("2", "3", "4", "5", "6", "7", "8", "9", "10",
             "Jack", "Queen", "King", "Ace")
    
    @classmethod
    def create_standard_deck_of_52_cards(cls):
        return [
            cls(rank = rank, suit = suit)
            for suit in cls.SUITS
            for rank in cls.RANKS
        ]
        
    def __init__(self, rank, suit):
        if rank not in self.RANKS:
            raise ValueError(f"The provided rank is not in {self.RANKS}")

        if suit not in self.SUITS:
            raise ValueError(f"The provided suit is not in {self.SUITS}")
        
        self.rank = rank
        
        # 14th Jun, 2026
        self.rank_index = self.RANKS.index(rank)
        # 14th Jun, 2026
        
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"
    
    def __repr__(self):
        return f"Card('{self.rank}', '{self.suit}')"

# At this point, even if Card(rank = "111", suit = "111") is given, it'll give the output as Card('111', '111'),
# which shouldn't be the case.

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

# 13th Jun, 2026
    def __lt__(self, other):

        # 08th Jul, 2026
        if self.rank == other.rank:
            return self.suit < other.suit
        # 08th Jul, 2026

        return self.rank_index < other.rank_index  # 14th Jun, 2026
        
        current_card_rank_index = self.RANKS.index(self.rank)  # As the RANKS tuple is already sorted, comparing with the index is beneficial.
        other_card_rank_index = self.RANKS.index(other.rank)
        return current_card_rank_index < other_card_rank_index
# 13th Jun, 2026
