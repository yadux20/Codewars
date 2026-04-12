def add_length(str_):
    s = str_.split()
    res=[f"{i} {len(i)}" for i in s]
    return res