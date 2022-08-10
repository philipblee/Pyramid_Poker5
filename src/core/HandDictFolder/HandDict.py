from src.core.LegalPokerHands import *
import pickle

# not working properly - missing 3ks, 5ks, 6ks, etc.  not sure why

class HandDict(dict):
    """ HandDict is a class that creates the dictionary for probabilities based on a key which
        is tuple(hand) where hand is a legal hand of a tuple of cards, this will help replace
        probability file which relies on points and value with hand and value
        """

    def __init__(self):
        suit = 'SHDC'  # 6 suits give us 78 cards
        #1- 78, 2- 234, 3 and 4- 21092, 5 23,049, 6 23,093 = total 88,638, unique = 17,672
        rank = 'AKQJT98765432'
        deck = [s + r for s in suit for r in rank]
        print ("length of deck", len(deck))
        legal_hands = LegalPokerHands(deck)
        my_hand = PokerHand()
        hand_dict = {}
        hands = legal_hands.hand1 + legal_hands.hand2 + legal_hands.hand3 + legal_hands.hand4 + legal_hands.hand5 + legal_hands.hand6
        print (len(hands))

        hands_tuple = []
        for hand in hands:
            hands_tuple.append(tuple(hand[0]))
        hands_tuple.sort()

        hands_dedupe = HandDict.DeDupe(self, hands_tuple)
        print ("unique", len(hands_dedupe))

        for i in range(len(hands_dedupe)):
            v0 = my_hand.get_points_from_hand(hands_dedupe[i], "6")[0]
            v1 = my_hand.get_points_from_hand(hands_dedupe[i], "1")[1]
            v2 = my_hand.get_points_from_hand(hands_dedupe[i], "2")[1]
            v3 = my_hand.get_points_from_hand(hands_dedupe[i], "3")[1]
            v4 = my_hand.get_points_from_hand(hands_dedupe[i], "4")[1]
            v5 = my_hand.get_points_from_hand(hands_dedupe[i], "5")[1]
            v6 = my_hand.get_points_from_hand(hands_dedupe[i], "6")[1]
            hand_dict[hands_dedupe[i]] = [v0,v1,v2,v3,v4,v5,v6]

        print("keys in hand_dict", len(hand_dict))
        with open("hand_dict.pickle", "wb") as file:
            pickle.dump(hand_dict, file, protocol=pickle.HIGHEST_PROTOCOL)

        with open("hand_dict.pickle", "rb") as file:
            b = pickle.load(file)

        print (hand_dict == b)

        import sys
        original_stdout = sys.stdout
        with open("hand_dict.txt", "w") as f:
            sys.stdout = f
            for item in hand_dict:
                print(item, "/", hand_dict[item])
        sys.stdout = original_stdout

    def DeDupe(self, hand_tuples):
        """ goes through list of tuples and removes duplicates"""
        # import sys
        # original_stdout = sys.stdout
        # with open("hand_dict_output.txt", "w") as f:
        #     sys.stdout = f
        seen = []
        result = []
        for item in hand_tuples:
            fs = item
            if fs not in seen:
                result.append(item)
                # print ("keep", fs)
                seen.append(fs)
            # else:
            #     print ("delete", item)
        # sys.stdout = original_stdout
        return result

hd = HandDict()
