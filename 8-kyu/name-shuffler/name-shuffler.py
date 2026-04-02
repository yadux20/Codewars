def name_shuffler(str_):
    s = str_.split()
    if len(s) > 1:
        s[0], s[-1] = s[-1], s[0]
    return " ".join(s)