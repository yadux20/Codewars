def delete_nth(order,max_e):
    res = []
    freq = {}
    for i in order:
        if i in freq:
            freq[i] += 1
            if freq[i] <= max_e:
                res.append(i)
        else:
            freq[i] = 1
            res.append(i)
    return res