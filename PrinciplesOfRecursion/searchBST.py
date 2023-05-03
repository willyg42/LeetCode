def searchBST(root, val):
    if not root or val == root.val:
        return root
    
    return searchBST(root.left, val) if val < root.val else searchBST(root.right, val)