def find(search_list, value):
    if not search_list or value not in search_list:
        raise ValueError("value not in array")

    binary_list = sorted(search_list)
    middle = len(binary_list) // 2

    while value != binary_list[middle]:
        if value < binary_list[middle]:
            binary_list = binary_list[0:middle]
        elif value > binary_list[middle]:
            binary_list = binary_list[middle+1:]
        middle = len(binary_list) // 2

    return search_list.index(value)
