import math
def solution(n):
    cnt = 0 
    comb_arr = []
    for i in range(n+1):
        for j in range(n+1):
            # i 를 1만큼 j 를 2 만큼 comb arr
            sum = i + (j * 2)
            if sum == n:
                comb_arr.append([i, j])

    for c in comb_arr:
        cnt += math.comb(c[0]+c[1], c[0])
    # print(math.comb(6,0))
    # print(math.comb(6,6))
    
    return cnt % 1234567
            
            