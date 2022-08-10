from src.core.LegalPokerHands import *
from src.core.Card import *
import os
import pickle
from itertools import combinations

class HandDictionary(dict):
    """ HandDictionary is a class that creates the dictionary for probabilities based on a key which
        is tuple(hand) where hand is a legal hand of a tuple of cards, this will help replace
        probability file which relies on points and value with hand and value
        """

    def __init__(self):
        suit = 'SHDCSHDCSH'
        rank = 'AKQJT98765432'
        deck = [s + r for s in suit for r in rank]
        single_deck = [s + r for s in suit[0:4] for r in rank]

        all_non_pairs = []
        all_pairs = []
        all_trips = []
        print ("HandDictionary __init__ method executing")
        two_cards = []
        for c1 in single_deck:
            for c2 in single_deck:
                c3 = [c1] + [c2]
                two_cards.append(c3)
        # print("two cards", two_cards)

        trips = []
        for c1 in single_deck:
            for c2 in single_deck:
                for c3 in single_deck:
                    c4 = [c1] + [c2] + [c3]
                    trips.append(c4)

        for a in two_cards:
            if a[0][1] == a[1][1]:
                all_pairs.append(a)
            else:
                all_non_pairs.append(a)

        for a in trips:
            if a[0][1] == a[1][1] and a[0][1] == a[2][1]:
                all_trips.append(a)

        # print (all_pairs)
        # print (all_non_pairs)
        # print (deck)

        full_houses = []
        # create full house
        for trip in all_trips:
            for pair in all_pairs:
                if pair[0][1] != trip [0][1]:
                    full_house = list(trip)
                    full_house.append(pair[0])
                    full_house.append(pair[1])
                    # print (full_house)
                    # figure out the score stuff
                    best_hand = PokerHand(full_house)
                    x = best_hand.short_score
                    # print ("hand, x, ", full_house, x)
                    y = best_hand.get_points_from_hand(full_house, "6")[1]
                    new_hand_entry = [full_house, x, y]
                    full_houses.append(new_hand_entry)

        print ("full houses",len(full_houses))
        for full_house in full_houses[0:100]:
            print(full_house)
        # Use LegalPokerHands to find all legal hands and put them in hand1 through hand6
        legal_hands = LegalPokerHands(deck)

        # legal_hands.three_card_hands()
        # 1 - self.hand1 has hand, points and points
        # 2 - self.hand1_tuple only has hand tuple
        # 3 - self.hand_dups_removed has no duplicate hands

        added_hands = []
        remove_hands = []
        # # remove 4 card hands - then add 4 card hands with kickers
        for i in range(len(legal_hands.hand4)):
            # print(i, len(legal_hands.hand4[i][0]))
            if len(legal_hands.hand4[i][0]) == 4:
                # print (legal_hands.hand4[i][0])
                remove_hands.append(legal_hands.hand4[i])
                for card in (single_deck):
                    card_object = Card(card)
                    # print(card_object.card)
                    # print ("compare", card_object.rank, legal_hands.hand4[i][0][0][1])
                    if card_object.rank == legal_hands.hand4[i][0][0][1]:
                        pass
                    else:
                        # print (legal_hands.hand4[i][0], card)
                        new_hand = list(legal_hands.hand4[i][0])
                        new_hand.append(card)
                        # print (new_hand)
                        # figure out the score stuff
                        best_hand = PokerHand(new_hand)
                        x = best_hand.get_points_from_hand(new_hand, "6")[1]
                        y = best_hand.get_hand_score(new_hand)
                        new_hand_entry = [new_hand, y, x]
                        added_hands.append(new_hand_entry)
        print ("added hand count", len(added_hands))
        print ("hands removed", len(remove_hands))

        for hand in remove_hands:
            legal_hands.hand4.remove(hand)

        for hand in added_hands:
            legal_hands.hand4.append(hand)

        self.hand1 = legal_hands.hand1 + legal_hands.hand3 + legal_hands.hand4 + legal_hands.hand6 + full_houses
        print ("total legal hands in HandDictionary", len(self.hand1))

        x_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for hand in self.hand1:
            x_count[PokerHand(hand[0]).hand_key_values[0]] += 1
        print ("self.hand1 x_count", x_count)

        self.hand1_tuple = HandDictionary.Hand_Tuple(self, self.hand1)
        # self.hand_dups_removed = HandDictionary.DeDupe(self, self.hand1_tuple)
        self.hand_dups_removed = self.hand1_tuple



        self.hand_dictionary = {}

        x_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for hand in self.hand1:
            x_count[PokerHand(hand[0]).hand_key_values[0]] += 1
        print ("self.hand1 x_count", x_count)

        for i in range(len(self.hand_dups_removed)):
            my_hand = PokerHand(self.hand_dups_removed[i])
            hand_temp =  tuple(self.hand_dups_removed[i])

            # for one card hands - only in hand 1
            if len(self.hand_dups_removed[i]) == 1:
                points_temp1 = my_hand.get_points_from_hand(self.hand_dups_removed[i], "1")
                points_temp2 = my_hand.get_points_from_hand(self.hand_dups_removed[i], "2")
                points_temp3 = my_hand.get_points_from_hand(self.hand_dups_removed[i], "3")
                points_temp4 = my_hand.get_points_from_hand(self.hand_dups_removed[i], "4")
                if hand_temp not in self.hand_dictionary:
                    self.hand_dictionary[hand_temp] = [my_hand.hand_key_values, [False, points_temp1[1], points_temp2[1], points_temp3[1],
                                                                                 points_temp4[1], False, False], my_hand.final_hand_key]

            # for 3 card hands - only in hand 2, 3 or 4
            if len(self.hand_dups_removed[i]) == 3:
                points_temp2 = my_hand.get_points_from_hand(self.hand_dups_removed[i], "2")
                points_temp3 = my_hand.get_points_from_hand(self.hand_dups_removed[i], "3")
                points_temp4 = my_hand.get_points_from_hand(self.hand_dups_removed[i], "4")
                if hand_temp not in self.hand_dictionary:
                    self.hand_dictionary[hand_temp] = [my_hand.hand_key_values, [False, False, points_temp2[1], points_temp3[1], points_temp4[1], False, False],
                                                       my_hand.final_hand_key]
                else:
                    # retrieve and update
                    temp = self.hand_dictionary[hand_temp]
                    # print (temp)
                    temp[1][2] = points_temp2[1]
                    temp[1][3] = points_temp3[1]
                    temp[1][4] = points_temp4[1]
                    self.hand_dictionary[hand_temp] = temp

            # for 5 card hands, it's only in hand 3, 4, 5 or 6
            if len(self.hand_dups_removed[i]) == 5:
                points_temp3 = my_hand.get_points_from_hand(self.hand_dups_removed[i], "3")
                points_temp4 = my_hand.get_points_from_hand(self.hand_dups_removed[i], "4")
                points_temp5 = my_hand.get_points_from_hand(self.hand_dups_removed[i], "5")
                points_temp6 = my_hand.get_points_from_hand(self.hand_dups_removed[i], "6")
                # if it's flush, straight or house it cannot be hand 3 or 4, then just do hand 5 and 6
                if hand_temp[0] == 5 or hand_temp[0] == 6 or hand_temp[0] == 7:
                    pass
                else:
                    if hand_temp not in self.hand_dictionary:
                        self.hand_dictionary[hand_temp] = [my_hand.hand_key_values,
                                                           [False, False, False, points_temp3[1], points_temp4[1],
                                                            points_temp5[1], points_temp6[1]],
                                                           my_hand.final_hand_key]
                    else:
                        # retrieve and update
                        temp = self.hand_dictionary[hand_temp]
                        temp[1][3] = points_temp3[1]
                        temp[1][4] = points_temp4[1]
                        temp[1][5] = points_temp5[1]
                        temp[1][6] = points_temp6[1]
                        self.hand_dictionary[hand_temp] = temp

            # for 6 card hands, it's only in hand 4, 5 or 6
            if len(self.hand_dups_removed[i]) == 6:
                points_temp4 = my_hand.get_points_from_hand(self.hand_dups_removed[i], "4")
                points_temp5 = my_hand.get_points_from_hand(self.hand_dups_removed[i], "5")
                points_temp6 = my_hand.get_points_from_hand(self.hand_dups_removed[i], "6")
                if hand_temp not in self.hand_dictionary:
                    self.hand_dictionary[hand_temp] = [my_hand.hand_key_values,
                                                       [False, False, False, False, points_temp4[1],
                                                        points_temp5[1], points_temp6[1]],
                                                        my_hand.final_hand_key]
                else:
                    # retrieve and update
                    temp = self.hand_dictionary[hand_temp]
                    # print (temp)
                    temp[1][4] = points_temp4[1]
                    temp[1][5] = points_temp5[1]
                    temp[1][6] = points_temp6[1]
                    self.hand_dictionary[hand_temp] = temp

            # for 7 card hands, it's only in hand 5 or 6
            if len(self.hand_dups_removed[i]) == 7:
                points_temp5 = my_hand.get_points_from_hand(self.hand_dups_removed[i], "5")
                points_temp6 = my_hand.get_points_from_hand(self.hand_dups_removed[i], "6")
                if hand_temp not in self.hand_dictionary:
                    self.hand_dictionary[hand_temp] = [my_hand.hand_key_values,
                                                       [False, False, False, False, False,
                                                        points_temp5[1], points_temp6[1]],
                                                       my_hand.final_hand_key]
                else:
                    # retrieve and update
                    temp = self.hand_dictionary[hand_temp]
                    # print (temp)
                    temp[1][5] = points_temp5[1]
                    temp[1][6] = points_temp6[1]
                    self.hand_dictionary[hand_temp] = temp

           # for 8, 9 or 10 card hands, it's only in hand 6
            if len(self.hand_dups_removed[i]) == 8 or len(self.hand_dups_removed[i]) == 9\
                    or len(self.hand_dups_removed[i]) == 10:
                points_temp6 = my_hand.get_points_from_hand(self.hand_dups_removed[i], "6")
                if hand_temp not in self.hand_dictionary:
                    self.hand_dictionary[hand_temp] = [my_hand.hand_key_values, [False, False, False, False, False, False, points_temp6[1]],
                                                       my_hand.final_hand_key]
                else:
                    # retrieve and update
                    temp = self.hand_dictionary[hand_temp]
                    # print (temp)
                    temp[1][6] = points_temp6[1]
                    self.hand_dictionary[hand_temp] = temp

    def CreateDict(self, hand_tuples, hand):
        dictionary = {}
        my_hand = PokerHand()
        for i in range(len(hand_tuples)):
            points_temp = my_hand.get_points_from_hand(hand_tuples)
            hand_temp = tuple(hand_tuples[i])
            dictionary[hand_temp] = points_temp[1]

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
print("hand_dictionary", len(hd.hand_dictionary))

