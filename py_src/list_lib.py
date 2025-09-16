# linked list
class Node():
    def __init__(self, ele, next=None):
        self.ele = ele
        self.next = next

    def __repr__(self):
        return f"Node({self.ele}, {self.next})"

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
