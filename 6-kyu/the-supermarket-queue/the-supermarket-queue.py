def queue_time(customers, n):
    tills = [0] * n
    
    for time in customers:
        idx = tills.index(min(tills))
        tills[idx] += time
        
    return max(tills)