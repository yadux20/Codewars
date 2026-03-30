def pipe_fix(nums):
    res = []
    sorts = sorted(nums)
    for i in range(min(sorts), max(sorts)+1):
        res.append(i)
    return res
    