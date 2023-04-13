def generateParenthesis(n):
    result = []
    
    def generate(nOpen = 0, nClosed = 0, r=[]):
        if len(r) == n * 2:
            result.append(''.join(r))
            return result
        if nOpen < n:
            r.append('(')
            generate(nOpen + 1, nClosed, r)
            r.pop()
        if nClosed < nOpen:
            r.append(')')
            generate(nOpen, nClosed + 1, r)
            r.pop()

    generate()
    return result


if __name__ == '__main__':
    assert generateParenthesis(3) == ["((()))","(()())","(())()","()(())","()()()"]