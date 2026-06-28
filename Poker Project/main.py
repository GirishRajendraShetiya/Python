from poker.card import Card
from poker.deck import Deck

# 27th Jun, 2026
from poker.hand import Hand
from poker.player import Player
# 27th Jun, 2026

deck = Deck()
card = Card.create_standard_deck_of_52_cards()
deck.add_cards(card)

# deck.cards.extend(card) - This could be used but not recommeneded as it goes deep inside the card object, which is not required by the deck class.

# 27th Jun, 2026
hand1 = Hand(cards = [])
hand2 = Hand(cards = [])

player1 = Player(name = "Girish", hand = hand1)
player2 = Player(name = "Girish", hand = hand2)
# 27th Jun, 2026

# from main import deck, card, hand1, hand2, player1, player2
