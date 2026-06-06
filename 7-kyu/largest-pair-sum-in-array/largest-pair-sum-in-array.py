def largest_pair_sum(numbers): 
    s = sorted(numbers)
    return s[-1] + s[-2]
        