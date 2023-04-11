def rotate(matrix):
    transpose(matrix)
    reflect(matrix)


def transpose(matrix):
    for r in range(len(matrix)):
        for c in range(r + 1, len(matrix)):
            matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]


def reflect(matrix):
    for r in range(len(matrix)):
        for c in range(len(matrix) // 2):
            matrix[r][c], matrix[r][-c-1] = matrix[r][-c-1], matrix[r][c] 


if __name__ == '__main__':
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    rotate(matrix)
    assert matrix == [[7,4,1],[8,5,2],[9,6,3]]
    matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    rotate(matrix)
    assert matrix == [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]