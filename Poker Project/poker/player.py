class Player:
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand
    
    def __gt__(self, other):
        current_player_best_validator_index = self.best_hand()[0]  # 0
        other_player_best_validator_index = other.best_hand()[0]  # 2
        return current_player_best_validator_index < other_player_best_validator_index
        # A player is greater than the other player if it's validator index is less than the other player (0 in this case is higher than 2)

    def best_hand(self):
        # Hand(self.cards).best_rank()  # Without the use of dependency injection
        
        return self.hand.best_rank()  # Dependency injection

    def add_cards(self, cards):
        self.hand.add_cards(cards)
        
    def wants_to_fold(self):
        return False