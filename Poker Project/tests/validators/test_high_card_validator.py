import unittest

from poker.card import Card
from poker.validators import HighCardValidator

class HighCardValidatorTest(unittest.TestCase):
    def test_validates_that_cards_have_high_card(self):
        cards = [
            Card(rank = "Ace", suit = "Spades"),
            Card(rank = "7", suit = "Diamonds")
        ]

        validator = HighCardValidator(cards = cards)


        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_returns_high_card_from_card_collection(self):
        ace_of_diamonds = Card(rank = "Ace", suit = "Diamonds")

        cards = [
            Card(rank = "5", suit = "Diamonds"),
            Card(rank = "8", suit = "Hearts"),
            Card(rank = "2", suit = "Clubs"),
            Card(rank = "10", suit = "Spades"),
            ace_of_diamonds
        ]

        validator = HighCardValidator(cards = cards)

        self.assertEqual(
            validator.valid_cards(),
            [ace_of_diamonds]
        )
