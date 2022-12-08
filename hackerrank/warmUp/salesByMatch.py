def sockMerchant(n, ar):
    flag = 0
    for i in range(n):
        if ar[i:].count(ar[i])%2==0:
            flag+=1
    return flag