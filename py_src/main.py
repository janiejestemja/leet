from lib import add, qsort, search, msort
from list_lib import Node


def main():
    print("works?")
    print(add(11, 13))

    arr = [x for x in range(1, 8)]
    tarr = Tree.from_arr(arr)
    from_tarr = Tree.from_tree(tarr)
    print(tarr)
    print(from_tarr)


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


def circle_main():
    arr = [(-1)**(i % 3) * (x % 11) for i, x in enumerate(range(-22, 23))]
    print(arr)
    node = Node.from_arr(arr)

    circle = make_circle(node, 5)

    print(Node.check_circle(node))
    print(Node.check_circle(circle))


def make_circle(node, index):
    start = Node(None, None)
    tail = start

    counter = 0
    circlepoint = None
    while node:
        if counter == index:
            tail.next = node
            circlepoint = tail
            node = node.next
        else:
            tail.next = node
            node = node.next
        counter += 1
    tail.next = circlepoint

    return start.next


# Searching a very sorted 2D matrix
def qsearch(mat, tar):
    if not mat or not mat[0]:
        return False

    row, col = 0, len(mat[0]) - 1

    while row < len(mat) and 0 <= col:
        cur = mat[row][col]
        if cur == tar:
            return True
        elif cur > tar:
            col -= 1
        else:
            row += 1

    return False


def qsearch_main():
    arr = [(-1)**(i % 3) * (x % 11) for i, x in enumerate(range(-22, 23))]
    qsort_arr = qsort(arr)
    msort_arr = msort(arr)
    assert(qsort_arr == msort_arr)

    mindex = search(qsort_arr, 0)
    qindex = search(msort_arr, 0)
    assert(qindex == mindex)

    print(arr)
    print(qsort_arr)
    print(msort_arr)
    print(mindex)
    print(qindex)

    # for matrix
    mat = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
    tar = 5
    tara = 0
    mat = [[-1], [1]]
    mat = [[1, 3, 5]]
    tara = 4

    x = qsearch(mat, tar)
    print(x)
    x = qsearch(mat, tara)
    print(x)


if __name__ == "__main__":
    main()
