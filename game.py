from guizero import App, Picture
from deck import Deck
import random

my_deck = Deck()

def deal_hand(size):
    hand = []
    for i in range(size):
        new_card = random.choice(my_deck.cards)
        hand.append(new_card)

    return hand

card_width = 86
card_height = 132
my_hand = deal_hand(5)

app = App(title="game")

for card in my_hand:
    Picture(app, image=card.pic, width=card_width, height=card_height, align='left')

'''
for i in range(5):
    Picture(app, image=my_deck.cards[i].pic, width=card_width,height=card_height, align='left')
'''
#test_pic = Picture(app, image=my_card.pic, width=card_width, height=card_height)
#test_pic = Picture(app, image="diamond.png", width=15, height=15)
app.display()