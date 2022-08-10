suit = 'SHDC'
rank = 'AKQJT98765432'
deck_number = '+-*'
deck_of_cards = [s + r + d for s in suit for r in rank for d in deck_number]
deck_of_cards.extend(["WW+", "WW-", "WW*"])