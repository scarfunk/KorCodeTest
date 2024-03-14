
def recur(n, mem):
    if(n in mem):
        return mem[n]
    mem[n] = recur(n-2, mem) + recur(n-1, mem)
    return mem[n] % 1234567

def solution(n):
    mem = {0:0, 1:1}
    if n < 2:
        return mem[n]
    for i in range(2, n+1):
        mem[i] = (mem[i-2] + mem[i-1]) % 1234567
    return mem[n]
    
