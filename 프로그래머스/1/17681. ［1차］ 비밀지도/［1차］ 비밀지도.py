def makeArr(arr, n):
    ret = []
    for a in arr:
        bi = bin(a)[2:].zfill(n)
        # print(bi)
        ret.append(bi)
    return ret

def solution(n, arr1, arr2):
    a1 = makeArr(arr1, n)
    a2 = makeArr(arr2, n)

    for i in range(0,n):
        str = ""
        for j in range(0,n):
            str += "#" if int(a1[i][j]) | int(a2[i][j]) == 1 else " "
        a1[i] = str
            
    # print(a1)
    return a1
    
