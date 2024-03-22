def solution(answers):
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    a_cnt = 0
    b_cnt = 0
    c_cnt = 0
    for i in range(len(answers)):
        if a[i%5] == answers[i]:
            a_cnt += 1
        if b[i%8] == answers[i]:
            b_cnt += 1
        if c[i%10] == answers[i]:
            c_cnt += 1
    mx = max(a_cnt, b_cnt, c_cnt)
    ret = []
    if mx == a_cnt:
        ret.append(1)
    if mx == b_cnt:
        ret.append(2)
    if mx == c_cnt:
        ret.append(3)
        
    return ret
    