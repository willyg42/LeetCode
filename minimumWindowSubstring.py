from collections import Counter


def minWindow(s, t) :
    tCounter = Counter(t)
    l, r = 0, 0
    minRes = None
    while r < len(s):
        if s[r] in tCounter:
            tCounter[s[r]] -= 1
        while all(x <= 0 for x in tCounter.values()) and l <= r:
            if not minRes or r - l < len(minRes):
                minRes = s[l:r+1]
            if s[l] in tCounter:
                tCounter[s[l]] += 1
            l += 1
        r+=1
    return '' if not minRes else minRes


if __name__ == '__main__':
    assert minWindow('ADOBECODEBANC', 'ABC') == 'BANC'
    assert minWindow('A', 'A') == 'A'