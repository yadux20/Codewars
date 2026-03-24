def find_multiples(n, limit):
    res = []
    for i in range(n, limit+1, n):
            res.append(i)
    return res