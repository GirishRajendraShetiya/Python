class Deck():
    def __init__(self):
        self.cards = []
    
    def add_cards(self, card):
        self.cards.extend(card)
