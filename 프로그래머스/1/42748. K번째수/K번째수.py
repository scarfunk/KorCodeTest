def solution(array, commands):
    ret = []
    for (i,j,k) in commands:
        # print(f"{i} {j} {k}")
        ret.append(sorted(array[i-1:j])[k-1])
        
    # print(ret)
    return ret