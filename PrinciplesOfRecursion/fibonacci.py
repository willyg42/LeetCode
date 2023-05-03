memo = [None] * (31)
memo[0] = 0
memo[1] = 1

def fib(n):        
    if memo[n] != None:
        return memo[n]
    memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]


if __name__ == '__main__':
    assert fib(30) == 832040
    assert fib(4) == 3