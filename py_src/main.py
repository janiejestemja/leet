from lib import add, Node


def main():
    print("works?")
    print(add(11, 13))

    # 342 + 465 = 807
    # setup solution for comparison
    solution = 807
    l1 = [2, 4, 3]
    l2 = [5, 6, 4]
    out = [7, 0, 8]

    larr = Node.from_arr(l1)
    rarr = Node.from_arr(l2)
    out_node = Node.from_arr(out)

    sol, as_node = Node.add_nodes(larr, rarr)
    output = Node.from_node(as_node)

    assert(out == output)
    assert(sol == solution)


if __name__ == "__main__":
    main()
