def find_even_index(arr):
    tot = sum(arr)
    left_sum = 0
    
    for i in range(len(arr)):
        cur = arr[i]
        right_sum = tot - left_sum - cur
        if left_sum == right_sum:
            return i
        left_sum += cur
    return -1