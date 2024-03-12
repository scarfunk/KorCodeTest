
def down(b):
    # 아래 행부터 올라가며 빈곳을 찾으면 내린다
    x = len(b)
    y = len(b[0])
    for i in range(x-1, 0, -1):
        for j in range(0, y):
            if b[i][j] == "": # 빈것을 찾았으면
                # print(f'{i}{j}')
                for k in range(i-1, -1, -1): # 열은 고정하고 행만 -1 씩 0 까지.
                    if b[k][j] != "": 
                        # print(f'kj:{k}{j}: {b[k][j]}')
                        b[i][j] = b[k][j] # 내리고 
                        b[k][j] = "" # 타겟은 비운다.
                        break # 1개 내렸으면 멈춤
    # print(b)
    return b

def bomb(b):
    cnt = 0
    x = len(b)
    y = len(b[0])
    my_set = set()
    for i in range(0, x-1):
        for j in range(0, y-1):
            if b[i][j] == "": # 빈거는 팡의 대상이 아니라 패스
                continue
            if b[i][j] == b[i+1][j+1] and b[i][j] == b[i+1][j] and b[i][j] == b[i][j+1]:
                my_set.add(tuple([i,j]))
                my_set.add(tuple([i+1,j]))
                my_set.add(tuple([i,j+1]))
                my_set.add(tuple([i+1,j+1]))
                
    # print(my_set)
    if len(my_set) == 0: # 터트릴게 없으면 재귀 종료
        return 0
    cnt = len(my_set)
    # 터트릴것들을 저장하고 한방에 터트린다.
    for (x,y) in my_set:
        b[x][y] = ""
    # print(b)
    b = down(b)
    return len(my_set) + bomb(b) # 다시 재귀를 하고 터트릴게 없으면 stop 한다.

def solution(m, n, board):
    ret = []
    for b in board:
        ret.append(list(b))
    result = bomb(ret)
    # print(result)
    return result

            