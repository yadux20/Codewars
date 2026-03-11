def dig_pow(n, p):
    tot = 0
    for i in str(n):
        tot += int(i) ** p
        p += 1
    if tot % n ==0:
        return tot/n
    return -1