def solution(p):
    result = []
    for i in range(len(p)):
        t = p[i]
        # print("t", t)
        ret = 0
        for j in range(i+1, len(p)):
            ret = len(p) - i - 1
            # print("pj:", p[j])
            if(t > p[j]):
                ret = j - i
                break
                
        result.append(ret)
        
    # print(result)
    return result
                