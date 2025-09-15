from lib import Node


def test_Node():
    # Array
    arr = [x for x in range(1, 20)]
    after_trafo = Node.from_node(Node.from_arr(arr))
    assert(arr == after_trafo)
