def unique_in_order(seq):
    res = []
#     if not seq:
#         return res
#     for i in range(len(seq)-1):
#         if seq[i+1] != seq[i]:
#             res.append(seq[i])
#     res.append(seq[-1])
#     return res
​
    for i in seq:
        if not res or res[-1] != i:
            res.append(i)
    return res
        
​
    