def mxdiflg(a1, a2):
    if not a1 or not a2:
        return -1
    
    min1 = min(len(s) for s in a1)
    max1 = max(len(s) for s in a1)
    min2 = min(len(s) for s in a2)
    max2 = max(len(s) for s in a2)
    
    return max(abs(max1 - min2), abs(max2 - min1))