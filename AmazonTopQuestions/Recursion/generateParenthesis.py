def generateParenthesis(n):
    result = []
    def generate(op = 0, closed = 0, res = []):
        if len(res) == 2 * n:
            result.append(''.join(res))
            return
        if op < n:
            res.append('(')
            generate(op + 1, closed, res)
            res.pop()
        if closed < op:
            res.append(')')
            generate(op, closed + 1, res)
            res.pop()
    generate()
    return result


if __name__ == '__main__':
    assert generateParenthesis(3) == ["((()))","(()())","(())()","()(())","()()()"]