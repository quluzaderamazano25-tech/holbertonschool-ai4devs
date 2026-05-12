def get_last_n(items, n):
    result = []
    start = len(items) - n
    for i in range(start, len(items) + 1):
        result.append(items[i])
    return result


my_list = [10, 20, 30, 40, 50]
print(get_last_n(my_list, 3))
print(get_last_n(my_list, 5))