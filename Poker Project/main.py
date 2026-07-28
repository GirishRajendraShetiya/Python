from poker.card import Card
from poker.deck import Deck

# 27th Jun, 2026
from poker.game_round import GameRound
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
player2 = Player(name = "Rajesh", hand = hand2)
# 27th Jun, 2026

# 28th Jun, 2026
players = [player1, player2]

game_round = GameRound(deck = deck, players = players)
game_round.play()
# 28th Jun, 2026

# 12th Jul, 2026
# print(player1.hand)
# print(player1.best_hand())
# print(player2.hand)
# print(player2.best_hand())

for player in players:
    print(f"{player.name} receives a {player.hand}")
    index, hand_name, hand_cards = player.best_hand()
    hand_cards_strings = [str(card) for card in hand_cards]
    hand_card_string = " and ".join(hand_cards_strings)
    print(f"{player.name} has a {hand_name} with a {hand_card_string}")

winner_name = max(players)
print(f"The winner is {winner_name.name}")

# 12th Jul, 2026

# from main import deck, card, game_round, hand1, hand2, player1, player2
