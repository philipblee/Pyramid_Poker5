from src.core.LegalPokerHands import *


class HandDictionary(dict):
    """ HandDictionary is a class that creates the dictionary for probabilities based on a key which
        is tuple(hand) where hand is a legal hand of a tuple of cards, this will help replace
        probability file which relies on points and value with hand and value\
        """

    def __init__(self):
        suit = 'SHDC'
        rank = 'AKQJT98765432'
        deck = [s + r for s in suit for r in rank]
        print ("length of deck", len(deck))

        legal_hands = LegalPokerHands(deck)
        my_hand = PokerHand()
        # legal_hands.three_card_hands()
        # 1 - self.hand1 has hand, points and points
        # 2 - self.hand1_tuple only has hand tuple
        # 3 - self.hand1_dedup has no duplicate hands
        self.hand1 = legal_hands.hand1
        self.hand1_tuple = HandDictionary.Hand_Tuple(self, self.hand1)
        self.hand1_dedup = HandDictionary.DeDupe(self, self.hand1_tuple)
        self.hand1_dict = {}
        for i in range(len(self.hand1_dedup)):
            y = my_hand.get_points_from_hand(self.hand1_dedup[i], "1")
            z = tuple(self.hand1_dedup[i])
            self.hand1_dict[z] = y[1]
            
        self.hand2 = legal_hands.hand2
        self.hand2_tuple = HandDictionary.Hand_Tuple(self, self.hand2)
        self.hand2_dedup = HandDictionary.DeDupe(self, self.hand2_tuple)
        self.hand2_dict = {}
        for i in range(len(self.hand2_dedup)):
            # remove hands that are less than 5 cards
            if len(self.hand2_dedup[i]) < 5:
                y = my_hand.get_points_from_hand(self.hand2_dedup[i], "2")
                z = tuple(self.hand2_dedup[i])
                self.hand2_dict[z] = y[1]
        self.hand2_dictionary = {}
        self.hand2_dictionary = self.hand2_dict
        self.hand2_dict = self.hand2_dictionary
        
        self.hand3 = legal_hands.hand3
        self.hand3_tuple = HandDictionary.Hand_Tuple(self, self.hand3)
        self.hand3_dedup = HandDictionary.DeDupe(self, self.hand3_tuple)
        self.hand3_dict = {}
        for i in range(len(self.hand3_dedup)):
            y = my_hand.get_points_from_hand(self.hand3_dedup[i], "3")
            z = tuple(self.hand3_dedup[i])
            self.hand3_dict[z] = y[1]

        self.hand4 = legal_hands.hand4
        self.hand4_tuple = HandDictionary.Hand_Tuple(self, self.hand4)
        self.hand4_dedup = HandDictionary.DeDupe(self, self.hand4_tuple)
        self.hand4_dict = {}
        for i in range(len(self.hand4_dedup)):
            y = my_hand.get_points_from_hand(self.hand4_dedup[i], "4")
            z = tuple(self.hand4_dedup[i])
            self.hand4_dict[z] = y[1]

        # legal_hands.five_card_hands()
        self.hand5 = legal_hands.hand5
        self.hand5_tuple = HandDictionary.Hand_Tuple(self, self.hand5)
        self.hand5_dedup = HandDictionary.DeDupe(self, self.hand5_tuple)
        self.hand5_dict = {}
        for i in range(len(self.hand5_dedup)):
            y = my_hand.get_points_from_hand(self.hand5_dedup[i], "5")
            z = tuple(self.hand5_dedup[i])
            self.hand5_dict[z] = y[1]

        self.hand6 = legal_hands.hand6
        self.hand6_tuple = HandDictionary.Hand_Tuple(self, self.hand6)
        self.hand6_dedup = HandDictionary.DeDupe(self, self.hand6_tuple)
        self.hand6_dict = {}
        for i in range(len(self.hand6_dedup)):
            y = my_hand.get_points_from_hand(self.hand6_dedup[i], "6")
            z = tuple(self.hand6_dedup[i])
            self.hand6_dict[z] = y[1]

    def CreateDict(self, hand_tuples, hand):
        dictionary ={}
        my_hand = PokerHand()
        for i in range(len(hand_tuples)):
            y = my_hand.get_points_from_hand(hand_tuples)
            z = tuple(hand_tuples[i])
            dictionary[z] = y[1]
            
    def DeDupe(self, hand_tuples):
        """ goes through list of tuples and removes duplicates"""
        seen = set()
        result = []
        for item in hand_tuples:
            # print "item", item
            fs = frozenset(item)
            if fs not in seen:
                result.append(item)
                # print "result", result
                seen.add(fs)
        return result

    def Hand_Tuple(self, items):
        """ goes through items and saves hand into result"""
        result = []
        for hand, score, points in items:
            result.append(hand)
        return result

hd = HandDictionary()

print ("hand1_dict", len(hd.hand1_dict))
#
hand1_dict_sorted = sorted(hd.hand1_dict.items(), key=lambda x:x[0]) #, cmp=rank_sort)
hand2_dict_sorted = sorted(hd.hand2_dict.items(), key=lambda x:x[0])
hand3_dict_sorted = sorted(hd.hand3_dict.items(), key=lambda x:x[0])
hand4_dict_sorted = sorted(hd.hand4_dict.items(), key=lambda x:x[0])
hand5_dict_sorted = sorted(hd.hand5_dict.items(), key=lambda x:x[0])
hand6_dict_sorted = sorted(hd.hand6_dict.items(), key=lambda x:x[0])
#
for x in hd.hand1_dict:
    print (x, hd.hand1_dict[x])
    # print("hand1 key: {0:30}     points: {1}".format(x, hd.hand1_dict[x]))
#
print ("hand2_dict", len(hd.hand2_dict))
for x in hd.hand2_dict:
    print (x, hd.hand2_dict[x])

print ("hand3_dict", len(hd.hand3_dict))
for x in hd.hand3_dict:
    print (x, hd.hand3_dict[x])

print ("hand4_dict", len(hd.hand4_dict))
for x in hd.hand4_dict:
    print (x, hd.hand4_dict[x])

print ("hand5_dict", len(hd.hand5_dict))
for x in hd.hand5_dict:
    print (x, hd.hand5_dict[x])

print ("hand6_dict", len(hd.hand6_dict))
for x in hd.hand6_dict:
    print (x, hd.hand6_dict[x])
