def solution(p, location):
    tmp_list = list(enumerate(p))
    cnt = 0
    while tmp_list:
        max_prior = max([v for idx, v in tmp_list])
        # print(max_prior)
        first = tmp_list.pop(0)
        # print(first)
        
        
        if first[1] < max_prior:
            tmp_list.append(first) # 다시 큐의 뒤로 넣는다.
            continue
        else:
            cnt += 1 # 실행된수
        
        if first[0] == location:
            return cnt
            # break
            
            
        
    