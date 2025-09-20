# linked list
class Node():
    def __init__(self, ele, next=None):
        self.ele = ele
        self.next = next

    def __repr__(self):
        return f"Node({self.ele}, {self.next})"

    # Constructors for convenience
    # given an arr return nodes
    @staticmethod
    def from_arr(arr):
        # traverse from last to first and return first
        node = None
        for ele in reversed(arr):
            node = Node(ele, node)

        return node

    # given nodes return arr
    @staticmethod
    def from_node(node):
        arr = []

        while node:
            arr.append(node.ele)
            node = node.next

        return arr

    def __add__(self, other):
        lnode = self
        rnode = other

        carry = 0
        node = None
        tail = None
        while lnode or rnode or carry > 0:
            temp = carry

            if lnode:
                temp += lnode.ele
                lnode = lnode.next

            if rnode:
                temp += rnode.ele
                rnode = rnode.next

            digit = temp % 10
            carry = temp // 10

            if node:
                tail.next = Node(digit, None)
                tail = tail.next
            else:
                node = Node(digit, None)
                tail = node

        return node

    # Three mergefunction methodology
    @classmethod
    def sort_self(cls, node):
        if not node or not node.next:
            return node

        left, right = cls.csplit(node)
        left = cls.sort_self(left)
        right = cls.sort_self(right)

        return cls.merge(left, right)

    @staticmethod
    def merge(left, right):
        start = Node(None, None)
        tail = start

        while left and right:
            if left.ele <= right.ele:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next

            tail = tail.next
        tail.next = left or right
        return start.next

    @staticmethod
    def csplit(node):
        if not node or not node.next:
            return node, None
        slow, fast, prev = node, node, None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None

        return node, slow

    @staticmethod
    def check_circle(node):
        slow, fast = node, node

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
