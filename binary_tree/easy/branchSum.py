# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    if root is None:
        return []

    branches = branchSums(root.left) + branchSums(root.right)

    if branches:
        return [branch + root.value for branch in branches]
    else:
        return [root.value]
