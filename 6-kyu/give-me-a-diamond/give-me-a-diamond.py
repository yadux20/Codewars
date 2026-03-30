def diamond(n):
    if n <= 0 or n % 2 == 0:
        return None
    
    res = ""
    
    for i in range(1, n+1, 2):
        space = (n-i) // 2
        res += " " * space + "*" * i + "\n"
        
    for j in range(n-2, 0, -2):
        space = (n-j) // 2
        res += " " * space + "*" * j + "\n"
        
    return res