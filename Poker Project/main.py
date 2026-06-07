from poker.card import Card
from poker.deck import Deck

deck = Deck()
card = Card.create_standard_deck_of_52_cards()
deck.add_cards(card)

# deck.cards.extend(card) - This could be used but not recommeneded as it goes deep inside the card object, which is not required by the deck class.

# from main import deck, card
