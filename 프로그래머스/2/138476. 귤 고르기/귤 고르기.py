import collections

def solution(k, tgr):
    mem = collections.Counter(tgr)
    it = list(mem.values())
    it.sort(reverse=True)
    cnt = 0
    for v in it:
        # print( v)
        k -= v
        cnt += 1
        if k <= 0:
            break
        
    return cnt
        
        
        
    