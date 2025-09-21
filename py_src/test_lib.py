from list_lib import Node
from tree_lib import Tree
from lib import msort, qsort, search
from lib import get_medians, medSlideArr


def test_sorted_sliding_window():
    assert(medSlideArr([1,3,-1,-3,5,3,6,7], 3) == get_medians([1,3,-1,-3,5,3,6,7], 3))
    assert(medSlideArr([1,4,2,3], 4) == get_medians([1,4,2,3], 4))

    arr = [(-1)**(i % 3) * (x % 11) for i, x in enumerate(range(-22, 23))]
    k = 3
    assert(medSlideArr(arr, k) == get_medians(arr, k))


def test_sort_arrays():
    arr = [(-1)**(i % 3) * (x % 11) for i, x in enumerate(range(-22, 23))]
    qsort_arr = qsort(arr)
    msort_arr = msort(arr)
    assert(qsort_arr == msort_arr)

    mindex = search(qsort_arr, 0)
    qindex = search(msort_arr, 0)
    assert(qindex == mindex)


def test_sort_linkedlist():
    arr = [(-1)**(i % 3) * (x % 11) for i, x in enumerate(range(-22, 23))]
    unsorted = Node.from_arr(arr)

    msort_arr = msort(arr)
    presorted = Node.from_arr(msort_arr)

    from_sorted_nodes = Node.from_node(Node.sort_self(unsorted))

    for i, j in zip(msort_arr, from_sorted_nodes):
        assert(i == j)


def test_tree():
    arr = [(-1)**(i % 3) * (x % 11) for i, x in enumerate(range(-22, 23))]
    from_tree = Tree.from_tree(Tree.from_arr(arr))
    assert(arr == from_tree)


def test_trafo():
    # Array
    arr = [x for x in range(1, 20)]
    after_trafo = Node.from_node(Node.from_arr(arr))
    assert(arr == after_trafo)


def test_addition():
    # 342 + 465 = 807
    l1 = [2, 4, 3]
    l2 = [5, 6, 4]
    out = [7, 0, 8]

    lnode = Node.from_arr(l1)
    rnode = Node.from_arr(l2)
    out_node = Node.from_arr(out)

    as_node = lnode + rnode
    output = Node.from_node(as_node)

    assert(out == output)
    lnode = Node(0, None)
    rnode = Node(0, None)
    out =  [0]

    as_node = lnode + rnode
    output = Node.from_node(as_node)
    assert(out == output)

    # second testcase
    l1 = [0, 1, 0, 9, 9, 9, 9, 9, 9, 9]
    l2 = [0, 1, 0, 9, 9, 9, 9]
    out = [0, 2, 0, 8, 9, 9, 9, 0, 0, 0, 1]
    lnode = Node.from_arr(l1)
    rnode = Node.from_arr(l2)

    as_node = lnode + rnode
    output = Node.from_node(as_node)
    assert(out == output)
