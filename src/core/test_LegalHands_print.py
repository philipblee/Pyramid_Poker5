from src.core.Deck import *
from src.core.LegalPokerHands import *
# from src.core.analyze_wild_fast import *
pyramid_poker_list = Deck.deal()[0]
# pyramid_poker_list = ['HA+', 'CA-', 'CK-', 'CQ+', 'CJ-', 'CT+', 'C9+', 'S8+', 'H8+', 'D8+', 'C8*', 'C8+', 'C7+', 'H6+', 'H6*', 'C6*', 'H5-', 'D5*', 'C5-', 'H4+', 'D4*', 'D3-', 'S2+', 'D2*', 'C2-']
# pyramid_poker_list =['S2-', 'D2-', 'D3*', 'H5+', 'D4+', 'S4*', 'H8+', 'S9+', 'C7-', 'H7*', 'D9*', 'S7-', 'H5*', 'D7-', 'HA*', 'D6*', 'SA-', 'H4*', 'D3+', 'CT+', 'ST*', 'C7*', 'H4-', 'HQ-', 'C5-']
pyramid_poker_list = ['C5-', 'H6-', 'C5*', 'CQ+', 'H8-', 'C7*', 'D7-', 'CT-', 'H6*', 'D5-', 'SQ*', 'H5+', 'C4+', 'S3*', 'H4*', 'SA+', 'S8+', 'C9*', 'DT+', 'S5*', 'CJ*', 'D5*', 'C4*', 'DT-', 'D8-']
print(pyramid_poker_list)
analysis = Analysis(pyramid_poker_list)
for i in range(31):
    print(i, analysis.suit_rank_array[i])

my_hand = LegalPokerHands(pyramid_poker_list)

hand6 = my_hand.hand6
hand5 = my_hand.hand5[1:]


hand4 = my_hand.hand4
# for hand in reversed(hand4):
#     if len(hand[0]) == 1:
#         hand4.remove(hand)

hand3 = my_hand.hand3[1:]
hand2 = my_hand.hand2[2:]
hand1 = my_hand.hand1

for hand in hand6:
    print("hand6", hand)
for hand in hand4:
    print("hand4", hand)
for hand in hand3:
    print("hand3", hand)
for hand in hand2:
    print("hand2", hand)
for hand in hand1:
    print("hand1", hand)

hand6_count = len(hand6)
hand5_count = len(hand5)
hand4_count = len(hand4)
hand3_count = len(hand3)
hand2_count = len(hand2)
hand1_count = len(hand1)

print(hand6_count, hand5_count, hand4_count, hand3_count, hand2_count, hand1_count)