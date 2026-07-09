import unittest

from poker.card import Card
from poker.validators import TwoPairValidator

class TwoPairValidatorTest(unittest.TestCase):
    def setUp(self):
        self.five_of_clubs = Card(rank = "5", suit = "Clubs")
        self.king_of_clubs = Card(rank = "King", suit = "Clubs")
        self.king_of_spades = Card(rank = "King", suit = "Spades")
        self.ace_of_diamonds = Card(rank = "Ace", suit = "Diamonds")
        self.ace_of_hearts = Card(rank = "Ace", suit = "Hearts")

        self.cards = [
            self.five_of_clubs,
            self.king_of_clubs,
            self.king_of_spades,
            self.ace_of_diamonds,
            self.ace_of_hearts
        ]

    def test_validates_that_cards_have_atleast_two_pair_of_same_rank(self):
        validator = TwoPairValidator(cards = self.cards)
        
        self.assertEqual(
            validator.is_valid(),
            True
        )
    
    def test_returns_collection_of_cards_that_have_pairs(self):
        validator = TwoPairValidator(cards = self.cards)

        self.assertEqual(
            validator.valid_cards(),
            [
                self.king_of_clubs,
                self.king_of_spades,
                self.ace_of_diamonds,
                self.ace_of_hearts
            ]
        )
