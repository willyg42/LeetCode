from collections import deque


def zigzagLevelOrder(root):
    result = []
    def dfs(level, root):
        if root:
            if len(result) < level:
                result.append(deque([]))
            if level % 2 == 1:
                result[level - 1].append(root.val)
            else:
                result[level - 1].appendleft(root.val)
            dfs(level + 1, root.left)
            dfs(level + 1, root.right)
    dfs(1, root)
    return result