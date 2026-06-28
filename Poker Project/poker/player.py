class Player:
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand
        
    def best_hand(self):
        # Hand(self.cards).best_rank()  # Without the use of dependency injection
        
        return self.hand.best_rank()  # Dependency injection

