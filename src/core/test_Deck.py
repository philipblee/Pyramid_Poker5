from src.core.Deck import *

pyramid_poker_list = Deck.deal()[0]
print("\n25 card hand\n")
pyramid_poker_string = ', '.join(pyramid_poker_list)
print(pyramid_poker_string)
