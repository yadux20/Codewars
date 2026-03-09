def is_isogram(string):
    s = string.lower()
    w = []
    for i in s:
        if i.isalpha:
            if i in w:
                return False
            w.append(i)
    return True