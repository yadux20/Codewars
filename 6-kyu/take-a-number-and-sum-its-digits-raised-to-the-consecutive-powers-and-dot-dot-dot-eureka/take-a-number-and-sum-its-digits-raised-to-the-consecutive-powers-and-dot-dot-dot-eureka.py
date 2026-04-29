def sum_dig_pow(a, b): 
    res = []
    
    for i in range(a, b+1):
        s = str(i)
        tot = 0
        
        for j in range(len(s)):
            tot += int(s[j]) ** (j+1)
​
        if tot == i:
            res.append(tot)
        
    return res