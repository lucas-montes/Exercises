def countingValleys(steps, path):
    valleys = 0
    sea_level = 0

    for i in range(steps):
        
        if path[i] == 'U':
            sea_level +=1
            if sea_level == 0:
                valleys += 1

        elif path[i] == 'D':
            sea_level -=1

    return valleys