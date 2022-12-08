def repeatedString(s, n):
    return (s[:n%len(s)].count('a')+(s.count('a')*(n//len(s))))