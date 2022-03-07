from collections import Counter
def sherlockAndAnagrams(s):
    count=0
    dic=Counter(s)
    for i in range(2,len(s)):
        sb=s[0:i]
        l=len(sb)
        dic["".join(sorted(sb))]+=1
        for j in range(1,len(s)):
            if j+l<=len(s):
                dic["".join(sorted(s[j:j+l]))]+=1

    for k,v in dic.items():
        count+=v*(v-1)//2
    return count