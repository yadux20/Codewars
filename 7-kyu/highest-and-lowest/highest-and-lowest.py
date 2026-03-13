def high_and_low(n):
    lst = []
    for i in n.split():
        lst.append(int(i))
    a = max(lst)
    b = min(lst)
    return f"{a} {b}"