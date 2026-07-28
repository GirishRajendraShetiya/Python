import unittest

from poker.card import Card
from poker.validators import RoyalFlushValidator

class RoyalFlushValidatorTest(unittest.TestCase):
    def test_validates_that_cards_do_not_have_a_straight_flush_ending_with_an_ace(self):
        cards = [
            Card(rank = "9", suit = "Hearts"),
            Card(rank = "10", suit = "Hearts"),
            Card(rank = "Jack", suit = "Hearts"),
            Card(rank = "Queen", suit = "Hearts"),
            Card(rank = "King", suit = "Hearts"),
            Card(rank = "Ace", suit = "Diamonds")
        ]
        
        validator = RoyalFlushValidator(cards = cards)

        self.assertEqual(
            validator.is_valid(),
            False
        )

    def test_validates_that_cards_have_a_straight_flush_ending_with_an_ace(self):
        cards = [
            Card(rank = "2", suit = "Spades"),
            Card(rank = "10", suit = "Hearts"),
            Card(rank = "Jack", suit = "Hearts"),
            Card(rank = "Queen", suit = "Hearts"),
            Card(rank = "King", suit = "Hearts"),
            Card(rank = "Ace", suit = "Hearts"),
            Card(rank = "Ace", suit = "Diamonds")
        ]
        
        validator = RoyalFlushValidator(cards = cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_returns_five_cards_with_same_rank_ending_in_ace(self):
        two = Card(rank = "2", suit = "Spades")
        ten = Card(rank = "10", suit = "Hearts")
        jack = Card(rank = "Jack", suit = "Hearts")
        queen = Card(rank = "Queen", suit = "Hearts")
        king = Card(rank = "King", suit = "Hearts")
        ace_of_hearts = Card(rank = "Ace", suit = "Hearts")
        ace_of_diamonds = Card(rank = "Ace", suit = "Diamonds")

        cards = [
            two,
            ten,
            jack,
            queen,
            king,
            ace_of_hearts,
            ace_of_diamonds
        ]
        
        validator = RoyalFlushValidator(cards = cards)

        self.assertEqual(
            validator.valid_cards(),
            [
                ten,
                jack,
                queen,
                king,
                ace_of_hearts
            ]
        )
