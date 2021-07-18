"""
Each class should have:
- docstring to provide documentation on how to use the class.
- __str__ magic method to give a meaningful string representation.
- a proper __repr__ magic method for representation in the interative shell, debugger, and other cases where string conversion does not happen.
- __eq__ and __lt__ so that it can be sorted and meaningfully compared with other instances.
- access control for each instance variable (public, read-only, value checked before changing)

if the class is a container for other classes:
- find out how many are held with len method
- be able to iterate over the items in the container
- may allow users to access items in container using square bracket index notation

print statement uses __repr__ to display objects
for comparisons, only 3 need to be implemented __eq__, __lt__, __le__ OR __eq__, __gt__, __ge__
"""

import random

class MSDie:
    """
    Multi-sided die

    Instance Variables:
        current_value
        num_sides

    """

    def __init__(self, num_sides):
        self.num_sides = num_sides
        self.current_value = self.roll()

    def roll(self):
        self.current_value = random.randrange(1,self.num_sides+1)
        return self.current_value

    def __str__(self):
        return str(self.current_value)

    def __repr__(self):
        return "MSDie({}) : {}".format(self.num_sides, self.current_value)

    def __eq__(self,other):
        return self.current_value == other.current_value

    def __lt__(self,other):
        return self.current_value < other.current_value

    def __le__(self, other):
        return self.current_value <= other.current_value

x = MSDie(6)
y = MSDie(7)

x.current_value = 6
y.current_value = 5

print(x == y)
print(x < y)
print(x > y)
print(x != y)
print(x<=y)
print(x>=y)
print(x is y)