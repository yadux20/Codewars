def find_uniq(arr):
    a, b = list(set(arr))
    if arr.count(a) == 1:
        return a
    return b