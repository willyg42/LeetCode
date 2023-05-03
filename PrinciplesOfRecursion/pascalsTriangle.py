def getRow(rowIndex):
    if rowIndex == 0:
        return [1]
    lastRow = getRow(rowIndex - 1)
    newRow = []
    for i in range(len(lastRow) + 1):
        if i == 0 or i == len(lastRow):
            newRow.append(1)
        else:
            newRow.append(lastRow[i] + lastRow[i - 1])
    return newRow


if __name__ == '__main__':
    assert getRow(3) == [1, 3, 3, 1]