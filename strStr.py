def strStr(haystack, needle):
    for i in range(len(haystack)):
        if haystack[i: i + len(needle)] == needle:
            return i
        return -1
    

if __name__ == '__main__':
    assert strStr('sadbutsad', 'sad') == 0
    assert strStr('leetcode', 'leeto') == -1