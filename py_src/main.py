from lib import add, qsort, search


def main():
    print("works?")
    print(add(11, 13))

    arr = [x % 11 for x in range(1, 50)]
    sorted_arr = qsort(arr)

    index = search(sorted_arr, 0)
    print(sorted_arr)
    print(f"{index} target index")
    print(f"{len(sorted_arr)} length of sorted arr")
    print(f"{sorted_arr[index]} val in arr at index")



if __name__ == "__main__":
    main()
