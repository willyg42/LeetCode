def numIslands(grid):
    numIslands = 0
    def flood(r, c, grid):
        if r >= 0 and c >= 0 and r < len(grid) and c < len(grid[0]) and grid[r][c] == '1':
            grid[r][c] = '0'
            flood(r + 1, c, grid)
            flood(r - 1, c, grid)
            flood(r, c + 1, grid)
            flood(r, c - 1, grid)
        
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '1':
                numIslands+=1
                flood(r, c, grid)
    return numIslands


if __name__ == '__main__':
    assert numIslands([
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
    ]) == 1