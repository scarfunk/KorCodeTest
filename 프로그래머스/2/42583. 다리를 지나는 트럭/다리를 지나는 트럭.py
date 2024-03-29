def solution(br_len, weight, truck_weights):
    que = [0] * br_len # 다리길이만큼 0 으로 채워놓음
    sum_wei = 0
    result = 0
    while truck_weights:
        result += 1 # 진입에 1초를 항상더함.
        
        sum_wei -= que[0] # 빠져나갈 무게 제거
        que.pop(0) # 0번째 빠져나감
        que.append(0) # 마지막을 들어올수있게 0 삽입
        incoming = truck_weights[0]
        
        if que[-1] == 0 and sum_wei + incoming <= weight: # 마지막이 비고, 무게가 작으면
            t = truck_weights.pop(0)
            que[-1] = t
            sum_wei += t
    
    return result + br_len
            
            