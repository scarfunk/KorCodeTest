def solution(babbling):
    # print(babbling)
    spk = ["aya", "ye", "woo", "ma"]
    not_spk = ["ayaaya", "yeye", "woowoo", "mama"]
    cnt = 0
    for bab in babbling:
        b = bab
        br = False
        for ns in not_spk:
            if b.find(ns) != -1:
                br = True
        if br:
            continue
        # print(b)
        for s in spk:
            b = b.replace(s, "X")
        b = b.replace("X", "")
        # print(b)
        if len(b) == 0:
            cnt = cnt +1
    
    return cnt