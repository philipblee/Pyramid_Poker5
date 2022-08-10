# a playing card

class Card():
    def __init__(self, card):
        suit = "WCDHS"
        rank = "W123456789TJQKA"
        suit_name = ["Wild", "Clubs", "Diamonds", "Hearts", "Spades"]
        rank_name = ["Wild", "Ace", "Deuce", "Three", "Four", "Five", "Six",
                     "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]

        if len(card) > 3:
            print ("card is too many characters")
        self.card = card
        self.suit = card[0]
        self.rank = card[1]
        self.suit_value = suit.index(card[0])
        self.rank_value = rank.index(card[1])
        self.suit_name = suit_name[self.suit_value]
        self.rank_name = rank_name[self.rank_value]
        self.card_name = self.rank_name + " of " + self.suit_name
        # self.card_image =

# card1 = Card("SA+")
# print (card1.card)
# print (card1.card_name)
# print(card1.suit_value)
# print(card1.rank_value)
#
# card2 = Card("WW+")
# print (card2.card)
# print (card2.card_name)
# print(card2.suit_value)
# print(card2.rank_value)
#
# card3 = Card("DJ+")
# print (card3.card)
# print (card3.card_name)
# print(card3.suit_value)
# print(card3.rank_value)