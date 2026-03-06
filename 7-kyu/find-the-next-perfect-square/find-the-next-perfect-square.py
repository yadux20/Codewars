def find_next_square(sq):
    sqr = sq**0.5
    if sqr % 1 ==0:
        return int((sqr+1)**2)
    else:
        return -1
​