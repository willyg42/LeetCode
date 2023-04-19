def exist(board, word):
    def dfs(r, c, rem):
        if len(rem) == 0:
            return True
        
        if r < 0 or r == len(board) or c < 0 or c == len(board[0]):
            return False
        
        if board[r][c] != rem[0]:
            return False
        
        board[r][c] = '#'
        res = False
        for rDelta, cDelta in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            res = dfs(r + rDelta, c + cDelta, rem[1:])
            if res:
                break
        board[r][c] = rem[0]
        return res
    
    for r in range(len(board)):
        for c in range(len(board[0])):
            if dfs(r, c, word):
                return True
    return False


if __name__ == '__main__':
    assert exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], 'SEE')
    assert exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], 'ABCB') == False