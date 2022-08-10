suit = "CDHSW"
rank = "123456789TJQKAW"
deck = "+-*!="

def suit_rank_sort(a):
    """ sorts by suit then rank"""
    # suit = "CDHSW"
    # rank = "123456789TJQKAW"
    if len(a) <= 1:
        return
    # print (a)
    return(suit.index(a[0])*14 + rank.index(a[1]))

def rank_sort(a):
    """ sorts by rank then suit"""
    # suit = "CDHSW"
    # rank = "123456789TJQKAW"
    # print("rank_sort", a)
    if len(a) <= 1:
        return
    return(rank.index(a[1])*10 + suit.index(a[0]))

def tuple_sort(input):
    print (input)
    print (type (input))
    # input_convert = tuple(input)
    # print (input_convert)
    new_tuple = input.split(sep = ",")
    # new_tuple = new_tuple.split(sep = ","d)
    print(new_tuple)
    # number_of_values = len(tuple)
    # final_key_value = 0
    # place = 21
    # for i in range(number_of_values):

        # final_key_value += key_val ** ((place-i)*2)
    return




