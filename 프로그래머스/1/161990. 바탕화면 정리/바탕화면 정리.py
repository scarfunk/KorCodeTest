def solution(wp):
    min_x = 50
    min_y = 50
    max_x = 0
    max_y = 0
    for i in range(len(wp)):
        s = wp[i]
        l = s.find("#")
        if l == -1:
            l = min_x
        r = s.rfind("#")
        if r == -1:
            r = max_x
        
        min_x = min(l, min_x)
        max_x = max(r, max_x)
        
        if "#" in s:
            min_y = min(min_y, i)
            max_y = max(max_y, i)
            
    return [min_y, min_x, max_y+1 , max_x+1]
        