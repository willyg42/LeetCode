def missingNumber(nums):
    N = len(nums)
    total1 = 0
    total2 = 0
    for i, n in enumerate(nums):
        total1 += n
        total2 += (i + 1)
    return total2 - total1


if __name__ == '__main__':
    assert missingNumber([9,6,4,2,3,5,7,0,1]) == 8
    assert missingNumber([0,1]) == 2
    assert missingNumber([3,0,1]) == 2