def tower_builder(n):
    tower = []
    width = 2*n -1
    for i in range(1, n+1):
        stars = "*" * (2*i-1)
        tower.append(stars.center(width))
    return tower
        
​
            