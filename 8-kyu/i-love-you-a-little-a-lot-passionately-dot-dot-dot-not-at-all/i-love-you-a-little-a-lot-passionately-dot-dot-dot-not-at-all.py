def how_much_i_love_you(nb):
    l=["I love you",
        "a little",
        "a lot",
        "passionately",
        "madly",
        "not at all"]
    for i in l:
        return l[(nb-1)%6]
        