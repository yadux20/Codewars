def remove_smallest(numbers):
    if not numbers:
        return []
    
    smal = numbers.index(min(numbers))
    return numbers[:smal] + numbers[smal+1:]