import collections
def solution(nums):
    max_get = len(nums) // 2
    cnt = collections.Counter(nums)
#     print(max_get)
    
#     print(cnt.keys())
#     print(len(cnt.keys()))
    
    return min(len(cnt.keys()), max_get)