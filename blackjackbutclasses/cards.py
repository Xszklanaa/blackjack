

class Card:
    def __init__(self, value,suit):
        self._value = value
        self._suit = suit
    @property
    def value(self):
        return self._value
    @property
    def suit(self):
        return self._suit

    def _str(self):
        return f"{self._value}{self._suit}"
class Deck:
    def __init__(self, num_of_decs=4):
        self._cards = []
        self._num_of_decs = num_of_decs
    def reset_deck(self):
        values = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
        suits = ["H","D","C","S"]
        for i in range(self._num_of_decs):
            for value in values:
                for suit in suits:
                    self._cards.append(Card(value,suit))
    def draw_card(self):
        if len(self._cards) == 0:
            raise Exception("Deck is empty")
        else:
            return self._cards.pop()

class Hand:
    def __init__(self):
        self._cards = []
        self._score = 0
    @property
    def cards(self):
        return self._cards
    @property
    def score(self):
        return self._score

    def add_card(self, card):
        self._cards.append(card)
        self._score = self._calculate_score()
    def _calculate_score(self):
        total = 0
        aces = 0
        for card in self._cards:
            if card.value == "A":
                aces +=1
                total += 11
            elif card.value in ["J","Q","K","10"]:
                total += 10
            elif card.value in ["2","3","4","5","6","7","8","9"]:
                total += int(card.value)
        while total >21 and aces >0:
            total -= 10
            aces -=1
        return total



