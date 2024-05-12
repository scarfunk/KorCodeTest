import itertools


def solution(number):
    comb = itertools.combinations(number, 3)
    # print(list(comb))
    cnt = 0
    for three in list(comb):
        if sum(three) == 0:
            cnt += 1
            
    return cnt
    