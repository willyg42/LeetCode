def threeSumClosest(nums, target):
    nums.sort()
    closestSum = float('inf')
    for i in range(len(nums)):
        if i == 0 or nums[i] != nums[i - 1]:
            j, k = i + 1, len(nums) - 1
            while j < k:
                cSum = nums[i] + nums[j] + nums[k]
                if cSum == target:
                    return cSum
                if abs(target - cSum) < abs(target - closestSum):
                    closestSum = cSum
                if cSum < target:
                    j += 1
                else:
                    k -= 1
    return closestSum


if __name__ == '__main__':
    assert threeSumClosest([-1,2,1,-4], 1) == 2
    assert threeSumClosest([0, 0, 0], 1) == 0