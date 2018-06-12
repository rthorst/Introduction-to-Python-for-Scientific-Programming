import numpy as np
import itertools

class Circle:

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return 3.14 * (self.radius ** 2)

    def get_perimeter(self):
        return 2 * 3.14 * self.radius

def euclidean_distance(arr1, arr2):
    dist = 0
    for i in range(len(arr1)):
        dist += ((arr1[i] - arr2[i]) ** 2)
    return dist


""" Atlanta United Signs """
for r1 in range(1, 10):  # 1-9
    r2 = 10 - r1
    c1 = Circle(radius=r1)
    c2 = Circle(radius=r2)
    area = c1.get_area() + c2.get_area()
    print("Radii : (%s, %s), Area = %s" % (r1, r2, area))

""" Distance from fixation"""
def is_fixation(coords):
    return euclidean_distance(coords, (0,0)) <= 2

coords = [
    (1.5, 1.5),
    (1, 1),
    (1, 1.5),
    (0.5, 1.6)
]
for (x, y) in coords:
    print("Gaze (%s, %s) : is fixation? --> %s" % (x, y, is_fixation((x,y))))

""" Playing cards, deck """
"""
Challenge:
Write a class to implement a playing card. It should have a suit and rank.
(J=11 ... A=14).

Add a function to test if the card has a higher rank than another card.

Write a Deck class. It should hold a list of cards. It should have a deal()
method. 

"""
class Card:

    def __init__(self, suit, rank):
        self.suit = suit # character: "C", "D", "H", "S"
        self.rank = rank # integer: 2-14, J=11 ... A=14

    def __str__(self):
        rank_strs = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]
        rank_to_str = {rank : str for rank, str in zip(np.arange(2,15), rank_strs)}
        return rank_to_str[self.rank] + self.suit

    def is_higher_rank_than(self, other_card):
        return self.rank > other_card.rank

class Deck:

    def __init__(self):
        self.cards = []

    def __str__(self):

        rank_strs = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]
        rank_to_str = {rank : str for rank, str in zip(np.arange(2,15), rank_strs)}
        suits = ["C","D","H","S"]
        suit_to_cards = {suit: [] for suit in suits}

        for card in self.cards:
            suit = card.suit
            rank = rank_to_str[card.rank]
            suit_to_cards[suit].append(rank)
        out = ""
        for suit in suits:
            out += "%s: %s\n" % (suit, ', '.join(suit_to_cards[suit]))
        return out

    def deal(self):

        suits = ["C","D","H","S"]
        ranks = np.arange(2,15)
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))
