def past(h, m, s):
    hs = 3600 * h
    ms = 60 * m
    sum = (hs + ms + s)*1000
    return sum