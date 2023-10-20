#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    result = (0, 0)
    for i in range(2):
        result[i] = tuple_a[i] + tuple_b[i]
    return (result)
def multiple_returns(sentence):
    if sentence == "":
        return (0, None)
    else:
        return (len(sentence), sentence[0])
def max_integer(my_list=[]):
    if not my_list:
        return (None)
    biggest_integer = my_list[0]
    for integer in my_list[1:]:
        if integer > biggest_integer:
            biggest_integer = integer
    return (biggest_integer)