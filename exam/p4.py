def getSublists(L, n):
    res = []
    for i in xrange(len(L)-n+1):
        res.append(L[i:i+n])

    return res

def longestRun(L):
    longest = 1
    prevItem = L[0]
    current = 1
    for item in L[1:]:
        if item >= prevItem:
            current += 1
        else:
            longest = max(longest, current)
            current = 1
        prevItem = item

    return max(longest, current)

