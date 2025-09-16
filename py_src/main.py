from lib import add, qsort, search
from list_lib import Node


def main():
    print("works?")
    print(add(11, 13))
    l1 = [1, 0, 9, 9, 9, 9, 9, 9, 9]
    l2 = [1, 0, 9, 9, 9, 9]
    out = [2, 0, 8, 9, 9, 9, 0, 0, 0, 1]
    lnode = Node.from_arr(l1)
    rnode = Node.from_arr(l2)

    as_node = lnode + rnode
    output = Node.from_node(as_node)
    assert(out == output)


def legacy_main():

    arr = [x % 11 for x in range(1, 50)]
    sorted_arr = qsort(arr)

    index = search(sorted_arr, 0)
    print(sorted_arr)
    print(f"{index} target index")
    print(f"{len(sorted_arr)} length of sorted arr")
    print(f"{sorted_arr[index]} val in arr at index")


if __name__ == "__main__":
    main()
