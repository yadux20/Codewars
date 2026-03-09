def nb_year(p0, percent, aug, p):
    years=0
    popu=p0
    while(popu<p):
        popu=int(popu+(popu*(percent*0.01))+aug)
        years+=1
    return years    
        
        
    
    
    