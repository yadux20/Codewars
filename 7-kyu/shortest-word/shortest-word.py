def find_short(s):
    a = s.split()
    em = []
    for i in a:
        em.append(len(i))
    mini = min(em)
    return mini
        
            