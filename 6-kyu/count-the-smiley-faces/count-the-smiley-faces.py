# import re
# def count_smileys(arr):
#     pattern = r"^[:;][-~]?[)D]$"
#     count  = 0
#     for i in arr:
#         if re.match(pattern, i):
#             count+=1
#     return count
def count_smileys(arr):
    eyes = {':', ';'}
    nose = {'-', '~'}
    mouth = {')', 'D'}
    count = 0
    
    for face in arr:
        if len(face) == 2:
            if face[0] in eyes and face[1] in mouth:
                count+=1
        elif len(face) == 3:
            if face[0] in eyes and face[1] in nose and face[2]in mouth:
                count += 1
                
    return count
    