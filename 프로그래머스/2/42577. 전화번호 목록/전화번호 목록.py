def solution(p):
    p.sort()
    
    for i in range(1, len(p)):
        if p[i-1] in p[i][:len(p[i-1])]:
            return False
        
    return True
        
    
    
    
    