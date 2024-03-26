def solution(people, limit):
    people.sort()
    
    i = 0
    j = len(people) - 1
    ret = 0
    while i <= j:
        sum = people[i] + people[j]
        if sum > limit:
            ret += 1
            j -= 1
        else:
            ret += 1
            i += 1
            j -= 1
    
    return ret
            
        