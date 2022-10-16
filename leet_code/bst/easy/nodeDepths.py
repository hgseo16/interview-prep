def nodeDepths(root):
    def nodeDepth(root, distance):

        if root is None:
            return 0
        elif root.left is None and root.right is None:
            return distance
        else:
            sum = distance + nodeDepth(root.left, distance + 1) + nodeDepth(root.right, distance + 1)
            return sum

        # sum = distance + nodeDepth(root.left, distance + 1) + nodeDepth(root.right, distance + 1)
        # return sum

    return nodeDepth(root, 0)


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
