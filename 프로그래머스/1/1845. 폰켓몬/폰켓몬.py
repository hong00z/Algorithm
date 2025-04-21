from collections import Counter

def solution(nums):
    answer = 0
    n = len(nums)
    counter = len(Counter(nums))
    if n//2 > counter:
        answer = counter
    else:
        answer = n//2
    return answer