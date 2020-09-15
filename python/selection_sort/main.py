def selection_sort_v1(arr):
    res = []
    while arr:
        min_val = arr[0]
        if len(arr) == 1:
            res.append(min_val)
            break
        for i in range(1, len(arr)):
            min_val = min(min_val, arr[i])
        res.append(arr.pop(arr.index(min_val)))
    return res


def selection_sort_v2(arr, st=1):
    while True:
        if st == len(arr):
            break
        min_val = arr[st-1]
        idx = arr.index(min_val)
        for i in range(st, len(arr)):
            if min_val > arr[i]:
                arr[i], arr[idx], min_val = min_val, arr[i], arr[i]
                continue
        st += 1
    return arr