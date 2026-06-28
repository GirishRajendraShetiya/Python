import unittest
from unittest.mock import MagicMock

from poker.player import Player
from poker.hand import Hand

class PlayerTest(unittest.TestCase):
    def test_stores_names_and_cards(self):
        hand = Hand(cards = [])
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
