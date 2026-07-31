def find_longest(arr):
    longest = arr[0]
    
    for num in arr:
        if len(str(num)) > len(str(longest)):
            longest = num
            
    return longest