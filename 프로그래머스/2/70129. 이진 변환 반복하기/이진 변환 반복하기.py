def solution(s):
    cnt = 0
    removed = 0
    while s != "1":
        removed += s.count("0")
        only1 = s.replace("0", "")
        # print(len(only1))
        # ten = int(len(only1), 2)
        s = bin(len(only1))[2:]
        # print(s)
        cnt += 1
        
    return [cnt, removed]