def maxPathSum(root):
    maxSum = -float('inf')
    def dfs(root):
        nonlocal maxSum
        if not root:
            return 0
        
        leftMax = max(dfs(root.left), 0)
        rightMax = max(dfs(root.right), 0)
        maxSum = max(maxSum, leftMax + rightMax + root.val)
        return max(leftMax , rightMax) + root.val
    dfs(root)
    return maxSum