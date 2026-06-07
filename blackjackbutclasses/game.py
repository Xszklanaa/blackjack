from cards import Deck, Hand
from exceptions import InsufficientFunds, InvalidMove,BetError

class Game_engine:
    def __init__(self, start_balance=1000):
        self._balance = start_balance
        self._current_bet = 0
        self._deck = Deck()
        self._player_hand = None
        self._dealer_hand = None
    def place_bet(self, amount:int):
        if amount <= 0:
            raise BetError("Bet must be positive")
        if amount > self._balance:
            raise InsufficientFunds("Insufficient funds")
        self._current_bet = amount
        self._balance -= amount
    def start_round(self):
        self._player_hand = Hand()
        self._dealer_hand = Hand()
        self._player_hand.add_card(self._deck.draw_card())
        self._player_hand.add_card(self._deck.draw_card())
        self._dealer_hand.add_card(self._deck.draw_card())
        self._dealer_hand.add_card(self._deck.draw_card())



