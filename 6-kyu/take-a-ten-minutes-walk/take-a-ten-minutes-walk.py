# def is_valid_walk(walk):
#     ns = 0
#     ew = 0 
#     if len(walk) == 10:
#         for i in walk:
#             if i == 'n': ns+=1
#             if i == 's': ns -=1
#             if i == 'e': ew +=1
#             if i == 'w': ew -=1
#     else:
#         return False
#     return ns==0 and ew==0
​
def is_valid_walk(walk):
    return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('w') == walk.count('e')