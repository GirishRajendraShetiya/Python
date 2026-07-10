import unittest

from poker.card import Card
from poker.validators import FullHouseValidator

class FullHouseValidatorTest(unittest.TestCase):
    def setUp(self):
        self.three_of_hearts = Card(rank = "3", suit = "Hearts")
        self.three_of_clubs = Card(rank = "3", suit = "Clubs")
        self.three_of_spades = Card(rank = "3", suit = "Spades")
        self.two_of_diamonds = Card(rank = "2", suit = "Diamonds")
        self.two_of_spades = Card(rank = "2", suit = "Spades")

        self.cards = [
            self.three_of_hearts,
            self.three_of_clubs,
            self.three_of_spades,
            Card(rank = "5", suit = "Diamonds"),
            self.two_of_diamonds,
            Card(rank = "9", suit = "Clubs"),
            self.two_of_spades  
        ]

    def test_validates_if_it_is_a_full_house(self):        
        validator = FullHouseValidator(cards = self.cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_validates_collection_having_two_and_three_cards_of_same_rank_respectively(self):
        validator = FullHouseValidator(cards = self.cards)

        self.assertEqual(
            validator.valid_cards(),
            [
                self.three_of_hearts,
                self.three_of_clubs,
                self.three_of_spades,
                self.two_of_diamonds,
                self.two_of_spades
            ]
        )
