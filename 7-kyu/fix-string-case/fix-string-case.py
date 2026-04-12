def solve(s):
    lower = 0
    upper = 0
    
    for i in s:
        if i.isupper():
            upper += 1
        else:
            lower += 1
        
    if lower >= upper:
        return s.lower()
    else:
        return s.upper()