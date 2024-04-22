def solution(data, col, row_begin, row_end):
    
    # col = 2 로 오름차순 > 동일하면 > 1번째로 내림차순 하여 정렬.
    # 4 2 9 > 2 2 6 > 1 5 10 > 3 8 3
    
    # S_row_begin ~ S_row_end = 2~3 까지
    # S_i 는 i 번째 row 의 각 컬럼의 i 로 나눈 나머지들의 합
    # i = 2 이고 2 2 6 에 대해
    # i = 3 이고 1 5 10 에 대해
    
    sortedList = sorted(data, key = lambda x: (x[col-1], -x[0]))
    
    # print(sortedList)
    
    arr = []
    for i in range(row_begin, row_end + 1):
        sum = 0
        # print(sortedList[i-1])
        for n in sortedList[i-1]:
            sum += n % i
        
        arr.append(sum)
        
    # print(arr)
    x = 0
    for i in arr:
        x ^= i
    return x
    
    
    