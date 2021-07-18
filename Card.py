class Card:

    def __init__(self, rank, suit):

        self.rank = rank
        self.suit = suit
    
    def show(self):
        print("{} of {}".format(self.rank, self.suit))

    def get_rank(self):
        return self.rank
    
    def get_suit(self):
        return self.suit

    
if __name__ == '__main__':
    card = Card("King", "Spades")
    card.show()