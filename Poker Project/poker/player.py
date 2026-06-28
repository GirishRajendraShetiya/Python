class Player:
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand
        
    def best_hand(self):
        # Hand(self.cards).best_rank()  # Without the use of dependency injection
        
        return self.hand.best_rank()  # Dependency injection

    def add_cards(self, cards):
        self.hand.add_cards(cards)
        
    def wants_to_fold(self):
        return False