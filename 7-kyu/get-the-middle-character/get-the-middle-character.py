def get_middle(s):
    length = len(s)
    mid = length//2
    
    if length == 1 or length == 2:
        return s
    
    if length % 2 == 0:
        return s[mid-1:mid+1]
    else:
        return s[mid]