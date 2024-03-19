def solution(s):
    arr = []
    
    for c in s:
        if c == '(':
            arr.append(c)
        else:
            if arr:
                arr.pop()
            else:
                return False
    
    if arr:
        return False
    return True
            