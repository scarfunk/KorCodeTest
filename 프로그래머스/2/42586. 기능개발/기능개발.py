def solution(p, s):
    result = [] 
    while p:
        ret = 0
        while p and p[0] >= 100:
            p.pop(0)
            s.pop(0)
            ret += 1
        if ret > 0:
            result.append(ret)
        
        for i in range(0, len(p)):
        
            p[i] += s[i]
            
    return result
            