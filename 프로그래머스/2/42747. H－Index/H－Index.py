def solution(c):
    c.sort()
    # [0,1,3,5,6]
    
    l = len(c)
    ret = 0
    for i in range(l):
        v = c[i]
        over = l - i
        m = min(v, over)
        ret = max(ret, m)
        
    print(ret)
    return ret
    