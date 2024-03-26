def solution(n, words):

    word_set = set()
    seq = n # 3,4,5...
    
    prev_c = words[0][0]
    for w in words:
        if prev_c != w[0] or w in word_set:
            m_seq = seq % n # 0,1,2...
            turn = seq // n
            return [m_seq + 1, turn]
            # end
        else:
            word_set.add(w)
        prev_c = w[-1]
        seq += 1
    
    return [0,0]