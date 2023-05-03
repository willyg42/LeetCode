def reverseString(s):
    l, r = 0, len(s) - 1
    while l < r:
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1


if __name__ == '__main__':
    str1 = ['h', 'e', 'l', 'l', 'o']
    reverseString(str1)
    assert str1 == ['o', 'l', 'l', 'e', 'h']