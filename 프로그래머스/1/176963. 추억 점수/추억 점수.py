def solution(name, yearning, photo):
    res = []
    for p in photo:
        sum = 0
        for n in p:
            try:
                idx = name.index(n)
            except:
                continue
            sum += yearning[idx]
        res.append(sum)
        
    return res