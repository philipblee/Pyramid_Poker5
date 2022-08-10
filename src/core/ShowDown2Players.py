from src.core.PokerHand import *

class ShowDownPoints2Players():
    """ShowDownPoints takes points_stored and play_hand25 to determine
    the player_win_points and player_points"""
    def __init__(self, points_stored):
        player_names = ["Peter ", "Johnny", "Ming  ", "Tony  ", "Edmond", "Philip"]
        # calculate who wins how many points round robin
        # hands_stored is 1-6, points_stored is 1-6
        player_points = [0, 0, 0, 0, 0, 0]
        player_win_loss = ['', '', '', '', '', '']
        player_win_points = 7 * [7 * [[0, 0, 0, 0, 0, 0, 0]]]
        this_hand = PokerHand()
        # print player_win_points
        for i in range(6):  # i is player 1
            print (player_names[i], i, end="")
            temp_player_sum = 0
            for j in range(6):  # j is player 2
                temp_hand_sum = 0
                for k in range(1, 7): # k is hand number
                    if i != j:
                        if points_stored[i][k][0] > points_stored[j][k][0]:
                            player_win_points[i][j][k] = 1 * this_hand.get_winpoints_from_score(
                                points_stored[i][k][0], str(k))
                        elif points_stored[i][k][0] < points_stored[j][k][0]:
                            player_win_points[i][j][k] = -1 * this_hand.get_winpoints_from_score(
                                points_stored[j][k][0], str(k))
                        elif points_stored[i][k][0] == points_stored[j][k][0]:
                            player_win_points[i][j][k] = 0
                    else:
                        player_win_points[i][j][k] = 0
                    # print i,j,k,player_win_points[i][j][k]
                    temp_hand_sum += player_win_points[i][j][k]
                player_win_points[i][j][0] = temp_hand_sum
                print ('{:>29}'.format(str(player_win_points[i][j])), end="")
                player_win_loss[i] += str(player_win_points[i][j]) + ', '
                temp_player_sum += temp_hand_sum
                player_points[i] = temp_player_sum
            # print '{:^180}'.format(str(player_win_points[i]))
            print ('{:>5}'.format(temp_player_sum))
        self.player_win_points = player_win_points
        self.player_points = player_points
