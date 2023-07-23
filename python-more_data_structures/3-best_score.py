def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    largest_value = float('-inf')
    largest_key = None

    for key in a_dictionary:
        item = a_dictionary[key]

        if item > largest_value:
            largest_value = item
            largest_key = key

    return largest_key
