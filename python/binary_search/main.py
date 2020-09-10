def binary_search(data, elem):
    low = 0
    high = len(data) - 1
    while low <= high:
        middle = data[int((low + high) / 2)]
        if middle == elem:
            return data[middle]
        elif middle < elem:
            low = data[middle] + 1
            continue
        else:
            high = data[middle] - 1
            continue
    return None

