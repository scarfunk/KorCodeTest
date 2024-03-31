def solution(s):
    s = s.replace("{{","")
    s = s.replace("}}","")
    x = s.split("},{")
    
    # print(x)
    arr = []
    for c in x:
        arr.append(c.split(","))
    
    arr.sort(key=len)
    # print(arr)
    
    res = []
    for g_list in arr:
        for g in g_list:
            g = int(g)
            if g not in res:
                res.append(g)
            
    return res
        
    