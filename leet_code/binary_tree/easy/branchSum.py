class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    if root is None:
        return []
    elif root.left is None and root.right is None:
        return [root.value]
    else:
        branchSumList = branchSums(root.left) + branchSums(root.right)
        return [root.value + branchSum for branchSum in branchSumList]