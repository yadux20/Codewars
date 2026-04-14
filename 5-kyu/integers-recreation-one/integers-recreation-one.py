def list_squared(m, n):
    res = []
    
    for num in range(m, n + 1):
        tot = 0
        
        i = 1
        while i * i <= num:
            if num % i == 0:
                tot += i * i
                
                if i != num // i:
                    tot += (num // i) * (num // i)
            
            i += 1
        
        root = int(tot ** 0.5)
        if root * root == tot:
            res.append([num, tot])
    
    return res