def count_positives_sum_negatives(arr):
    sum = 0
    count = 0
    if len(arr)==0:
        return []
    for i in arr:
        if i >0:
            count+=1
        else:
            sum += i
    return [count, sum]