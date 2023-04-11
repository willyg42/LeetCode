from collections import Counter 


def firstUniqueChar(s):
    charCounter = Counter(s)
    for i, c in enumerate(s):
        if charCounter[c] == 1:
            return i
    return -1


if __name__ == '__main__':
    assert firstUniqueChar('loveleetcode') == 2
    assert firstUniqueChar('aabb') == -1
    assert firstUniqueChar('leetcode') == 0