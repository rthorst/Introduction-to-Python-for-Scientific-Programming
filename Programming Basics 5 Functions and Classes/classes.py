class Square:

    def __init__(self, length, width):

        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

    def get_perimeter(self):
        return 2 * (self.length + self.width)

    def larger_area_than_perimeter(self):
        return self.get_area() > self.get_perimeter()

s1 = Square(length=2, width=4)
s2 = Square(length=3, width=3)
print("Area of s1 = %s" % s1.get_area())
print("Area of s2 = %s" % s2.get_area())
print("Perimeter of s1 = %s" % s1.get_perimeter())
print("Perimeter of s2 = %s" % s2.get_perimeter())
print("Does s1 have larger area than perimeter? %s" % s1.larger_area_than_perimeter())

"""
Problem1: write a circle class.
     Circle is defined by its radius.
     Area : pi * r^2
     Circumference : 2 * pi * r

Write a method to get: area, circumference.


Problem 2: 
You are making two circular Atlanta United signs (hurray!). Your goal, of coures,
is to make the signs have as large a total area as possible. 
While making the signs,
you get into the following debate. Please resolve the debate using code.

You are required to make 2 signs.
The radii of the 2 signs must add up to 10
Each radius must be an integer > 0.  (thus 1 thru 10)

What are the optimal radii of the two signs? Check all possibilities. 



Problem 3: You asked a partcipant to fixate on a cross located at (0,0).
The problem is, you don't know if they actually did.
For analysis purposes, let's say a fixation counts if it's within a circle of
radius 2 from (00,).
Extend the circle class so that you can query whether some point, say
(1.5, 1.5), falls within the circle.

TEST CASES:
(1, 1) : True
(1.5, 1.5) : False
(1, 1.5) : True


HINT: a point is within the circle if the Euclidean 
distance from the center of the 
circle is less than the radius. 


"""


"""
Challenge:
Write a class to implement a playing card. It should have a suit and rank.
(J=11 ... A=14).

Add a function to test if the card has a higher rank than another card.

Write a Deck class. It should hold a list of cards. It should have a deal()
method. 

"""