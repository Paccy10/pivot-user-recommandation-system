def convert_list_to_dict(given_list):
    new_dict = {}

    for x in given_list:
        key1 = list(x.keys())[0]
        key2 = list(x.keys())[1]
        new_dict[x[key1]] = x[key2]

    return new_dict


def sum_dict(dict1, dict2):
    new_dict = {}
    keys = list(dict1.keys()) + list(dict2.keys())

    for key in keys:
        val1 = dict1.get(key) if dict1.get(key) else 0
        val2 = dict2.get(key) if dict2.get(key) else 0

        new_dict[key] = val1 + val2

    return new_dict


def count_occurrences(string, substring):
    count = start = 0
    while True:
        start = string.find(substring, start) + 1
        if start > 0:
            count += 1
        else:
            return count


def multiply_dict(dict1, dict2, dict3):
    new_dict = {}
    keys = list(dict1.keys()) + list(dict2.keys()) + list(dict3.keys())
    for key in keys:
        val1 = dict1.get(key) if dict1.get(key) else 1
        val2 = dict2.get(key) if dict2.get(key) else 1
        val3 = dict3.get(key) if dict3.get(key) else 1

        new_dict[key] = round(val1 * val2 * val3, 3)

    return new_dict
