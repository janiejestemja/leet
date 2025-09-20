# binary search tree
class Tree:
    def __init__(self, ele, left=None, right=None):
        self.ele = ele
        self.left = left
        self.right = right

    def __repr__(self):
        return f"T({self.ele}, {self.left}, {self.right})"

    @classmethod
    def from_arr(cls, arr):
        if len(arr) == 0:
            return None
        piv = len(arr) // 2
        root = Tree(arr[piv])
        root.left = cls.from_arr(arr[:piv])
        root.right = cls.from_arr(arr[piv + 1:])

        return root

    @classmethod
    def from_tree(cls, root):
        if not root:
            return []
        left = cls.from_tree(root.left)
        right = cls.from_tree(root.right)
        return left + [root.ele] + right
