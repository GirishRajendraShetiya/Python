import unittest
from unittest.mock import MagicMock

from poker.card import Card
from poker.player import Player
from poker.hand import Hand

class PlayerTest(unittest.TestCase):
    def test_stores_names_and_cards(self):
        # hand = Hand(cards = [])
        # 28th Jun, 2026
        hand = Hand()
        # 28th Jun, 2026
        
        player = Player(name = "Boris", hand = hand)
        self.assertEqual(player.name, "Boris")
        self.assertEqual(player.hand, hand)

    def test_figures_out_own_best_hand(self):
        mock_hand = MagicMock()  # It's a fake hand
        mock_hand.best_rank.return_value = "Straight Flush"
        player = Player(name = "Boris", hand = mock_hand)
        
        self.assertEqual(
            player.best_hand(),
            "Straight Flush"
        )
        
        player.best_hand()
        mock_hand.best_rank.assert_called()

    def test_passes_new_cards_to_hand(self):
        mock_hand = MagicMock()
        player = Player(name = "Appu", hand = mock_hand)
        
        cards = [
            Card(rank = "Ace", suit = "Spades"),
            Card(rank = "7", suit = "Hearts")
        ]
        
        player.add_cards(cards)
        
        mock_hand.add_cards.assert_called_once_with(cards)
        