count_x = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
count = 0
for key,value in sorted(hd.hand_dictionary.items()):
    count_x[value[0][0]] += 1
    if (value [0][0] == 5 or
        value [0][0] == 6 or
        value [0][0] == 7 or
        value [0][0] == 8):
        pass
    else:
        count += 1
        # print(count, key, value)
print (count_x)
    # print("hand1 key: {0:30}     points: {1}".format(x, hd.hand_dictionary[x]))

count = 0
hand_dictionary_sorted = sorted(hd.hand_dictionary.items(), key=lambda x: x[1])


# for i in hand_dictionary_sorted:
#     if i[1][0][0] == 5 or i[1][0][0] == 6 or i[1][0][0] == 7or i[1][0][0] == 8:
#         pass
#     else:
#         print (count, i)
#     count += 1

print ("create key_value_dictionary")
key_value_dictionary = {}
for key,value in sorted(hd.hand_dictionary.items()):
    key_value_dictionary[tuple(value[0])] = [value[1], value[2]]

# for key,value in sorted(key_value_dictionary.items()):
#     if value[0][0] == 5 or value[0][0] == 6 or \
#         value[0][0] == 7 or value[0][0] == 8:
#         pass
#     else:
#         print (key, value)

count = 1
for i in key_value_dictionary:
    if count <3000:
        print (count , i)
    count += 1

# does key_values_dictionary.pkl exist?  If no, open the file
# os.path.dirname(__file__) gives us the directory of script
pathname = os.path.dirname(__file__) + "\\key_values.pkl"
print (pathname)

if os.path.exists(pathname):
    with open(pathname, "wb") as g:
        pickle.dump(key_value_dictionary, g)
else:
    with open(pathname, "wb") as g:
        pickle.dump(key_value_dictionary, g)