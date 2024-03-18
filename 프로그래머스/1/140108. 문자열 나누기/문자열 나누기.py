def solution(s):
    first_c = None
    first_cnt = 0
    other_cnt = 0
    ret = 0
    for c in s:
        if first_c is None:
            first_c = c
            first_cnt += 1
            continue
            
        if c != first_c:
            # 다르면 카운트 한다.
            other_cnt += 1
        else:
            # 같으면 first cnt += 1 한다.
            first_cnt += 1
            
        if other_cnt == first_cnt:
            ret += 1
            # 모두 리셋
            first_c = None
            first_cnt = 0
            other_cnt = 0
    if first_c is not None:
        ret += 1
    
    return ret 