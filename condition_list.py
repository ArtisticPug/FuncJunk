""" 
Функции написаны с целью поиска "одновременных" промежутков в датасетах

"""

def append_func(item1, list):
    compare_list = []
    compare_list.append(item1)
    for el in list:
        if el['start'] >= item1['start'] and el['start'] < item1['end']:
            append = True
        else:
            return len(compare_list)
        for item in compare_list:
            if el['start'] < item['end']:
                pass
            else:
                append = False
        if append:
            compare_list.append(el)
    return len(compare_list)


def count_func(list):
    count = 0
    for el in list:
        rest_list = list[(list.index(el)+1):]
        meta_result = append_func(el, rest_list)
        if meta_result > count:
            count = meta_result
    return count


list = [
    {'start': 1, 'end': 10},
    {'start': 2, 'end': 3},
    {'start': 4, 'end': 5},
    {'start': 6, 'end': 7},
    {'start': 8, 'end': 9},
]

list2 = [
    {'start': 1, 'end': 5},
    {'start': 2, 'end': 6},
    {'start': 3, 'end': 8},
    {'start': 4, 'end': 8},
    {'start': 5, 'end': 9},
    {'start': 6, 'end': 10},
    {'start': 7, 'end': 11},
    {'start': 8, 'end': 12},
    {'start': 9, 'end': 13},
    {'start': 2, 'end': 14},
    {'start': 3, 'end': 15},
    {'start': 4, 'end': 16},
    {'start': 5, 'end': 12},
    {'start': 6, 'end': 12},
    {'start': 7, 'end': 14},
]

list = sorted(list, key=lambda k: k['start'])  # Сортированный список
list2 = sorted(list2, key=lambda k: k['start'])  # Сортированный список

print(count_func(list))
print(count_func(list2))
