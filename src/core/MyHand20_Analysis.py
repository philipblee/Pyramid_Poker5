# MyHand20 Analysis basically analyzes he first 20 cards to decide whether to play or not
# 04/29/2021
# How do I decide whether to play a 20 card hand?
# 1 - Look by ranks - how many trips/4Ks/5Ks, etc?
# 2 - Look by suits - is there a straight flush? Are there straight flush gaps?
# 2 - Do I have one or more wild cards?
# 3 - Let me see if mean and stdev change based on number of data points
# 4 - create match_card_list - ranks pairs, trips, etc.

from src.core.Analysis import *
from src.core.StraightFlushList import *
from src.core.BestHand25Wild import *

class MyHand20_Analysis(list):

    def __init__(self, card_list):
        ranks = "W123456789TJQKA"
        suits = "WCDHS"
        match_card_list = []
        card_list1 = (sorted(card_list, key=rank_sort, reverse=True))
        card_list_temp = list(card_list)
        MyHand20 = Analysis(card_list_temp)
        wilds = 0
        for card in card_list:
            if "WW" in card:
                wilds += 1

        for i in range (0,50):
            if len(MyHand20.suit_rank_array[i]) > 0:
                print (i, MyHand20.suit_rank_array[i])

        # match_card are cards in the remaining 139 cards
        # that myhand20_analysis a pair - 10, a trip - 9, etc.
        # Or how many of remaining 139 cards are good for me
        # match quality = 0-best, 1-good, 2-pretty good, 3-Ok
        # match_quality = [0,0,0,0]
        to_create = [[0, 0], [0, 0], [0, 0],
                     [0, 0], [0, 0], [0, 0],
                     [0, 0], [0, 0], [0, 0],
                     [0, 0], [0, 0], [0, 0]]
        for pair in MyHand20.pairs_list:
            print (pair, "pair")
            if ranks.index(pair[0][1]) >= 8:
                to_create[3][1] += 1
            else:
                to_create[3][0] += 1

        for trip in MyHand20.trips_list:
            print (trip, "trip")
            if ranks.index(trip[0][1]) >= 8:
                to_create[4][1] += 1
            else:
                to_create[4][0] += 1
                
        for fourk in MyHand20.fourks_list:
            print (fourk, "fourk")
            if ranks.index(fourk[0][1]) >= 8:
                to_create[5][1] += 1
            else:
                to_create[5][0] += 1
                
        for fivek in MyHand20.fiveks_list:
            print (fivek, "fivek")
            if ranks.index(fivek[0][1]) >= 8:
                to_create[6][1] += 1
            else:
                to_create[6



                ][0] += 1

        print (to_create, "to_create")
        # for fourk in MyHand20.fourks_list:
        #     print (fourk, "fourk")
        #     if ranks.index(fourk[0][1]) >= 2:
        #         match_quality[0] += 1
        # for fivek in MyHand20.fiveks_list:
        #     print (fivek, "fivek")
        #     if ranks.index(fivek[0][1]) >= 2:
        #         match_quality[0] += 1

        match_cards = MyHand20.pairs * 10
        match_cards += MyHand20.trips * 9
        match_cards += MyHand20.fourks * 8
        match_cards += MyHand20.fiveks * 7
        match_cards += MyHand20.sixks * 6

        # print (match_quality, "match_quality")
        for i in range (32,41):
            if len(MyHand20.suit_rank_array[i]) > 0:
                # print (MyHand20.suit_rank_array[i])
                match_card_list.extend(MyHand20.suit_rank_array[i])
        print (match_card_list)
        card_list_temp = list(card_list)

        # figure out myhand20_analysis quality - not all matches are the same


        # SF matches looks at # number of wilds that create
        # straight flushes - multiply by 3 for three decks
        # This undercounts, if it's open ended sf, then it
        # would be twice as many cards
        sf = StraightFlushList(card_list_temp)
        print ("StraightFlushList", sf)
        match_cards += len(sf.straightflush_list) * 3

        # each remaining wild card is a myhand20_analysis card
        match_cards += 3 - wilds

        # above analysis needs to be rethought - not right
        self.matches = match_cards

        # average matches, figures out the %myhand20_analysis * 5 cards
        # a 3 or higher is good.  Lower than 2 is not so good
        self.average_matches = round(match_cards * 5/139.0,2)
        print (match_cards, "number of match cards of 139", round(match_cards/139),3)
        # print ("# of Possible Matches per card - ", match_cards)
        # print ("Average Matches over 5 cards - ", self.average_matches)

        wild_cards = 0
        if card_list1[2][0:2] == "WW":
            wild_cards = 3
        elif card_list1[1][0:2] == "WW":
            wild_cards = 2
        elif card_list1[0][0:2] == "WW":
            wild_cards = 1

        small_trip = 0
        med_trip = 0
        high_trip = 0
        small_fourk = 0
        med_fourk = 0
        high_fourk = 0
        specials = 0

        # Print out wilds, singles, pairs, trips, etc.
        if wilds > 0:
            print ("Number of wilds", wilds,)
            specials = wild_cards

        if MyHand20.singles > 0:
            print ("Number of singles", MyHand20.singles, MyHand20.singles_list,)

        if MyHand20.pairs > 0:
            print ("Number of pairs", MyHand20.pairs, MyHand20.pairs_list,)

        if MyHand20.trips > 0:
            print ("Number of trips", MyHand20.trips, MyHand20.trips_list,)
            for trip in MyHand20.trips_list:
                # print trip
                if ranks.index(trip[0][1]) <= 5:
                    small_trip += 1
                elif ranks.index(trip[0][1]) <= 10:
                    med_trip += 1
                else:
                    high_trip += 1

        if MyHand20.fourks > 0:
            print ("Number of 4K's", MyHand20.fourks, MyHand20.fourks_list,)
            for fourks in MyHand20.fourks_list:
                specials += 1
                # print fourks
                if ranks.index(fourks[0][1]) <= 5:
                    small_fourk += 1
                elif ranks.index(fourks[0][1]) <= 10:
                    med_fourk += 1
                else:
                    high_fourk += 1

        if MyHand20.fiveks > 0:
            print ("Number of 5K's", MyHand20.fiveks, MyHand20.fiveks_list,)
            specials += 1

        if MyHand20.sixks > 0:
            print ("Number of 6K's", MyHand20.sixks_list,)
            specials += 1

        if MyHand20.sevenks > 0:
            specials += 1
            print ("Number of 7K's", MyHand20.sevenks_list,)

        if MyHand20.eightks > 0:
            specials += 1
            print ("Number of 8K's", MyHand20.eightks_list,)

        if MyHand20.nineks > 0:
            specials += 1
            print ("Number of 9K's", MyHand20.nineks_list,)

        if MyHand20.tenks > 0:
            specials += 1
            print ("Number of 10K's", MyHand20.tenks_list,)

        if MyHand20.five_card_straightflushes > 0:
            specials += 1
            print ("\nSF", MyHand20.five_card_straightflush)

        if MyHand20.five_card_straightflushes > 1:
            specials += 1

        if len(MyHand20.six_card_straightflush) > 0:
            specials += 1
            print ("6SF", MyHand20.six_card_straightflush,)

        if len(MyHand20.six_card_straightflush) > 1:
            specials += 1

        if len(MyHand20.seven_card_straightflush) > 0:
            specials += 1
            print ("7SF", MyHand20.seven_card_straightflush,)

        if len(MyHand20.seven_card_straightflush) > 1:
            specials += 1

        if len(MyHand20.eight_card_straightflush) > 0:
            specials += 1
            print ("8SF", MyHand20.eight_card_straightflush,)

        if len(MyHand20.eight_card_straightflush) > 1:
            specials += 1

        if len(MyHand20.nine_card_straightflush) > 0:
            specials += 1
            print ("9SF", MyHand20.nine_card_straightflush,)

        if len(MyHand20.nine_card_straightflush) > 1:
            specials += 1

        if len(MyHand20.ten_card_straightflush) > 0:
            specials += 1
            print ("10SF", MyHand20.six_card_straightflush,)

        if len(MyHand20.ten_card_straightflush) > 1:
            specials += 1

        hand20_hands = MyHand20.trips + MyHand20.fourks
        hand20_quality = high_fourk + high_trip + med_fourk + med_trip
        formed_hands = hand20_hands

        # Need to do better job here:
        # If I have three trips, I'm going
        # If I have two trips 8 or higher then I'm going
        # Needs more thought

        # print ("# of trips and 4K's - ", hand20_hands)
        # print ("# 4K's and better - ", specials)
        # print ("4 cards of a Straight Flush - ", len(sf.straightflush_list))

        # second try analysis
        # print ("v2 formed hands", formed_hands)
        # figure out possibilities for getting more formed hands - pairs
        # print ("v2 pairs in hand", MyHand20.pairs, MyHand20.pairs_list)
        # print("v2 more trip possibilities - cards=", MyHand20.pairs * 10)

        formed_hands_quality = 0
        # formed_hands_quality
        # 1st trip = trip Aces or better
        # 2nd trip = trip Jacks or better
        # 3rd trip = trip 8 or better
        # 1st special = K or better
        # 2nd special = T or better
        # 3rd special = anything
        # if MyHand20.trips >= 1:
        #     if int(MyHand20.suit_rank_array[33][0]) >= 14:
        #         formed_hands_quality += 1
        # if MyHand20.trips >= 2:
        #     if int(MyHand20.suit_rank_array[33][1]) >= 11:
        #         formed_hands_quality += 1
        # if MyHand20.trips >= 3:
        #     if int(MyHand20.suit_rank_array[33][2]) >= 8:
        #         formed_hands_quality += 1
        # if MyHand20.fourks >= 1:
        #     if int(MyHand20.suit_rank_array[34][0]) >= 13:
        #         formed_hands_quality += 1
        # if MyHand20.fourks >= 2:
        #     if int(MyHand20.suit_rank_array[34][1]) >= 10:
        #         formed_hands_quality += 1
        # if MyHand20.fourks >= 3:
        #     if int(MyHand20.suit_rank_array[34][2]) >= 2:
        #         formed_hands_quality += 1

        # print ("v2 formed quality hands", formed_hands_quality)


        if len(sf.straightflush_list) > 0:
            print ("cards that make Straight Flush(es) - ", sf.straightflush_list)

        # if hand20_hands >= 3:
        #     print (">=3 trips or 4K's, play")
        # elif hand20_hands >= 3 and wild_cards >=1:
        #     print (">=3 trips or 4K's and >= 1 wild_card, play")
        # elif specials >= 2:
        #     print (">=2 specials, play")
        # else:
        #     print ("don't play")
        self.match_card_list = match_card_list
        print (match_card_list, "match card list")

        self.hand20_signal = hand20_hands + len(sf.straightflush_list) + specials