from src.core.Deck import *
from src.core.LegalPokerHands import *

pyramid_poker_list = Deck.deal()[0]
# pyramid_poker_list =['S2-', 'D3-', 'D2*', 'H2+', 'D2+', 'S4*', 'H8+', 'S9+', 'C7-', 'H7*', 'D9*', 'S7-', 'H5*', 'D7-', 'HA*', 'D6*', 'SA-', 'H4*', 'D3+', 'CT+', 'ST*', 'C7*', 'H4-', 'HQ-', 'C5-']
# pyramid_poker_list  =['CT-', 'H3*', 'S9+', 'D7-', 'D4-', 'CJ+', 'H5-', 'S8+', 'CK-', 'HT-', 'SQ+', 'D9+', 'H2+', 'H4*', 'H8-', 'SA-', 'H5+', 'H9+', 'SQ*', 'SJ-', 'SQ-', 'C4-', 'C2-', 'DQ*', 'H6-']
# ['WW*', 'SA+', 'DA-', 'SK*', 'SQ*', 'SJ+', 'SJ*', 'ST*', 'CT+', 'S9+', 'H8+', 'D8*', 'C8-', 'C8*', 'C7-', 'H6*', 'S5+', 'H5*', 'H4+', 'C4-', 'D3*', 'S2+', 'D2*', 'D2-', 'C2*']pyramid_poker_list = \
# pyramid_poker_list = \
# ['DA', 'DA', 'CA', 'HK', 'HQ', 'DQ', 'HJ', 'HJ', 'ST', 'HT', 'DT', 'CT', 'S9', 'H9', 'H8', 'D8', 'C8', 'D7', 'D7', 'D6', 'H5', 'D5', 'C5', 'H4', 'C3']
# ['DA+', 'DA*', 'CA-', 'HK+', 'HQ+', 'DQ+', 'HJ-', 'HJ*', 'ST*', 'HT*', 'DT-', 'CT-', 'S9+', 'H9*', 'H8*', 'D8-', 'C8*', 'D7*', 'D7-', 'D6*', 'H5-', 'D5-', 'C5-', 'H4*', 'C3*']
pyramid_poker_list = sorted(pyramid_poker_list, key=rank_sort, reverse=True)
print (pyramid_poker_list)

my_hand = LegalPokerHands(pyramid_poker_list)

hand6 = list(my_hand.hand6)
hand5 = list(my_hand.hand5)
hand4 = list(my_hand.hand4)
hand3 = list(my_hand.hand3)
hand2 = list(my_hand.hand2)
hand1 = list(my_hand.hand1)

hand6_count = len(hand6)
hand5_count = len(hand5)
hand4_count = len(hand4)
hand3_count = len(hand3)
hand2_count = len(hand2)
hand1_count = len(hand1)

print ("hand6")
for i in range(hand6_count):
    print (hand6[i])
print ("hand5")
for i in range(hand5_count):
    print (hand5[i])
print ("hand4")
for i in range(hand4_count):
    print (hand4[i])
print ("hand3")
for i in range(hand3_count):
    print (hand3[i])
print ("hand2")
for i in range(hand2_count):
    print (hand2[i])
print ("hand1")
for i in range(hand1_count):
    print (hand1[i])

print ("hand counts", hand6_count, hand5_count, hand4_count, hand3_count, hand2_count, hand1_count)