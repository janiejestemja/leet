from lib import add, qsort, search


def main():
    print("works?")
    print(add(11, 13))

    arr = [x % 7 for x in range(1, 50)]
    print(arr)
    sorted_arr = qsort(arr)

    index = search(arr, 0)
    print(index)



if __name__ == "__main__":
    main()
