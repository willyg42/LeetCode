def isSymmetric(root):
    def validate(lnode, rnode):
        if not lnode and not rnode:
            return True
        if not lnode or not rnode:
            return False
        return lnode.val == rnode.val and validate(lnode.left, rnode.right) and validate(lnode.right, rnode.left) 
            
    return validate(root.left, root.right)