def better_than_average(class_points, your_points):
    sum=0
    for i in class_points:
        sum=sum+i
    avg=sum/len(class_points)
    return True if your_points>avg else False  
        
    
        