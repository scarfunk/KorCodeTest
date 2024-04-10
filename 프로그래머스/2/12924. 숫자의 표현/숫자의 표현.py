def solution(n):
    left = 1
    cnt = 0
    while left <= n:
        sum = 0
        for x in range(left, n+1):
            sum += x
            if sum == n:
                cnt += 1
                break
            if sum > n:
                break
        
        left += 1
        
    # print(cnt)
    return cnt