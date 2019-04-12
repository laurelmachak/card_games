class Card(object):
    def __init__(self,suit,number, pic):
        self._suit = suit
        self._number = number
        self.pic = pic

    def __repr__(self):
        #return self._number + " of " self._suit
        pass

    @property
    def suit(self):
        return self._suit

    @suit.setter
    def suit(self, suit):
        if suit in ["H", "S", "C", "D"]:
            self._suit = suit
        else:
            print("Not a suit!")

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, number):
        if number in ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]:
            self._number = number
        else:
            print("Not a card number!")