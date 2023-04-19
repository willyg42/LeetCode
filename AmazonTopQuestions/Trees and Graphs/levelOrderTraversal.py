def levelOrder(root):
    def traverse(node, level, result):
        if node:
            if len(result) <= level:
                result.append([])
            result[level].append(node.val)
            traverse(node.left, level + 1, result)
            traverse(node.right, level + 1, result)
    
    result = []
    traverse(root, 0, result)
    return result