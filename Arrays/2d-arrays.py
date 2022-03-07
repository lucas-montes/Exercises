def hourglassSum(arr):
    sumas = []
    longitud = len(arr)
    max_long = longitud -2 #por ahora 4
    for i in range(0, max_long):

        for j in range(0, max_long):

            total = 0
            for k in range(3):

                for l in range (3):

                    if k == 1 and l in [0,2]:
                        continue

                    total += arr[i+k][j+l]
            sumas.append(total)


    return (max(sumas))