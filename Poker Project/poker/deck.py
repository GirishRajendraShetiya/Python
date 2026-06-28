import random

class Deck():
    def __init__(self):
        self.cards = []
    
    def add_cards(self, card):
        self.cards.extend(card)
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def remove_cards(self, card_to_be_removed):
        cards_to_remove = self.cards[:card_to_be_removed]
        del self.cards[:card_to_be_removed]
        return cards_to_remove
