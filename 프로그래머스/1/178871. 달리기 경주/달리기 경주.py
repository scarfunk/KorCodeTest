def solution(players, callings):
    dict = {str: i for i, str in enumerate(players)}
    # print(dict)
    for c in callings:
        idx = dict[c]
        prev = players[idx - 1]
        (players[idx], players[idx-1]) = players[idx - 1],  players[idx]
        dict[c] -= 1
        dict[prev] += 1
    
    return players
        