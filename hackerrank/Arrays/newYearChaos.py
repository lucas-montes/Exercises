def minimumBribes(q):
    bribes = 0
    for i,o in enumerate(q):
        cur = i + 1
        if o - cur > 2:
            return print('Too chaotic')

        for k in q[max(o - 2, 0):i]:

            if k > o:
                bribes += 1


    return print(bribes)