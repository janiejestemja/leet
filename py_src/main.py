from lib import add, qsort, search


def main():
    print("works?")
    print(add(11, 13))

    arr = [x % 11 for x in range(1, 50)]
    print(arr)
    sorted_arr = qsort(arr)
    print(sorted_arr)

    index = search(sorted_arr, 0)
    print(index)
    print(sorted_arr[index])



if __name__ == "__main__":
    main()
