# linked list
class Node():
    def __init__(self, ele, next=None):
        self.ele = ele
        self.next = next

    def __repr__(self):
        return f"Node({self.ele}, {self.next})"

    def __add__(self, other):
        # setup solution
        sol = 0

        # digit multiplication in decimal system
        expon = 1
        # traverse left side
        node = self
        while node:
            sol += node.ele * expon
            expon *= 10
            node = node.next

        # traverse right side
        expon = 1
        node = other
        while node:
            sol += node.ele * expon
            expon *= 10
            node = node.next

        # got solution
        # trafo into nodes (node is already none)
        for ele in str(sol):
            node = Node(int(ele), node)

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
