def solution(t, p):
    l = len(p)
    cnt = 0
    for i in range(len(t)-l+1):
        sliced = t[i:i+l]
        # print(sliced)
        if int(sliced) <= int(p):
            cnt += 1
            
    return cnt