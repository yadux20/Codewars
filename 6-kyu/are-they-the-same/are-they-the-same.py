def comp(a1, a2):
    if a1 is None or a2 is None or len(a1) != len(a2):
        return False
    else:
        return sorted([x**2 for x in a1]) == sorted(a2)
    