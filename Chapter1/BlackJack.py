from Deck import Deck
from Deck import Hand

class Blackjack:
    #One-player blackjack with dealer
    #One round
    #No betting
    #Dealer hits on all 17
    #Ace is always 11
    def __init__(self):
        
        #Initialize dealer hand and player hand
        self.dealer_hand = Hand("Dealer")
        self.player_hand = Hand("Player")

    def play_round(self):
        #Simulate one round of blackjack
        
        #Initialize deck and shuffle for each round
        deck = Deck()
        deck.shuffle()

        #Deal cards to player and dealer
        self.player_hand.add_card(deck.draw())
        self.dealer_hand.add_card(deck.draw())
        self.player_hand.add_card(deck.draw())
        self.dealer_hand.add_card(deck.draw())

        #Show player cards and dealer upcard
        self.show_player_cards()
        self.show_dealer_cards(False)

        #Calculate initial scores
        player_score = self.calculate_score(self.player_hand)
        dealer_score = self.calculate_score(self.dealer_hand)

        #Check for blackjack
        if player_score == 21:
            if dealer_score == 21:
                print("Push. You and Dealer have blackjack.")
                self.show_dealer_cards()
                return None
            else:
                print("Blackjack! You Win!")
                self.show_dealer_cards()
                return None

        else:
            while True:
                #simulate player's turn

                draw = str(input("Would you like to draw another card? (y/n)"))
                
                if draw.lower() == 'y':
                    self.player_hand.add_card(deck.draw())
                    self.show_player_cards()
                    player_score = self.calculate_score(self.player_hand)
                    
                    if player_score > 21:
                        #check for bust
                        print("Busted!")
                        self.show_dealer_cards()
                        return None
                    elif player_score == 21:
                        #stop player turns once they hit 21
                        break
                elif draw.lower() == 'n':
                    break
                else:
                    print("Input not valid. Try again.")

            #simulate dealer's turn
            dealer_score = self.dealer_play(deck)
            
            #check ending conditions
            if dealer_score > 21:
                print("Dealer busted! You win!")
            elif player_score > dealer_score:
                print("You beat the dealer! You win!")
            elif player_score == dealer_score:
                print("Push.")
            else:
                print("Dealer Wins.")
            return None


    def show_player_cards(self):
        print("-" * 8, "Your Hand", "-" * 8)
        self.player_hand.show()

    def show_dealer_cards(self, dealer_turn=True):
        #Show dealer cards by default, show upcard if dealer_turn is false

        if dealer_turn:
            print("-" * 8, "Dealer's Hand", "-" * 8)
            self.dealer_hand.show()
        else:
            print("-" * 8, "Dealer's Card", "-" * 8)
            self.dealer_hand.cards[0].show()

    def calculate_score(self, hand):
        #Calculate score of hand
        #Ace is fixed at 11

        score = 0
        values = {
            "Ace": 11,
            "Two": 2,
            "Three": 3,
            "Four": 4,
            "Five": 5,
            "Six": 6,
            "Seven": 7,
            "Eight": 8,
            "Nine": 9,
            "Ten": 10,
            "Jack": 10,
            "Queen": 10,
            "King": 10
        }
        for card in hand.cards:
            score += values[card.get_rank()]
        return score

    
    def dealer_play(self, deck):
        #Simulates dealer turns
        #Dealer always hits on 17

        self.show_dealer_cards()
        while self.calculate_score(self.dealer_hand) <= 17:
            self.dealer_hand.add_card(deck.draw())
            self.dealer_hand.show()
        return self.calculate_score(self.dealer_hand)






if __name__ == "__main__":
    bj = Blackjack()
    bj.play_round()

