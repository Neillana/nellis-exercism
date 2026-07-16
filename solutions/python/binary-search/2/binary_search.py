def find(search_list, value):
    if not search_list or value not in search_list:
        raise ValueError("value not in array")

    first_index = 0
    last_index = len(search_list) - 1

    while first_index <= last_index:
        mid = first_index + (last_index - first_index) // 2

        if search_list[mid] < value:
            first_index = mid + 1
        elif search_list[mid] > value:
            last_index = mid - 1
        else:
            return mid
    return -1
