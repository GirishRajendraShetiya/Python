import unittest
from poker.hand import Hand
from poker.card import Card

# 13th Jun, 2026
class HandTest(unittest.TestCase):
    # 28th Jun, 2026
    def test_starts_out_with_no_cards(self):
        hand = Hand()
        self.assertEqual(hand.cards, [])
    
    def test_shows_all_its_cards_in_technical_representation(self):
        cards = [
            Card(rank = "King", suit = "Spades"),
            Card(rank = "Queen", suit = "Hearts")
        ]
        
        hand = Hand()
        hand.add_cards(cards)
        
        self.assertEqual(
            repr(hand),
            "Queen of Hearts, King of Spades"
        )
    
    # 28th Jun, 2026
    
    def test_receives_and_stores_cards(self):
        ace_of_spades = Card(rank = "Ace", suit = "Spades")
        six_of_clubs = Card(rank = "6", suit = "Clubs")
        
        cards = [
            ace_of_spades,
            six_of_clubs
        ]
        hand = Hand()
        
        # 28th Jun, 2026
        hand.add_cards(cards)
        # 28th Jun, 2026
        
        self.assertEqual(
            hand.cards,
            [
                six_of_clubs,
                ace_of_spades
            ]
        )
    
    # 27th Jun, 2026
    # def test_figures_out_best_rank_is_no_card(self):
    #     hand = Hand()
    #     self.assertEqual(
    #         hand.best_rank(),
    #         "No Cards"
    #     )
    # 27th Jun, 2026
    
    # def test_figures_out_high_card_is_best_rank(self):
    #     cards = [
    #         Card(rank = "7", suit = "Diamonds"),
    #         Card(rank = "Ace", suit = "Spades")
    #     ]
    #     hand = Hand()
    #     # 28th Jun, 2026
    #     hand.add_cards(cards)
    #     # 28th Jun, 2026
        
    #     self.assertEqual(
    #         hand.best_rank(),
    #         "High Card"
    #     )

    # 08th Jul, 2026
    # def test_figures_out_pair_is_best_rank(self):
    #     cards = [
    #         Card(rank = "Ace", suit = "Spades"),
    #         Card(rank = "Ace", suit = "Diamonds")
    #     ]
        
    #     hand = Hand()
    #     # 28th Jun, 2026
    #     hand.add_cards(cards)
    #     # 28th Jun, 2026
        
    #     self.assertEqual(
    #         hand.best_rank(),
    #         "Pair"
    #     )
    
    # def test_figures_out_two_pair_is_best_rank(self):
    #     cards = [
    #         Card(rank = "Ace", suit = "Diamonds"),
    #         Card(rank = "5", suit = "Clubs"),
    #         Card(rank = "Ace", suit = "Hearts"),
    #         Card(rank = "King", suit = "Spades"),
    #         Card(rank = "King", suit = "Clubs")
    #     ]
        
    #     hand = Hand()
    #     # 28th Jun, 2026
    #     hand.add_cards(cards)
    #     # 28th Jun, 2026
        
    #     self.assertEqual(
    #         hand.best_rank(),
    #         "Two Pair"
    #     )
    # 08th Jul, 2026

    # 09th Jul, 2026
    # def test_figures_out_three_of_a_kind_is_best_rank(self):
    #     cards = [
    #         Card(rank = "King", suit = "Diamonds"),
    #         Card(rank = "5", suit = "Clubs"),
    #         Card(rank = "Ace", suit = "Hearts"),
    #         Card(rank = "King", suit = "Spades"),
    #         Card(rank = "King", suit = "Clubs")
    #     ]
        
    #     hand = Hand()
    #     # 28th Jun, 2026
    #     hand.add_cards(cards)
    #     # 28th Jun, 2026
        
    #     self.assertEqual(
    #         hand.best_rank(),
    #         "Three of a Kind"
    #     )
    # 09th Jul, 2026

    # 10th Jul, 2026
    # def test_figures_out_straight_is_best_rank(self):
    #     cards = [
    #         Card(rank = "6", suit = "Hearts"),
    #         Card(rank = "7", suit = "Diamonds"),
    #         Card(rank = "8", suit = "Spades"),
    #         Card(rank = "9", suit = "Clubs"),
    #         Card(rank = "10", suit = "Clubs")
    #     ]
            
    #     hand = Hand()
    #     # 28th Jun, 2026
    #     hand.add_cards(cards)
    #     # 28th Jun, 2026
            
    #     self.assertEqual(
    #         hand.best_rank(),
    #         "Straight"
    #     )
        

