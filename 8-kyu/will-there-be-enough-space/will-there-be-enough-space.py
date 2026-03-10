def enough(cap, on, wait):
    sum = cap - on
    if sum <= wait:
        return wait - sum
    else:
        return 0