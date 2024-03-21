def solution(numbers, target):

    def dfs(i, sum):
        nonlocal cnt
        if len(numbers) == i:
            if sum == target:
                cnt += 1
            return 
        else:
            dfs(i+1, sum+numbers[i])
            dfs(i+1, sum-numbers[i])
            return
    cnt = 0
    dfs(0, 0)
    return cnt
        
            
    