# 13th Jun, 2026

# 14th Jun, 2026
    # def test_does_not_deem_two_consecutive_to_be_straight(self):
    #     cards = [
    #         Card(rank = "6", suit = "Spades"),
    #         Card(rank = "7", suit = "Clubs")
    #     ]
        
    #     hand = Hand()
    #     # 28th Jun, 2026
    #     hand.add_cards(cards)
    #     # 28th Jun, 2026
        
    #     self.assertEqual(
    #         hand.best_rank(),
    #         "High Card"
    #     )

    # def test_figures_out_best_rank_when_flush(self):
    #     cards = [
    #         Card(rank = rank, suit = "Hearts")
    #         for rank in ["2", "5", "8", "10", "Ace"]
    #     ]
        
    #     hand = Hand()
    #     # 28th Jun, 2026
    #     hand.add_cards(cards)
    #     # 28th Jun, 2026
        
    #     self.assertEqual(
    #         hand.best_rank(),
    #         "Flush"
    #     )
    
    # def test_figures_out_full_house_is_best_rank(self):
    #     cards = [
    #         Card(rank = "3", suit = "Hearts"),
    #         Card(rank = "3", suit = "Clubs"),
    #         Card(rank = "3", suit = "Spades"),
    #         Card(rank = "2", suit = "Diamonds"),
    #         Card(rank = "2", suit = "Spades")
    #     ]
        
    #     hand = Hand()
    #     # 28th Jun, 2026
    #     hand.add_cards(cards)
    #     # 28th Jun, 2026
        
    #     self.assertEqual(
    #         hand.best_rank(),
    #         "Full House"
    #     )
    # 10th Jul, 2026

    # 11th Jul, 2026
    # def test_figures_out_four_of_a_kind_is_best_rank(self):
    #     cards = [
    #         Card(rank = "3", suit = "Hearts"),
    #         Card(rank = "3", suit = "Clubs"),
    #         Card(rank = "3", suit = "Spades"),
    #         Card(rank = "3", suit = "Diamonds"),
    #         Card(rank = "2", suit = "Spades")
    #     ]
        
    #     hand = Hand()
    #     # 28th Jun, 2026
    #     hand.add_cards(cards)
    #     # 28th Jun, 2026
        
    #     self.assertEqual(
    #         hand.best_rank(),
    #         "Four of a Kind"
    #     )
    # 11th Jul, 2026

    def test_figures_out_straight_flush_is_best_rank(self):
        cards = [
            Card(rank = "3", suit = "Hearts"),
            Card(rank = "4", suit = "Hearts"),
            Card(rank = "5", suit = "Hearts"),
            Card(rank = "6", suit = "Hearts"),
            # Card(rank = "7", suit = "Spades"),  # It's a false positive as there are 5 consecutive ranks, but not of same suits, a false positive
            Card(rank = "7", suit = "Hearts")
        ]
        
        hand = Hand()
        # 28th Jun, 2026
        hand.add_cards(cards)
        # 28th Jun, 2026
        
        self.assertEqual(
            hand.best_rank(),
            "Straight Flush"
        )    

    def test_figures_out_royal_flush_is_best_rank(self):
        cards = [
            Card(rank = "10", suit = "Hearts"),
            Card(rank = "Jack", suit = "Hearts"),
            Card(rank = "Queen", suit = "Hearts"),
            Card(rank = "King", suit = "Hearts"),
            Card(rank = "Ace", suit = "Hearts")
        ]
        
        hand = Hand()
        # 28th Jun, 2026
        hand.add_cards(cards)
        # 28th Jun, 2026
        
        self.assertEqual(
            hand.best_rank(),
            "Royal Flush"
        )

# 14th Jun, 2026