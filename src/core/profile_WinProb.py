import cProfile
import PokerHand

def test1():
    win = PokerHand()
    win.get_prob(71412,"5")
    # print (win.points, win.hand, win.prob)
    #
    # win.get_prob(91312, "6")
    # print (win.points, win.hand, win.prob)
    #
    # win.get_prob(91312, "5")
    # print (win.points, win.hand, win.prob)

    print (win.get_points_from_hand(['SA','SK','SQ','SJ','ST'], "6"))

    # print (points_from_hand(['SA','SK','SQ','SJ','ST'], "5"))
    #
    # print (points_from_hand(['SA','SK','SQ','SJ','ST'], "4"))
    #
    # print get_points_from_score(91312, "6")
    #
    # print get_points_from_score(91312, "5")
    #
    # print get_points_from_score(91312, "4")

cProfile.run('test1()')