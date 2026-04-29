def race(v1, v2, g):
    if v1 >= v2:
        return None
    time = g / (v2 - v1)
    tot_sec = int(time * 3600)
    hours = tot_sec  // 3600
    minutes = (tot_sec % 3600) // 60
    secs = tot_sec % 60
    
    return[hours, minutes, secs]
    
    