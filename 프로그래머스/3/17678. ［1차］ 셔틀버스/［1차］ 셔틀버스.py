def solution(n, t, m, timetable):    
    # 버스는 승객이 다 안차도 출발한다.
    arr = []
    for tt in timetable:
        (hou,minu) = tt.split(":")
        d = (int(hou) * 60) + int(minu)
        arr.append(d)
    arr.sort() # 순방향소팅
    start = 9 * 60 - t # 9시 보다 -t 만큼 부터 시작
    
    for i in range(n-1): #  마지막 1개 루프는 미처리
        start = start + t # 9시부터 시작하며 증가
        cnt = 0
        # arr 에서 deque 를 m 만큼한다.
        for _ in range(m):
            if arr and arr[0] <= start: # m 만큼, arr 이 아직존재하고, 0번째가 출발보다 이전이면
                arr = arr[1:] # 0 번째를 제거하고 다시 루프 > 0번째 다시 검사.
            else:
                break # 출발시간보다 늦은 시간이 나오면 버스는 안차도 출발.
    
    # 마지막 1번 남은 루프
    start = start + t
    result = 0
    if len(arr) < m or arr[m-1] > start: # 남은 arr 이 m 보다 작거나, 마지막이 출발시간 보다 뒤면
        # 1) 출발이 0900 인데 arr 이 1개 [0850] 만 있다면, 가장늦은건 0900
        # 2) 출발이 0900 인데 arr 이 [..., 0910] 이면 0900 이어야 한다.
        result = start # 다음출발시간이 제일늦은 시간이다. 
    else:
        # [..., 0850] 으로 m 이 꽉찼다면 0849 로 새치기 해야 탈수 있다.
        result = arr[m-1] - 1 # 아니라면 마지막탑승 m idx 보다 1분을 빼야 탈수 있다.
         
    return f'{result//60:02d}:{result%60:02d}'
        
        
                

