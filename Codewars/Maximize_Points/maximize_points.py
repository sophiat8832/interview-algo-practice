def maximize_points(team1, team2):
    team1.sort()
    team2.sort()
    result, i, j = 0, 0, 0
    while i < len(team1):
        if team1[i] > team2[j]: 
            result += 1
        else:
            j -= 1
        i += 1
        j += 1  
    return result