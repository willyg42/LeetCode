def trap(height):
    l, r = 0, len(height) - 1
    l_max, r_max = 0, 0
    total = 0
    while l < r:
        if height[l] < height[r]:
            if height[l] >= l_max:
                l_max = height[l]
            else:
                total += l_max - height[l]
            l += 1
        else:
            if height[r] >= r_max:
                r_max = height[r]
            else:
                total += r_max - height[r]
            r -= 1
    return total


if __name__ == '__main__':
    assert trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
    assert trap([4,2,0,3,2,5]) == 9