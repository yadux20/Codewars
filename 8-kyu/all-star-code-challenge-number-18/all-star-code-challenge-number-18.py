def str_count(strng, letter):
    cnt = 0
    for i in strng:
        if i == letter:
            cnt+=1
    return cnt