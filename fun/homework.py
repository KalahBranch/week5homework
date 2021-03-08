"""Homework file for my students to have fun with some algorithms! """


def find_greatest_number(incoming_list):
    return max(incoming_list)
    pass


def find_least_number(incoming_list):
    return min(incoming_list)
    pass


def add_list_numbers(incoming_list):
    if incoming_list is None:
        totalSum = 0
    else:
        totalSum = sum(incoming_list)
    return totalSum
    pass


def longest_value_key(incoming_dict):
    maxKeyLength = 0
    longestKey = "finalkey"
    if incoming_dict is None:
        return longestKey is None

    if len(incoming_dict) == 0:
        return longestKey is None

    for key in incoming_dict:
        if len(incoming_dict[key]) > maxKeyLength:
            maxKeyLength = len(incoming_dict[key])
            longestKey = key
    return longestKey
    pass
