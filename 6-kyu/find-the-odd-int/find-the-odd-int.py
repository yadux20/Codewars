def find_it(seq):
    for i in seq:
        count = seq.count(i)
        if count % 2 != 0:
            return i