import unittest
from poker.card import Card

class CardTest(unittest.TestCase):
    def test_has_rank(self):
        card = Card(rank = "Queen", suit = "Hearts")
        self.assertEqual(card.rank, "Queen")

    def test_has_suit(self):
        card = Card(rank = "Queen", suit = "Hearts")
        self.assertEqual(card.suit, "Hearts")
        
    def test_has_string_representation_with_rank_and_suit(self):
        card = Card("5", "Diamonds")
        self.assertEqual(str(card), "5 of Diamonds")
    
    def test_has_representation(self):
        card = Card("5", "Diamonds")
        self.assertEqual(repr(card), "Card('5', 'Diamonds')")
    
    def test_card_has_four_suit_options(self):
        self.assertEqual(
            Card.SUITS,
            ("Hearts", "Clubs", "Spades", "Diamonds")
        )
    
    def test_card_has_thirteen_rank_options(self):
        self.assertEqual(
            Card.RANKS,
            (
                "2", "3", "4", "5", "6", "7", "8", "9", "10",
                "Jack", "Queen", "King", "Ace")
        )
    
    def test_card_only_allows_valid_rank(self):
        with self.assertRaises(ValueError):
            Card(rank = "Two", suit = "Hearts")
        
    def test_card_only_allows_valid_suit(self):
        with self.assertRaises(ValueError):
            Card(rank = "2", suit = "Hello")    

# python -m unittest discover tests: Command to run all the mentioned test files within the /tests folder at once.

# python -m unittest .\tests\test_cards.py: Command to run a specific test file within the /tests folder.
