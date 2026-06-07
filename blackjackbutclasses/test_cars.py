import  unittest
from cards import Card, Hand

class TestHandScoring(unittest.TestCase):
    def test_hand_score(self):
        hand = Hand()
        hand.add_card(Card("A", 'H'))
        hand.add_card(Card("10", "S"))
        self.assertEqual(hand.score, 21)
    def test_three_Aces(self):
        hand = Hand()
        hand.add_card(Card("A","H"))
        hand.add_card(Card("A","D"))
        hand.add_card(Card("A","C"))
        self.assertEqual(hand.score, 13)

if __name__ == '__main__':
    unittest.main()