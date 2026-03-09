def nb_year(p0, percent, aug, p):
    yrs = 0
    tot = p0
    while(tot<p):
        tot = int(tot+(tot *(percent*0.01))+aug)
        yrs += 1
    return yrs