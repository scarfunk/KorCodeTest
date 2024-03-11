def solution(n, m, section):
    painted_idx = 0
    cnt = 0
    for s in section:
        if(painted_idx >= s):
            continue
        painted_idx = s + m - 1
        cnt = cnt + 1
        
    return cnt
        