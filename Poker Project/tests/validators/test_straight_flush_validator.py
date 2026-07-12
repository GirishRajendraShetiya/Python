import unittest

from poker.card import Card
from poker.validators import StraightFlushValidator

class StraightFlushValidatorTest(unittest.TestCase):
    def test_determines_that_there_are_not_five_consecutive_cards_with_same_suit(self):
        cards = [
            Card(rank = "3", suit = "Hearts"),
            Card(rank = "4", suit = "Hearts"),
            Card(rank = "5", suit = "Hearts"),
            Card(rank = "6", suit = "Hearts"),
            Card(rank = "7", suit = "Spades"),
            Card(rank = "King", suit = "Hearts"),
            Card(rank = "Ace", suit = "Diamonds")
        
        # It's a straight (rank from 3 to 7) and flush (5 cards with the same suit as "Hearts"), both are True,
        # but, it's not a straight flush.
        ]

        validator = StraightFlushValidator(cards = cards)

        self.assertEqual(
            validator.is_valid(),
            False
        )

    def test_determines_that_there_are_five_consecutive_cards_with_same_suit(self):
        cards = [
            Card(rank = "3", suit = "Hearts"),
            Card(rank = "4", suit = "Hearts"),
            Card(rank = "5", suit = "Hearts"),
            Card(rank = "6", suit = "Hearts"),
            Card(rank = "7", suit = "Hearts"),
            Card(rank = "King", suit = "Hearts"),
            Card(rank = "Ace", suit = "Diamonds")
        
        # It's a straight (rank from 3 to 7) and flush (5 cards with the same suit as "Hearts"), both are True,
        # but, it's not a straight flush.
        ]

        validator = StraightFlushValidator(cards = cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_determines_that_there_are_only_five_consecutive_cards_with_same_suit(self):
        three = Card(rank = "3", suit = "Hearts")
        four = Card(rank = "4", suit = "Hearts")
        five = Card(rank = "5", suit = "Hearts")
        six = Card(rank = "6", suit = "Hearts")
        seven = Card(rank = "7", suit = "Hearts")

        cards = [
            three,
            four,
            five,
            six,
            seven,
            Card(rank = "King", suit = "Hearts"),
            Card(rank = "Ace", suit = "Diamonds")
        
        # It's a straight (rank from 3 to 7) and flush (5 cards with the same suit as "Hearts"), both are True,
        # but, it's not a straight flush.
        ]

        validator = StraightFlushValidator(cards = cards)

        self.assertEqual(
            validator.valid_cards(),
            [
                three,
                four,
                five,
                six,
                seven
            ]
        )