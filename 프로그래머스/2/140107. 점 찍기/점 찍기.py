from math import sqrt

def solution(k, d):
    cnt = 0
    for y in range(0, d+1, k):
        x = d ** 2 - y ** 2
        cnt += (sqrt(x) // k) + 1
        
    return cnt
        
        