"""Homework file for my students to have fun with some algorithms! """


def find_greatest_number(incoming_list):
    return max(incoming_list)


def find_least_number(incoming_list):
    return min(incoming_list)


def add_list_numbers(incoming_list):
    total_sum = 0
    if incoming_list is None:
        total_sum = 0
    else:
        total_sum = sum(incoming_list)
    return total_sum


def longest_value_key(incoming_dict):
    try:
        key_result = None
        max_value = 0
        for key in incoming_dict:
            if len(incoming_dict[key]) > max_value:
                max_value = len(incoming_dict[key])
                key_result = key
    except:
        incoming_dict = None

    return key_result
