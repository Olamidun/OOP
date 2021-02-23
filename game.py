import random
suite = 'H S D C'.split()

ranks = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
# print(cards)
# print(len(cards))

class Deck:
    
    def __init__(self, cards):
        self.cards = [(s,r) for s in suite for r in ranks]

    
    def split(self):
        return (self.cards[:26], self.cards[26:])

    def shuffle(self):
        random.shuffle(self.cards)

class Hand:

    def __init__(self, hand):

        self.hand = hand

    def __str__(self):
        return f"Contains {len(self.hand)} cards"

    def add(self):


           