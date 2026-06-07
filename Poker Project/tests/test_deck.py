import unittest
from poker.deck import Deck
from poker.card import Card

class DeckTest(unittest.TestCase):
    def test_has_no_cards_at_start(self):
        deck = Deck()
        self.assertEqual(
            deck.cards,
            []
        )
    
    def test_add_cards(self):
        card = Card(rank = "2", suit = "Clubs")
        deck = Deck()
        deck.add_cards([card])  # As we're adding it to a list
        
        self.assertEqual(
            deck.cards,
            [card]
        )
