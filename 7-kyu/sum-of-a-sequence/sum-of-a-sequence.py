def sequence_sum(begin, end, step):
    res = 0
    for i in range(begin, end+1, step):
        if begin > end:
            return 0
        else:
            res += i
    return res