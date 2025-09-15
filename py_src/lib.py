def add(left, right):
    return left + right


class Node():
    def __init__(self, ele, next=None):
        self.ele = ele
        self.next = next

    def __repr__(self):
        return f"Node({self.ele}, {self.next.ele})"

    # given an arr return nodes
    @staticmethod
    def from_arr(arr):
        # traverse from last to first and return first
        node = None
        for ele in reversed(arr):
            node = Node(ele, node)

        return node

    @staticmethod
    def from_node(node):
        arr = []

        while node:
            arr.append(node.ele)
            node = node.next

        return arr
