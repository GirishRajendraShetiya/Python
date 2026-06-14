import unittest
from poker.card import Card

# python -m unittest discover tests: Command to run all the mentioned test files within the /tests folder at once.

# python -m unittest .\tests\test_cards.py: Command to run a specific test file within the /tests folder.

class CardTest(unittest.TestCase):
    def test_has_rank(self):
        card = Card(rank = "Queen", suit = "Hearts")
        self.assertEqual(card.rank, "Queen")

    def test_has_suit(self):
        card = Card(rank = "Queen", suit = "Hearts")
        self.assertEqual(card.suit, "Hearts")
    
    # 14th Jun, 2026
    def test_knows_its_rank_index(self):
        card = Card(rank = "Jack", suit = "Hearts")
        self.assertEqual(card.rank_index, 9)
    # 14th Jun, 2026
    
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
                "Jack", "Queen", "King", "Ace"
            )
        )
    
    def test_card_only_allows_valid_rank(self):
        with self.assertRaises(ValueError):
            Card(rank = "Two", suit = "Hearts")
        
    def test_card_only_allows_valid_suit(self):
        with self.assertRaises(ValueError):
            Card(rank = "2", suit = "Hello")    
            
    def test_can_create_standard_52_cards(self):
        cards = Card.create_standard_deck_of_52_cards()
        self.assertEqual(len(cards), 52)
        
        self.assertEqual(
            cards[0],
            Card(rank = "2", suit = "Hearts")
        )

        self.assertEqual(
            cards[-1],
            Card(rank = "Ace", suit = "Diamonds")
        )
        
    def test_figure_out_if_two_card_objects_are_equal(self):
        self.assertEqual(
            Card(rank = "2", suit = "Hearts"),
            Card(rank = "2", suit = "Hearts")
        )

    # 13th Jun, 2026
    def test_card_can_sort_itself_with_another_one(self):
        queen_of_spades = Card(rank = "Queen", suit = "Spades")
        king_of_spades = Card(rank = "King", suit = "Spades")
        evaluation = queen_of_spades < king_of_spades
        
        self.assertEqual(
            evaluation,
            True,
            "The sort algorithm is not sorting the lower card first"
        )

    def test_sort_cards(self):
        two_of_spades = Card(rank = "2", suit = "Spades"),
        five_of_diamonds = Card(rank = "5", suit = "Diamonds"),
        five_of_hearts = Card(rank = "5", suit = "Hearts"),
        eight_of_hearts = Card(rank = "8", suit = "Hearts"),
        ace_of_clubs = Card(rank = "Ace", suit = "Clubs"),
    
        unsorted_cards = [
            five_of_diamonds,
            eight_of_hearts,
            ace_of_clubs,
            five_of_hearts,
            two_of_spades
        ]
        
        unsorted_cards.sort()
        
        self.assertEqual(
            unsorted_cards,
            [
                two_of_spades,
                five_of_diamonds,  # Sorting of suit is being done ALPHABETICALLY
                five_of_hearts,
                eight_of_hearts,
                ace_of_clubs
            ]
        )
# 13th Jun, 2026
