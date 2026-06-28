from poker.card import Card
from poker.deck import Deck

# 27th Jun, 2026
from poker.hand import Hand
from poker.player import Player
# 27th Jun, 2026

# 28th Jun, 2026
from poker.game_round import GameRound
# 28th Jun, 2026

deck = Deck()
card = Card.create_standard_deck_of_52_cards()
deck.add_cards(card)

# deck.cards.extend(card) - This could be used but not recommeneded as it goes deep inside the card object, which is not required by the deck class.

# 27th Jun, 2026
hand1 = Hand()
hand2 = Hand()

player1 = Player(name = "Girish", hand = hand1)
player2 = Player(name = "Girish", hand = hand2)
# 27th Jun, 2026

# 28th Jun, 2026
players = [player1, player2]

# game_round = GameRound(deck = deck, players = players)
# game_round.play()
# 28th Jun, 2026

# from main import deck, card, hand1, hand2, player1, player2
