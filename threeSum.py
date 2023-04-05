def threeSum(nums):
    nums.sort()
    results = []
    for i in range(len(nums)):
        if nums[i] > 0:
            break
        if i == 0 or nums[i - 1] != nums[i]:
            twoSum(nums, i, results)
    return results


def twoSum(nums, i, results):
    seen = set()
    j = i + 1
    while j < len(nums):
        complement = -nums[i] - nums[j]
        if complement in seen:
            results.append([nums[i], complement, nums[j]])
            while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                j += 1
        seen.add(nums[j])
        j += 1


if __name__ == '__main__':
    assert threeSum([-1,0,1,2,-1,-4]) == [[-1,0,1], [-1, -1, 2]]
    assert threeSum([0, 1, 1]) == []
    assert threeSum([0, 0, 0]) == [[0, 0, 0]]