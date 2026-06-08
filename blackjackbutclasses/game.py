from cards import Deck, Hand
from exceptions import InsufficientFunds, InvalidMove,BetError

class GameEngine:
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
    def hit(self):
        if self._player_hand.is_bust():
            raise InvalidMove("You can't hit after busting")
        self._player_hand.add_card(self._deck.draw_card())
    def stand(self):
        while self._dealer_hand.score < 17:
            self._dealer_hand.add_card(self._deck.draw_card())
    def settle_round(self):
        if self._player_hand.is_bust():
            print("You bust!")
        elif self._dealer_hand.is_bust():
            print("Dealer busts!")
            self._balance += self._current_bet * 2
        elif self._player_hand.score > self._dealer_hand.score:
            print("You win!")
            self._balance += self._current_bet * 2
        elif self._player_hand.score < self._dealer_hand.score:
            print("you lose!")
        elif self._player_hand.score == self._dealer_hand.score:
            print("Tie!")
        self._current_bet = 0

