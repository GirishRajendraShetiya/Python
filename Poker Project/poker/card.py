class Card():
    SUITS = ("Hearts", "Clubs", "Spades", "Diamonds")
    RANKS = ("2", "3", "4", "5", "6", "7", "8", "9", "10",
             "Jack", "Queen", "King", "Ace")
    
    def __init__(self, rank, suit):
        if rank not in self.RANKS:
            raise ValueError(f"The provided rank is not in {self.RANKS}")

        if suit not in self.SUITS:
            raise ValueError(f"The provided suit is not in {self.SUITS}")
        
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"
    
    def __repr__(self):
        return f"Card('{self.rank}', '{self.suit}')"

# At this point, even if Card(rank = "111", suit = "111") is given, it'll give the output as Card('111', '111'),
# which shouldn't be the case.
