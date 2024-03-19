import collections

def solution(participant, completion):
    pp = collections.Counter(participant)
    
    for c in completion:
        pp[c] -= 1
        if pp[c] == 0:
            del pp[c]
    
    # print(list(pp))
    return list(pp)[0]