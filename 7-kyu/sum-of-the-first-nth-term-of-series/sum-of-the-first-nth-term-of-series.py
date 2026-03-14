def series_sum(n):
    res = 0
    for i in range(1, n+1):
        res += 1/(3*i - 2)
    return f"{res:.2f}"