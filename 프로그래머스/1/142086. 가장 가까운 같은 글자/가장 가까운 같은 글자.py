def solution(s):
    mem = {}
    ret = [];
    for i in range(len(s)):
        c = s[i]
        if c in mem:
            ret.append(i-mem[c])
        else:
            ret.append(-1)
        mem[c] = i
    return ret