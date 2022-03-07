def rotLeft(a, d):
    for move in range(d):
        a.insert((len(a)-1),a.pop(0))
    return a