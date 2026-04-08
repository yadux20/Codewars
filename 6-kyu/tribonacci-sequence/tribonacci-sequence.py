def tribonacci(s, n):
    if n == 0:
        return []
    if n < 3:
        return s[:n]
    
    res = s.copy()
    for i in range(n-3):
        nxt = res[-1] + res[-2] + res[-3]
        res.append(nxt)
    return res
    