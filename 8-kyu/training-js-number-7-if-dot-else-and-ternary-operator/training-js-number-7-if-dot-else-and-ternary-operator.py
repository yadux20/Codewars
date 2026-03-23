def sale_hotdogs(n):
    sum = 0
    for i in range(1,n+1):
        if n < 5:
            sum += 100
        elif n >= 5 and n < 10:
            sum += 95
        else:
            sum += 90
    return sum