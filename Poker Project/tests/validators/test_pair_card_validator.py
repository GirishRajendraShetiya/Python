import unittest

from poker.card import Card
from poker.validators import PairCardValidator

class PairCardValidatorTest(unittest.TestCase):
    def test_validates_that_cards_have_exact_a_pair(self):
        cards = [
            Card(rank = "Ace", suit = "Spades"),
            Card(rank = "Ace", suit = "Diamonds")
        ]
        
        validator = PairCardValidator(cards = cards)
        
        self.assertEqual(
            validator.is_valid(),
            True
        )
    
    def test_returns_pair_from_card_collection(self):
        ten_of_spades = Card(rank = "10", suit = "Spades")
        ten_of_diamonds = Card(rank = "10", suit = "Diamonds")

        cards = [
            Card(rank = "5", suit = "Hearts"),
            Card(rank = "7", suit = "Clubs"),
            ten_of_diamonds,
            ten_of_spades,
            Card(rank = "9", suit = "Spades")
        ]

        validator = PairCardValidator(cards = cards)

        self.assertEqual(
            validator.valid_cards(),
            [ten_of_diamonds, ten_of_spades]
        )
