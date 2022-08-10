from src.core.PokerHand import *

class ShowDownPoints():
    """ShowDownPoints takes points_stored and play_hand25 to determine
    the player_win_points and player_points"""
    def __init__(self, points_stored, hand_stored, play_hand20):
        player_names = ["Peter ", "Johnny", "Ming  ", "Tony  ", "Edmond", "Philip"]
        # calculate who wins how many points round robin
        # hands_stored is 1-6, points_stored is 1-6
        print("\nEntering ShowDownPoints")
        print()
        player_points = [0, 0, 0, 0, 0, 0]
        player_win_loss = ['', '', '', '', '', '']
        player_win_points = [[[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0]],
                             [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]],
                             [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]],
                             [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]],
                             [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]],
                             [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]],
                             [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]]

        this_hand = PokerHand()
        # print (player_win_points)
        # print ("\n", player_names[0],player_names[1],player_names[2],player_names[3],player_names[4],player_names[5])
        for i in range(6):  # i is player 1
            if play_hand20[i] == True:
                # print (player_names[i], i)
                temp_player_sum = 0
                for j in range(6):  # j is player 2
                    temp_hand_sum = 0
                    if play_hand20[j] == True:
                        for k in range(1, 7): # k is hand number
                            if i != j:
                                if points_stored[i][k][0] > points_stored[j][k][0]:
                                    player_win_points[i][j][k] = 1 * this_hand.get_winpoints_from_score(
                                        points_stored[i][k][0], str(k))
                                elif points_stored[i][k][0] < points_stored[j][k][0]:
                                    player_win_points[i][j][k] = -1 * this_hand.get_winpoints_from_score(
                                        points_stored[j][k][0], str(k))
                                elif points_stored[i][k][0] == points_stored[j][k][0]:
                                    # if points stored are equal, let's compare hands
                                    if hand_stored[i][k] == hand_stored[j][k]:
                                        if hand_stored[i][k] > hand_stored[j][k]:
                                            player_win_points[i][j][k] = 1 * this_hand.get_winpoints_from_score(
                                                points_stored[i][k][0], str(k))
                                        else:
                                            player_win_points[i][j][k] = -1 * this_hand.get_winpoints_from_score(
                                                points_stored[j][k][0], str(k))
                                    # if hands are equal, then it's fine, if not, use long score to determine winner
                                    player_win_points[i][j][k] = 0
                            # else:
                            #     player_win_points[i][j][k] = 0
                            # print ("i, j, k, player_win_points", i ,j, k, player_win_points[i][j][k])
                            temp_hand_sum += player_win_points[i][j][k]
                        player_win_points[i][j][0] = temp_hand_sum
                        # prints player_win_points[i][j] results of player i vs. player j - total, 6 hands
                        print ('{:>28}'.format(str(player_win_points[i][j])), end="")
                        player_win_loss[i] += str(player_win_points[i][j]) + ', '
                        temp_player_sum += temp_hand_sum
                        player_points[i] = temp_player_sum
                    # print("\ni versus j", i, j, player_names[i], player_names[j], player_win_points[i][j])
                print ('{:>5}'.format(temp_player_sum))
                # print("\nsummary", i, player_names[i], player_win_points[i])
                print()
        self.player_points = player_points
        self.player_win_points = player_win_points