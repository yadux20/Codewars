def get_sum(a,b):
    start = min(a,b)
    stop = max(a,b)
    sum=0
    for i in range(start, stop+1):
        sum+=i
    return sum