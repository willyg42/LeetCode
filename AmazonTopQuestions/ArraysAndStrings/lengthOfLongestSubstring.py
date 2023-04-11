def lengthOfLongestSubstring(s):
    charIndex = {}
    l = -1
    maxLength = 0
    for i, c in enumerate(s):
        if c in charIndex and charIndex[c] > l:
            l = charIndex[c]
        maxLength = max(maxLength, i - l)
        charIndex[c] = i
    return maxLength


if __name__ == '__main__':
    assert lengthOfLongestSubstring('abcabcbb') == 3
    assert lengthOfLongestSubstring(' ') == 1
    assert lengthOfLongestSubstring('') == 0
    assert lengthOfLongestSubstring('pwwkew') == 3
    assert lengthOfLongestSubstring('bbbbbb') == 1