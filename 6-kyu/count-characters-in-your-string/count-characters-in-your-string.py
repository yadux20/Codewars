def count(s):
    val = {}
    for i in s:
        if i in val:
            val[i] += 1
        else:
            val[i] = 1
    return val