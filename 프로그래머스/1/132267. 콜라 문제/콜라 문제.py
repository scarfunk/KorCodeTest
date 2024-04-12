def solution(a, b, n):
    res = 0
    while n >= a:
        v, m = n // a, n % a
        # print(v, m)
        if m == 0:
            n = v * b
        else:
            n = v * b + m
        res += v * b
        
    return res
            
        
    