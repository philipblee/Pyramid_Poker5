from BestHand25Wild import *
from ShowDownPoints import *
import global_variables

k_num = 0
wild_count = [0, 0, 0, 0]


class PlaySixHands25():

    """ Given six_hands, PlaySixHands25 plays all six hands and determines:
        self.points_stored = points_stored
        self.hand_stored = hands_stored
        self.player_score_hand20 = player_score_hand20
        self.play_hand20_quality = play_hand20_quality
        self.player_score_prediction = player_score_prediction
        self.play_hand25 = play_hand25
        self.player_wilds = player_wilds

        after that it uses ShowDownPoints to determine:
        self.player_points = winpoints.player_points
        self.player_win_points = winpoints.player_win_points
         """
    def __init__(self, six_hands):
        global k_num, wild_count
        my_hand = PokerHand()
        best = [[],[],[],[],[],[],[],[]]
        play_hand20_quality = ["", "", "", "", "", "", ""]
        player_score_hand20 =[0,0,0,0,0,0]
        player_names = ["Peter ", "Johnny", "Ming  ", "Tony  ", "Edmond", "Philip"]
        self.player_names = player_names
        player_score_prediction = [0, 0, 0, 0, 0, 0, 0]
        points_stored = [[], [], [], [], [], [], []]
        hands_stored = [[], [], [], [], [], [], []]
        hand20_signal = [0, 0, 0, 0, 0, 0]
        player_wilds = [0, 0, 0, 0, 0, 0]
        play_hand25 = [True, True, True, True, True, True, True]
        for hand_number in range(6):
            card_list = six_hands[hand_number]
            # print card_list
            card_list2_unsorted = list(card_list[0:NUMBER_OF_CARDS])  # deal number_of_cards
            card_list2 = (sorted(card_list2_unsorted, key=rank_sort, reverse=True))
            wild_cards = 0
            # count number of wild cards
            if card_list2[2][0:2] == "WW":  wild_cards = 3
            elif card_list2[1][0:2] == "WW":  wild_cards = 2
            elif card_list2[0][0:2] == "WW":  wild_cards = 1

            if wild_cards == 1:  wild_count[1] += 1
            elif wild_cards == 2:  wild_count[2] += 1
            elif wild_cards == 3:  wild_count[3] += 1

            player_wilds[hand_number] = wild_cards
            player_wilds[hand_number] = wild_cards

            print("\nGame#", k_num + 1, "Hand#", (k_num) * 6 + hand_number + 1, "One Wild=", wild_count[1],
                  "Two Wild=", wild_count[2], "Three Wild=", wild_count[3], "=========== New Hand ===============")

            # Look at 25 cards and decide what to do
            card_list25 = list(card_list2_unsorted[0:25])
            card_list25 = (sorted(card_list25, key=rank_sort, reverse=True))
            # print (player_names[hand_number], "is the player.  Analysis to follow.")
            print(card_list25)
            card_list1 = list(card_list25)
            myhand = BestHand25Wild(card_list1)
            points = myhand.best_hand_points
            best_25handx = myhand.best_25handx
            best[hand_number] = myhand.best_25handx
            points_stored[hand_number] = points
            hands_stored[hand_number] = best_25handx

            # print out the best hands
            global_variables.best_scores_list.sort(key=lambda t: t[0], reverse=True)
            for i in range(1, 7):
                hand_description_string = my_hand.get_description_from_score(points[i][0], str(i))
                print('{:>10}'.format(hand_description_string), end=" ")
            print()

        k_num += 1
        # save_wins = -1

        sd_points = ShowDownPoints(points_stored, hands_stored, play_hand25)
        # sd_game = ShowDownGame(sd_points.player_points, play_hand25)

        self.points_stored = points_stored
        self.hand_stored = hands_stored
        self.player_score_hand20 = player_score_hand20
        self.play_hand20_quality = play_hand20_quality
        self.player_score_prediction = player_score_prediction
        self.play_hand25 = play_hand25
        self.player_wilds = player_wilds
        self.hand20_signal = hand20_signal

        # sd_points = ShowDownPoints(points_stored, play_hand25)
        self.player_points = sd_points.player_points
        self.player_win_points = sd_points.player_win_points

        # print()
        for i in range(6):
            print("player", i, end="")
            print('{:8}'.format(player_names[i]), end=" ")
            print(points_stored[i])

        print()
        for i in range(6):
            print('{:8}'.format(player_names[i]), end=" ")
            for j in range(1,7):
                hand_description_string = my_hand.get_description_from_score(points_stored[i][j][0], str(j))
                print ('{:>12}'.format(hand_description_string), end="")
            print()
        self.best_pyramid_hands = best
        return