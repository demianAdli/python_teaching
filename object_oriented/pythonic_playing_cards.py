import random as rd
"""
This module is developed by Alireza Adli (Demian) for dealing 
with playing cards.
Each card includes SUITS (heart, club, diamond or spade) which will be 
depicted by emojis and RANKS which are the usual poker ranks from 2 to Ace.

Class Card makes a single card while class Deck makes a whole deck using
class Card.
Class Hand can be used to represent arbitary numbers of cards as 
a group (hand).

Rank 10 is represented with 'T' for easing its calling in the code.

"""


class Card:
    ranks = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
             '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    suits = {'heart': '♥', 'club': '♣', 'diamond': '♦', 'spade': '♠'}

    def __init__(self, values, colors):
        self.values = values
        self.colors = colors

    @property
    def values(self):
        return self.__values

    @values.setter
    def values(self, values):
        if values in Card.ranks:
            self.__values = values
        else:
            print("It's not a number.")

    @property
    def colors(self):
        return self.__colors

    @colors.setter
    def colors(self, colors):
        if colors.lower() in Card.suits:
            self.__colors = Card.suits[colors.lower()]
        else:
            print("It's not a suit.")

    def __getitem__(self, item):
        """ba argooman 0, emtiaze kart ra barmigardanad
        ba baaghie adaad khaale kart ra"""
        if item == 0:
            answer = self.values
        else:
            answer = self.colors
        return answer

    def __str__(self):
        return f"{self.values + self.colors}"

    def __gt__(self, other):
        return Card.ranks[self.values] > Card.ranks[other.values]

    def __lt__(self, other):
        return not self.__gt__(other)

    def __eq__(self, other):
        return Card.ranks[self.values] == Card.ranks[other.values]

    def __ne__(self, other):
        return not self.__eq__(other)


class Deck:
    def __init__(self):
        self.cards = []
        self.build()
        rd.shuffle(self.cards)
        rd.shuffle(self.cards)

    def build(self):
        """Building the deck by iterating through two dictionaries
        ranks and suits which are the class attributes of the Card class"""
        self.cards = [Card(value, suit) for value in Card.ranks for suit in Card.suits]

    def __getitem__(self, num):
        return self.cards[num]

    def draw(self):
        """drawing cards from the deck"""
        return self.cards.pop()

    def __len__(self):
        return len(self.cards)

    def __str__(self):
        return ' '.join(str(card) for card in self.cards)


class Hand:
    def __init__(self, nums, deck):
        self.nums = nums
        self.hand = nums * []
        self.deal(deck)

    def deal(self, deck):
        """Creating the hand list using the draw method of the deck class"""
        for num in range(self.nums):
            self.hand.append(deck.draw())
        return self.hand

    def __getitem__(self, num):
        return self.hand[num]

    def __len__(self):
        return self.nums

    def __str__(self):
        return ' '.join(str(card) for card in self.hand)


if __name__ == "__main__":
    deck_01 = Deck()
    print(deck_01)
    hand_01 = Hand(5, deck_01)
    print(hand_01)
    print(deck_01)
    print(len(hand_01))
    print(hand_01[2])
    print(hand_01[2][1])
    print(len(deck_01))
    print(deck_01[0] > deck_01[1])


