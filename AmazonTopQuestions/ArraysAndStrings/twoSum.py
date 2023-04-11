def twoSum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        if target - num in seen:
            return (seen[target - num], i)
        seen[num] = i
    

if __name__ == '__main__':
    nums = [9,19,20,10,4,3,-1]
    assert twoSum(nums, 8) == (0, 6)
