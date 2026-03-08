def duplicate_encode(word):
    w = word.lower()
    res = ""
    for i in w:
        if w.count(i) == 1:
            res += "("
        else:
            res += ")"
    return res