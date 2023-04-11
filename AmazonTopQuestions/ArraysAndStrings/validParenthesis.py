def isValid(s):
    stack = []
    openParen = {'[', '(', '{'}
    closedParen = {'}': '{', ')': '(', ']': '['}
    for c in s:
        if c in openParen:
            stack.append(c)
        elif c in closedParen and stack and stack[-1] == closedParen[c]:
            stack.pop()
        else:
            return False
    return not stack


if __name__ == '__main__':
    assert isValid('()[]{}') == True
    assert isValid(']') == False
    assert isValid('(])') == False