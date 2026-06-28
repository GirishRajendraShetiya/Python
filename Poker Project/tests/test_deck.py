import unittest
from unittest.mock import patch
from poker.deck import Deck
from poker.card import Card

class DeckTest(unittest.TestCase):
    def test_has_length_equal_to_count_of_cards(self):
        deck = Deck()
        self.assertEqual(
            len(deck),
            0
        )
    
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

    # 28th Jun, 2026    
    @patch('random.shuffle')
    def test_shuffle_method(self, mock_shuffle):
        deck = Deck()
        
        cards = [
            Card(rank = "Ace", suit = "Spades"),
            Card(rank = "8", suit = "Diamonds")
        ]
        
        deck.add_cards(cards)
        
        deck.shuffle()
        
        mock_shuffle.assert_called_once_with(cards)
    
    def test_removes_specified_number_of_cards_from_deck(self):
        ace   = Card(rank = "Ace", suit = "Spades")
        eight = Card(rank = "8", suit = "Diamonds")
        cards = [ace, eight]
        
        deck = Deck()
        deck.add_cards(cards)
        
        self.assertEqual(
            deck.remove_cards(1),
            [ace]
        )
        
        self.assertEqual(
            deck.cards,
            [eight]
        )
    
    # 28th Jun, 2026
