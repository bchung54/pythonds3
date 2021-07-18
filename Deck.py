from Card import Card
import random

class Deck:

    ranks = ("Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King")
    suits = ("Diamond", "Club", "Heart", "Spade")

    def __init__(self):

        self.cards = []
        self.build()
    
    def build(self):
        self.cards = [Card(rank, suit) for suit in Deck.suits for rank in Deck.ranks]
        """for suit in Deck.suits:
            for rank in Deck.ranks:
                self.cards.append(Card(rank, suit))"""
            
    def show(self):
        for card in self.cards:
            card.show()

    def shuffle(self):
        for i in range(len(self.cards)):
            r = random.randint(0, len(self.cards) - 1)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def draw(self):
        return self.cards.pop()


class Hand(Deck):

    def __init__(self, label=''):
        self.cards = []
        self.label = label

    def add_card(self, card):
        self.cards.append(card)
    


    
    

if __name__ == "__main__":
    deck = Deck()
    deck.shuffle()
    deck.show()
    print("-"*10)
    x = deck.draw()
    x.show()
    a = Hand("John")
    b = Hand("Dealer")
    a.add_card(deck.draw())
    a.add_card(deck.draw())
    b.add_card(deck.draw())
    b.add_card(deck.draw())
    print(a.label, "Hand")
    a.show()
    print(b.label, "Hand")
    b.cards[0].show()
    