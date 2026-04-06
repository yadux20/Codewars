def dir_reduc(arr):
    opposite = {
        "NORTH" : "SOUTH",
        "SOUTH" : "NORTH",
        "EAST" : "WEST",
        "WEST" : "EAST"
    }
    
    res = []
    
    for i in arr:
        if res and opposite[i] == res[-1]:
            res.pop()
        else:
            res.append(i)
    return res