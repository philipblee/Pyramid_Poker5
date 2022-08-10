class ShowDownGame():
    """ ShowDownGame takes player_points and play_hand25 and determines
    player_wins, player_ante, player_surrender for this hand/deal"""
    def __init__(self, player_points, play_hand20):
        print ("Entering ShowDownGame")
        player_ante = [0,0,0,0,0,0,0]
        player_surrender = [0,0,0,0,0,0]
        player_wins = [0,0,0,0,0,0,0]
        all_surrender = True
        highest_points = 0
        number_players = 0

        # count the number of players playing, also find highest_points
        for i in range(6):
            if play_hand20[i] == True:
                number_players = number_players + 1
                all_surrender = False
            if player_points[i] > highest_points:
                highest_points = player_points[i]
        # print "highest_points", highest_points

        winning_player = [0, 0, 0, 0, 0, 0]
        winners = 0

        # find all players who "has" highest_points, to identify winner and number of winners
        for i in range(6):
            if player_points[i] == highest_points and play_hand20[i] == True:
                winning_player[i] = 1
                winners += 1

        ante = 0
        surrender = 0

        # If all surrender is False, then collect ante
        if all_surrender == False:
            players = 0
            for i in range(6):
                player_ante[i] += -10  # everyone ante's $10
                ante += +10

                if play_hand20[i] == True:
                    player_ante[i] += -10  # $10 to buy cards
                    ante += +10
                    players += 1

                else:
                    player_surrender[i] = max(-40,-10 * number_players)  # $40 to surrender
                    surrender += min(40, +10 * number_players)

            total_player_wins = 0
            for i in range(6):
                if winning_player[i] == 1:
                    player_ante[i] += ante / winners
                    player_surrender[i] = surrender / winners
                    player_wins[i] = 1 / winners

        self.number_players = number_players
        self.player_wins = player_wins
        self.player_ante = player_ante
        self.player_surrender = player_surrender
