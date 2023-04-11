def productExceptSelf(nums):
    result = [1] * len(nums)
    
    lTotal = 1
    for i in range(len(nums)):
        result[i] = lTotal
        lTotal *= nums[i]

    rTotal = 1
    for i in reversed(range(len(nums))):
        result[i] *= rTotal
        rTotal *= nums[i]
    
    return result


if __name__ == '__main__':
    assert productExceptSelf([1,2,3,4]) == [24,12,8,6]
    assert productExceptSelf([-1,1,0,-3,3]) == [0,0,9,0,0]