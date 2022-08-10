# TODO: 2019-08-23 - Done - replace the function analyze_wild with the class Analysis in the entire program
# TODO: 2019-08-23 - look for ways to vectorize specific parts of Pyramid-Poker3
# TODO: 2019-08-23 - write more unittests
# TODO: 2019-08-23 - streamline programming in general
# TODO: 2019-08-23 - improve performance in general
# TODO: 2019-08-23 - test performance using three identical decks - went from 969 seconds to 137 seconds.  Why does that work?
# TODO: 2019-08-23 - Done - BestHand25Wild = made code generic. No special case for zero wild cards -
# TODO: 2019-08-23 - Done - BestHand25 = fixed bug where hand4 and hand3 were not looping to number of hands -

# TODO: 2 Wild card hand - 54 wild combinations - 921.33 seconds
# TODO: 2 Wild card hand - 54 wild combinations - added 3,000 as best points to speed up... 496 seconds
# TODO: 2 Wild card hand - 54 wild combinations - using Analysis class instead of analyze_wild
# TODO: 2 Wild card hand - 54 wild combinations - 1031 seconds - moved counts for union and intersect to right place
# TODO: 2 Wild card hand - 54 wild combinations - added 3,000 as best points to speed up... 520 seconds
# TODO: 2 Wild card hand - 54 wild combinations - for hand6/hand5 - separated (intersect from h6>65 and hopeless) in if statement 20% slower even though less intersect by 3%
# TODO: 2 Wild card hand - 54 wild combinations - changed WildList to use Analysis instead of analyze_wild - 983 seconds
# TODO: 2 Wild card hand - 54 wild combinations - fixed a bug where it wasn't looking at all combinations.  Now it takes 2136 seconds
# TODO: 2 Wild card hand - 54 wild combinations - fixed a bug where it wasn't looking at all combinations.  Now it takes 2091 seconds
# TODO: 2 Wild card hand - 54 wild combinations - removed hands when hand 6 = hand 4,3,2, then when hand 5 = hand 4,3,2. 1305 seconds
# TODO: 2 Wild card hand - 54 wild combinations - start next loop at previous+1 also - 1217 seconds
# TODO: 2 Wild card hand - 54 wild combinations - use in operator instead of intersection for f -> does not work
# TODO: 2 Wild card hand - 54 wild combinations - trying isdisjoint for a-f - 1052 seconds --> isdisjoint = 77 seconds, intersection = 129 seconds
# TODO: interesting 3 routines make up 97% of time, Big 3 time consumers:  BestHand25 827, Set 115, isdisjoin 77 seconds
# TODO: interesting 3 routines make up 97% of time, Removed hands 4,3,2 if = to hand 6 or 5 - 968 seconds   -> 766, 103 and 68
# TODO: interesting 3 routines make up 97% of time, if not Three_Specials, then remove all hands 4, 3, 2 that are > 3 996 - no improvement at all  -> 780, 113, 72
# TODO: 2 Wild card hand - 5661 - 54 wild combinations - not performance.  Just changed to count_try versus count. slowed down 1045 seconds
# TODO: 2 Wild card hand - 6534 - just changed print formatting - 1034 seconds
# TODO: 2 Wild card hand - 2031 - try stop counting - must run alone to get good timing results - not valid when other programs running - 887 seconds  -> 687, 102, 68
# TODO: 2 Wild card hand - 2735 - put counts back in.... see how it goes - back to 949 seconds
# TODO: 2 Wild card hand - 7972 - v1-10 - simplified "max_hand1, etc." 900 seconds, 698, 104, 68
# TODO: 2 Wild card hand - 1744 - v1-10 - using Numpy instead of list for hand1,2,3,4,5,6 to see if it speeds up. Ended up taking 4224 seconds.  Much longer. I need to investigate.
# TODO: 2 Wild card hand - 1744 - v1-10 - Try SA SA took 609 secs, usually only takes 70 secs, answers correct for all 54 hands.  Counts are a little less.  3504, 546, 143
# TODO: 1314 - Use Try SA,SA to better understand why this is so slow - using list - total 72 seconds 56,10,5
# TODO: 8399 - using Numpy - 686 seconds - 554, 117, 15 - I notice 10 times the intersection!  619 million versus 58 million in list.
# TODO: 7943 - found a bug in LegalHands where no 3 specials existed, I did not remove hand4's that were more than 3 cards. - now SA,SA is 2.9 seconds
# TODO: 6195 - using list, need to rebaseline my timing again given that one bug - time is 65 seconds - 32, 9, 4 using list
# TODO: 5528 - using numpy, 81 seconds - 44, 10.4, 4.4
# TODO: need to solve this given just one hand with no wilds
# TODO: 106 - using list, 3.095 seconds, count are 55,708 ... in snagit i: 1.9m u:305,843 c:43,337
# TODO: 4032 - using numpy, 4,708 seconds, count are 49,371 ... in snagit i: 3.6m u:305,844 c:37,152 - why so many intersection?
# TODO: 5484 - using list, print h2...
# TODO: 9658 - using numpy, print h2...
# TODO: 5484 - using list, print h2 details
# TODO: 9658 - using numpy, print h2 details  ---> e is incorrect - need to fix
# TODO: 7463 - using numpy - 3.87 seconds - i:3.18m c:45,788  Total: 82,369
# TODO: ? - using list, print h2 details - 8.8 seconds - 5.34 on print - i=1.9M total: 55,708  b: 10,314, 43,337, d:13,220
# TODO: ? - using numpy, print h2 details - 7.68 seconds - 4.9 on print - i=1.3M total: 151,347  b:133,021
# TODO: ? - using list,  gets to 1006 and then beats all later point totals
# TODO: ? - using numpy = gets wrong answer - gets the right answer but does each hand from beginning to end
# TODO: ? - using numpy - start by limiting j - let's see if answer still correct --> working now, only difference is i:3.3m
# TODO: list and numpy versions are very close now - same answer and counts are the same except for i:.  Time is 3.188 for numpy-list and 2.795 for list or 14% slower 3.086 for numpy-numpy


# TODO: 8094 - using list - 2.88 seconds - i:1.9m c:43,337   Total: 55,708

# TODO: summary of time improvements:
# TODO: 2136, 2091, 1035, 1217, 1052, 968, 887, 949, 900

