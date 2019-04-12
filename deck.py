from card import Card
import os

class Deck(object):
    def __init__(self):
        self.cards = []
        self.populate()
    
    def populate(self):
        suits = ["H", "S", "C", "D"]
        numbers = [str(n) for n in range(2,11)] + ["J", "Q", "K", "A"]
        for suit in suits:
            for num in numbers:
                pic = os.getcwd() + '/PNG/' + num + suit + '.png'
                self.cards.append(Card(suit, num, pic))
        #self._cards = [ Card(s, n) for s in suits for n in numbers ]